"""Задание 3
Задача: реализовать менеджер контекста для работы с кэшом.
Менеджер должен хранить кэш в словаре и автоматически очищать его при выходе из блока with."""

class CacheManager:
    def __init__(self, cache_dict):
        self.cache = cache_dict
        print("кэш-менеджер инициилизорван")

    def __enter__(self):
        print(f"текущий размер кэша {len(self.cache)}")
        return self.cache

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"очищаем кэш: {len(self.cache)}")
        self.cache.clear()
        print(f"новый размер: {len(self.cache)}")
        return False # если есть исключение будет переброшено

#создаем КЭШ
app_cache = {
    "user_1": "dats_a",
    "user_2": "dats_b",
    "session_id": 12345,
}

print(f"кэш до {app_cache}")
with    CacheManager(app_cache) as cur_cache:
    print(f"кэш внутри блока {cur_cache}")
    cur_cache["pow_key"] = "new_value"
    print(f"Кэш после добавления: {cur_cache}")
print(app_cache)