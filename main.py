import time
import asyncio


async def main(name, time_prepare_1, time_protection_1, time_prepare_2, time_protection_2):
    print(f'{name} started the 1 task.')
    await asyncio.sleep(time_prepare_1 / 100)

    print(f'{name} started the 2 task.')
    await asyncio.sleep(time_prepare_2 / 100)

    print(f'{name} moved on to the defense of the 1 task.')
    await asyncio.sleep(time_protection_1 / 100)

    print(f'{name} completed the 1 task.')
    print(f'{name} moved on to the defense of the 2 task.')
    await asyncio.sleep(time_protection_2 / 100)
    print(f'{name} completed the 2 task.')


async def interviews_2(*args):
    tasks = [
        asyncio.create_task(main(*i))
        for i in args
    ]
    await asyncio.gather(*tasks)


data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
t0 = time.time()
asyncio.run(interviews_2(*data))
print(time.time() - t0)
