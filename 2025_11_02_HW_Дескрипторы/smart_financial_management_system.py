import datetime
from typing import Dict, List, Optional, Union


class FinancialDescriptor:
    """Базовый дескриптор для всех финансовых атрибутов"""

    def __init__(self, min_value: float = None, max_value: float = None):
        self.min_value = min_value
        self.max_value = max_value
        self.history = []
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, f"_{self._name}", 0.0)

    def __set__(self, obj, value):
        self._validate(value)
        old_value = getattr(obj, f"_{self._name}", 0.0)

        # Сохраняем в историю
        self.history.append({
            'timestamp': FinancialAccount._get_current_timestamp(),
            'old_value': old_value,
            'new_value': value,
            'attribute': self._name
        })

        setattr(obj, f"_{self._name}", value)

    def _validate(self, value: float):
        """Валидация минимальных/максимальных значений"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"Значение {self._name} должно быть числом")

        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Значение {self._name} не может быть меньше {self.min_value}")

        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Значение {self._name} не может быть больше {self.max_value}")


class BalanceDescriptor(FinancialDescriptor):
    """Дескриптор для баланса счета"""

    def __init__(self, is_credit: bool = False, credit_limit: float = 0):
        super().__init__(min_value=0 if not is_credit else -credit_limit)
        self.is_credit = is_credit
        self.credit_limit = credit_limit

    def check_sufficient_funds(self, obj, amount: float) -> bool:
        """Проверка достаточности средств"""
        current_balance = getattr(obj, f"_{self._name}", 0.0)
        return current_balance >= amount if not self.is_credit else current_balance - amount >= -self.credit_limit


class TransactionAmountDescriptor(FinancialDescriptor):
    """Дескриптор для суммы транзакции"""

    def __init__(self):
        super().__init__(min_value=0.01)
        self.commission_rate = 0.01  # 1% комиссия

    def calculate_commission(self, amount: float) -> float:
        """Расчет комиссии"""
        return amount * self.commission_rate

    def get_total_amount(self, amount: float) -> float:
        """Получение общей суммы с комиссией"""
        return amount + self.calculate_commission(amount)


class CategoryDescriptor(FinancialDescriptor):
    """Дескриптор для категорий расходов"""

    VALID_CATEGORIES = {
        'food', 'transport', 'entertainment', 'utilities',
        'healthcare', 'education', 'shopping', 'other'
    }

    def __init__(self):
        super().__init__()
        self.category_limits = {category: None for category in self.VALID_CATEGORIES}
        self.monthly_spending = {category: 0.0 for category in self.VALID_CATEGORIES}
        self.current_month = datetime.datetime.now().month

    def _validate(self, value: str):
        """Валидация категории"""
        if value not in self.VALID_CATEGORIES:
            raise ValueError(f"Недопустимая категория. Допустимые категории: {', '.join(self.VALID_CATEGORIES)}")

        # Сброс месячной статистики при смене месяца
        current_month = datetime.datetime.now().month
        if current_month != self.current_month:
            self.monthly_spending = {category: 0.0 for category in self.VALID_CATEGORIES}
            self.current_month = current_month

    def set_category_limit(self, category: str, limit: float):
        """Установка лимита для категории"""
        if category not in self.VALID_CATEGORIES:
            raise ValueError(f"Недопустимая категория: {category}")
        self.category_limits[category] = limit

    def check_category_limit(self, category: str, amount: float) -> bool:
        """Проверка лимита категории"""
        if category not in self.category_limits or self.category_limits[category] is None:
            return True

        return self.monthly_spending[category] + amount <= self.category_limits[category]

    def add_spending(self, category: str, amount: float):
        """Добавление расходов по категории"""
        if category in self.monthly_spending:
            self.monthly_spending[category] += amount


class FinancialAccount:
    """Основной класс для управления финансовым счетом"""

    # Курсы валют (статическое свойство)
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.73,
        'JPY': 110.0,
        'RUB': 75.0
    }

    def __init__(self, account_name: str, initial_balance: float = 0.0,
                 currency: str = 'USD', is_credit: bool = False,
                 credit_limit: float = 0.0):
        self.account_name = account_name
        self.currency = currency
        self.creation_date = self._get_current_timestamp()

        # Инициализация дескрипторов
        self._balance = BalanceDescriptor(is_credit, credit_limit)
        self._transaction_amount = TransactionAmountDescriptor()
        self._category = CategoryDescriptor()

        # Установка начального баланса
        self._balance_value = initial_balance
        self._total_commission = 0.0

        # Статистика
        self._transactions = []

    # Дескрипторы
    balance = BalanceDescriptor()
    transaction_amount = TransactionAmountDescriptor()
    category = CategoryDescriptor()

    @property
    def age_days(self) -> int:
        """Количество дней с момента создания счета"""
        return (datetime.datetime.now() - self.creation_date).days

    @property
    def total_commission_paid(self) -> float:
        """Общая сумма уплаченных комиссий"""
        return self._total_commission

    @property
    def monthly_statistics(self) -> Dict:
        """Статистика за текущий месяц"""
        return {
            'total_spent': sum(self.category.monthly_spending.values()),
            'by_category': self.category.monthly_spending.copy(),
            'category_limits': self.category.category_limits.copy(),
            'commission_paid': self._total_commission
        }

    @classmethod
    def convert_currency(cls, amount: float, from_currency: str, to_currency: str) -> float:
        """Конвертация между валютами"""
        if from_currency not in cls.exchange_rates or to_currency not in cls.exchange_rates:
            raise ValueError("Недопустимая валюта")

        usd_amount = amount / cls.exchange_rates[from_currency]
        return usd_amount * cls.exchange_rates[to_currency]

    @classmethod
    def set_exchange_rate(cls, currency: str, rate: float):
        """Установка курса валюты"""
        cls.exchange_rates[currency] = rate

    @staticmethod
    def _get_current_timestamp() -> datetime.datetime:
        """Получение текущего времени"""
        return datetime.datetime.now()

    def make_transaction(self, amount: float, category: str, description: str = "") -> bool:
        """Проведение транзакции с полной валидацией"""
        try:
            # Валидация суммы транзакции
            self.transaction_amount._validate(amount)

            # Валидация категории
            self.category._validate(category)

            # Проверка лимита категории
            if not self.category.check_category_limit(category, amount):
                raise ValueError(f"Превышен месячный лимит для категории '{category}'")

            # Расчет комиссии и общей суммы
            commission = self.transaction_amount.calculate_commission(amount)
            total_amount = amount + commission

            # Проверка достаточности средств
            if not self.balance.check_sufficient_funds(self, total_amount):
                raise ValueError("Недостаточно средств для проведения транзакции")

            # Выполнение транзакции
            self._balance_value -= total_amount
            self._total_commission += commission

            # Обновление статистики
            self.category.add_spending(category, amount)

            # Запись транзакции
            transaction = {
                'timestamp': self._get_current_timestamp(),
                'amount': amount,
                'category': category,
                'commission': commission,
                'description': description,
                'balance_after': self._balance_value
            }
            self._transactions.append(transaction)

            print(f"Транзакция выполнена: -{amount:.2f} {self.currency} "
                  f"(комиссия: {commission:.2f}) | Категория: {category}")
            return True

        except (ValueError, TypeError) as e:
            print(f"Ошибка транзакции: {e}")
            return False

    def deposit(self, amount: float, description: str = ""):
        """Пополнение счета"""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")

        self._balance_value += amount

        transaction = {
            'timestamp': self._get_current_timestamp(),
            'amount': amount,
            'category': 'deposit',
            'commission': 0.0,
            'description': description,
            'balance_after': self._balance_value
        }
        self._transactions.append(transaction)

        print(f"Счет пополнен: +{amount:.2f} {self.currency}")

    def set_category_limit(self, category: str, limit: float):
        """Установка лимита для категории расходов"""
        self.category.set_category_limit(category, limit)
        print(f"Лимит для категории '{category}' установлен: {limit:.2f} {self.currency}")

    def get_balance(self) -> float:
        """Получение текущего баланса"""
        return self._balance_value

    def get_transaction_history(self) -> List[Dict]:
        """Получение истории транзакций"""
        return self._transactions.copy()

    def __str__(self) -> str:
        """Строковое представление объекта"""
        return (f"Счет: {self.account_name}\n"
                f"Баланс: {self._balance_value:.2f} {self.currency}\n"
                f"Возраст счета: {self.age_days} дней\n"
                f"Всего комиссий уплачено: {self._total_commission:.2f} {self.currency}\n"
                f"Количество транзакций: {len(self._transactions)}")


# Пример использования
if __name__ == "__main__":
    # Создание счета
    account = FinancialAccount("Основной счет", 1000.0, "USD")

    # Установка лимитов по категориям
    account.set_category_limit('food', 200.0)
    account.set_category_limit('entertainment', 100.0)

    # Проведение транзакций
    account.make_transaction(50.0, 'food', 'Продукты')
    account.make_transaction(30.0, 'entertainment', 'Кино')
    account.make_transaction(25.0, 'transport', 'Такси')

    # Пополнение счета
    account.deposit(200.0, 'Зарплата')

    # Вывод информации
    print("\n" + "=" * 50)
    print(account)
    print("\nМесячная статистика:")
    print(account.monthly_statistics)

    # Пример конвертации валют
    converted = FinancialAccount.convert_currency(100, 'USD', 'EUR')
    print(f"\n100 USD = {converted:.2f} EUR")
