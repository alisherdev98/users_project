import asyncio
import time
import random

EMPLOYEES = ["Иван", "Петр", "Сергей",]


async def calculate_zp(employee, time_sleep):
    print(f"{employee} : \n -------------")
    await asyncio.sleep(time_sleep) #time.sleep(2)

    print(f"{employee} finish, time sleep: {time_sleep}")

    time_sleep2 = random.randint(1, 5)
    await asyncio.sleep(time_sleep2)

    print(f"{employee} second finish, time sleep: {time_sleep2}")

    print('Расчитать часы')
    print("Расчитать налоги")
    return employee

async def main():
    tasks = []
    for employee in EMPLOYEES:
        tasks.append(
            asyncio.create_task(calculate_zp(employee, random.randint(1, 5)))
        )

    await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(main())

print(f"Время выполнения: {time.time() - start_time}")