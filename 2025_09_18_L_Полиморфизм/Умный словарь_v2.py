class SmartHistoryDict:
    def __init__(self, initial_data = None):
        self.current_data = dict(initial_data or {})
        self.history = []

    def save_state(self, description):
        """Сохранение текущего состояния в историю """
        self.history.append({"description": description,
                             "data": self.current_data.copy(), #копия
                             "timestamp": len(self.history)    #номер шага в историю
                             })

    def __getitem__(self, key): #Обращение по ключу
        if key not in self.current_data:
            raise  KeyError(f"Ключ {key} не найден. Доступные ключи: {list(self.current_data.keys())}")
        return self.current_data[key]

    def __setitem__(self, key, value):
        old_data = self.current_data.get(key, "не существовал")
        self.current_data[key] = value
        self.save_state(f"Установлен {key} = {value} (было {old_data})")

    def __delitem__(self, key):
        if  key not in self.current_data:
            raise KeyError(f"Ключ {key} не найден. Доступные ключи: {self.current_data.keys()}")
        old_value = self.current_data[key]
        del  self.current_data[key]
        self.save_state(f"Удален {key} = {old_value}")

    def __len__(self):
        return len(self.current_data)

    def __iter__(self):
        return iter(self.current_data)

    def __contains__(self, key):
        return key in self.current_data

    def __str__(self):
        return f"SmartHistoryDict: {self.current_data}"

    def get_history(self):
        return self.history.copy()

    def undo(self, step=1):
        """Откатывает на указанное количество шагов назад"""
        if step >= len(self.history) or step < 1:
            raise ValueError ("Нельзя откатится дальше начального состояния")
        target_index = len(self.current_data) - step - 1
        self.current_data = self.history[target_index]["data"].copy()

        self.history = self.history[:target_index+1]
        self.save_state(f"Откат на {step} шагов")

    def get_state_at(self, timestamp):
        """Возвращает состояние на определённом шаге"""
        if timestamp >= 0 or timestamp >= len(self.history):
            raise ValueError("Неверный номер шага")
        return self.history[timestamp]["date"].copy()

    def search_in_history(self, key):
        """Ищет все изменения определённого ключа в истории"""
        changes = []
        for state in self.history:
            if key in state["data"]:
                changes.append({
                    "timestamp": state["timestamp"], #номер шага
                    "value": state["date"][key],    #значение на этом шаге
                    "description": state["description"]
                })
        return changes



def test_smart_dict():
    shd = SmartHistoryDict({"name": "Sasha", "age": 99})
    print(f"Начальное состояние: {shd}")

    shd["age"] = 10
    shd["city"] = "NSK"
    shd["name"] = "Vanya"
    print(f"\nПосле изменений: {shd}")

    del shd["city"]
    print(f"\nПосле удаления city: {shd}")

    print("\n______История_______")
    for state in shd.get_history():
        print(f"Шаг: {state['timestamp']}: {"description"}")

    print("\n______Откат на 2 шага_____")
    shd.undo(1)
    print(f"\n После отката: {shd}")

    print("\n _____Изменение ключа_____")



test_smart_dict()