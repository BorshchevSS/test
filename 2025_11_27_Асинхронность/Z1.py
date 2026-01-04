import asyncio
import random
import time

TOTAL = 10
TEMP_SENSOR = "Датчик температуры"
HUMIDITY_SENSOR = "Датчик влажности"

#Карутина которая будет собирать данные
async def read_sensor(sensor_name):
    delay = random.uniform(0.5, 1.5)
    print(f"{sensor_name} запуск изменения. Ожидание: {delay: .2f}сек.")
    await asyncio.sleep(delay)
    if sensor_name == TEMP_SENSOR:
        value = round(random.uniform(20.0, 30.0), 1)
        unit = "°C"
