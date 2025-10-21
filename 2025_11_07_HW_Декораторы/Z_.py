import time
import functools
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional

# Базовая функция обработки транзакций (не изменяем)
def process_transaction(account_id: int, amount: float, transaction_type: str) -> dict:
    """
    Базовая функция обработки банковских транзакций.
    В реальной системе здесь была бы логика работы с базой данных.
    """
    # Имитация обработки транзакции
    time.sleep(0.01) # Небольшая задержка для имитации работы

    # Простая логика для демонстрации
    if transaction_type == "deposit":
        result = {"status": "success", "message": f"Депозит {amount} на счет {account_id} выполнен"}
    elif transaction_type == "withdraw":
        if amount > 10000: # Простая проверка для демонстрации
            result = {"status": "error", "message": "Недостаточно средств"}
        else:
            result = {"status": "success", "message": f"Снятие {amount} со счета {account_id} выполнено"}
    else:
        result = {"status": "error", "message": "Неизвестный тип транзакции"}

    return result

# 1. Декоратор логирования
def log_transaction(func):
    @functools.wraps(func)
    def wrapper(account_id: int, amount: float, transaction_type: str, *args, **kwargs):
        start_time = time.time()
        result = func(account_id, amount, transaction_type, *args, **kwargs)
        end_time = time.time()

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "account_id": account_id,
            "amount": amount,
            "transaction_type": transaction_type,
            "result": result,
            "processing_time": f"{end_time - start_time:.4f} сек"
        }

        # Вывод в консоль
        print(f"[LOG] {log_entry['timestamp']} | Счет: {account_id} | "
              f"Операция: {transaction_type} | Сумма: {amount} | "
              f"Результат: {result['status']} | Время: {log_entry['processing_time']}")

        # Запись в файл
        with open("transactions.log", "a", encoding="utf-8") as f:
            f.write(str(log_entry) + "\n")

        return result
    return wrapper

# 2. Декоратор контроля доступа
def require_role(required_role: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(account_id: int, amount: float, transaction_type: str, *args, **kwargs):
            # Получаем роль пользователя из контекста (в реальной системе из базы данных)
            user_role = kwargs.get('user_role', 'client')

            # Проверка прав доступа
            if user_role == "client":
                if transaction_type == "withdraw" and amount > 50000:
                    return {
                        "status": "error",
                        "message": f"Клиенты не могут снимать более 50,000. Попытка снять: {amount}"
                    }
                elif transaction_type == "deposit" and amount > 100000:
                    return {
                        "status": "error",
                        "message": f"Клиенты не могут вносить более 100,000. Попытка внести: {amount}"
                    }
            elif user_role == "manager":
                # Менеджеры имеют больше прав
                if transaction_type == "withdraw" and amount > 200000:
                    return {
                        "status": "error",
                        "message": f"Менеджеры не могут снимать более 200,000. Попытка снять: {amount}"
                    }

            # Если проверка пройдена, выполняем транзакцию
            return func(account_id, amount, transaction_type, *args, **kwargs)
        return wrapper
    return decorator

# 3. Декоратор ограничения частоты операций
def limit(rate: int, period: int):
    def decorator(func):
        # Храним историю вызовов по account_id
        call_history: Dict[int, List[float]] = {}

        @functools.wraps(func)
        def wrapper(account_id: int, amount: float, transaction_type: str, *args, **kwargs):
            current_time = time.time()

            # Инициализируем историю для account_id если нужно
            if account_id not in call_history:
                call_history[account_id] = []

            # Удаляем старые записи (старше period секунд)
            call_history[account_id] = [
                call_time for call_time in call_history[account_id]
                if current_time - call_time <= period
            ]

            # Проверяем не превышен ли лимит
            if len(call_history[account_id]) >= rate:
                return {
                    "status": "error",
                    "message": f"Превышен лимит операций. Не более {rate} операций за {period} секунд"
                }

            # Добавляем текущий вызов в историю
            call_history[account_id].append(current_time)

            # Выполняем транзакцию
            return func(account_id, amount, transaction_type, *args, **kwargs)
        return wrapper
    return decorator

# 4. Декоратор кэширования баланса
def cache_balance(ttl: int):
    def decorator(func):
        cache: Dict[int, Dict[str, Any]] = {}

        @functools.wraps(func)
        def wrapper(account_id: int, amount: float, transaction_type: str, *args, **kwargs):
            current_time = time.time()

            # Проверяем есть ли актуальный кэш для этого счета
            if account_id in cache:
                cache_entry = cache[account_id]
                if current_time - cache_entry['timestamp'] <= ttl:
                    # Возвращаем результат из кэша
                    print(f"[CACHE] Использован кэш для счета {account_id}")
                    return cache_entry['result']

            # Выполняем транзакцию и кэшируем результат
            result = func(account_id, amount, transaction_type, *args, **kwargs)

            # Кэшируем только успешные операции
            if result.get('status') == 'success':
                cache[account_id] = {
                    'result': result,
                    'timestamp': current_time
                }

            return result
        return wrapper
    return decorator

# Применяем все декораторы к основной функции
@log_transaction
@require_role("client")
@limit(rate=5, period=60) # Не более 5 операций в минуту
@cache_balance(ttl=30) # Кэш на 30 секунд
def decorated_process_transaction(account_id: int, amount: float, transaction_type: str, **kwargs):
    return process_transaction(account_id, amount, transaction_type)

# Демонстрация работы системы
if __name__ == "__main__":
    print("=== Демонстрация системы банковских операций ===\n")

    # Тестовые транзакции
    test_transactions = [
        (1001, 1000, "deposit"),
        (1001, 500, "withdraw"),
        (1001, 60000, "withdraw"), # Должен быть отклонен из-за лимита для клиентов
        (1002, 2000, "deposit"),
        (1001, 300, "withdraw"),
        (1001, 400, "withdraw"),
        (1001, 500, "withdraw"), # 5-я операция для счета 1001
        (1001, 600, "withdraw"), # Должен быть отклонен из-за лимита частоты
    ]

    for i, (account_id, amount, transaction_type) in enumerate(test_transactions, 1):
        print(f"\n--- Транзакция {i} ---")
        result = decorated_process_transaction(
            account_id,
            amount,
            transaction_type,
            user_role="client" # Роль пользователя
        )
        print(f"Результат: {result}")

        # Небольшая пауза между транзакциями
        if i < len(test_transactions):
            time.sleep(1)

    print("\n=== Демонстрация завершена ===")
"""

Этот код реализует все требуемые функции:

1. Логирование (@log_transaction)

· Записывает детали каждой транзакции в консоль и файл transactions.log
· Включает время, тип операции, сумму, ID счета и результат

2. Контроль доступа (@require_role(role))

· Проверяет права пользователя на основе роли
· Клиенты не могут снимать более 50,000
· Можно легко расширить для других ролей

3. Лимит операций (@limit(rate, period))

· Ограничивает количество операций для каждого счета
· В примере: не более 5 операций в минуту для одного account_id

4. Кэширование баланса (@cache_balance(ttl))

· Кэширует результаты успешных операций на указанное время
· Уменьшает нагрузку на систему при частых запросах

Особенности реализации:

· Декораторы применяются в правильном порядке для оптимальной работы
· Сохраняется исходная функция process_transaction без изменений
· Все декораторы используют functools.wraps для сохранения метаданных
· Система легко расширяема для добавления новой функциональности

Запустите код, чтобы увидеть систему в действии с тестовыми транзакциями!"""