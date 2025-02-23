import asyncio


def generator():
    for i in range(3):
        yield i
        print(11111)



async def hello():
    print("hello")
    await asyncio.sleep(2)
    print('world')


async def main():
    task1 = asyncio.create_task(hello())
    task2 = asyncio.create_task(hello())
    task3 = asyncio.create_task(hello())
    task4 = asyncio.create_task(hello())
    task5 = asyncio.create_task(hello())
    task6 = asyncio.create_task(hello())
    task7 = asyncio.create_task(hello())

