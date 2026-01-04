import asyncio
import random
import time

TOTAL_TIME = 10
TEMP_SENSOR = 'Датчик температуры'
HUMIDITY_SENSOR = 'Датчик влажности'

async def read_sensor(sensor_name):
    delay = random.uniform(0.5, 1.5)
    print(f'{sensor_name} запуск измерения. '
          f'ожидание: {delay:.2f}сек.')
    await asyncio.sleep(delay)
    if sensor_name == TEMP_SENSOR:
        value = round(random.uniform(20.0, 30.0), 1)
        unit = '°C '
    else:
        value = round(random.uniform(50.0, 70.0), 1)
        unit = '%'
    print(f'{sensor_name} готово. значение: {value}{unit}')

async def greenhouse_monitor(sensor_name):
#     основная корутина (для мониторинга одного датчика)
    start_time = time.time()
    while time.time() - start_time < TOTAL_TIME:
        try:
            await read_sensor(sensor_name)
        except asyncio.CancelledError:
            print(f'{sensor_name}: мониторинг отменен')
            break
        await asyncio.sleep(0.1)
    print(f'{sensor_name}. мониторинг завершен по таймеру')

async def main():
    task_temp = asyncio.create_task(greenhouse_monitor(TEMP_SENSOR))
    task_humidity = asyncio.create_task(greenhouse_monitor(HUMIDITY_SENSOR))
    await asyncio.gather(task_temp, task_humidity)
    print('датчики завершили работу')

if __name__ == '__main__':
    asyncio.run(main())