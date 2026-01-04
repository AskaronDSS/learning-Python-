# Напишите функцию, которая 
# завершается случайным сбоем и 
# автоматически повторяет до 3 раз с задержками.


import asyncio
import random

# async def fail(n):
#     if random.random() < 0.7:
#         print(f"Attempt {n}: Failing...")
#         raise Exception("Random failure")
#     print(f"Attempt {n}: Succeeded!")
#     return "Success"

# async def retryable_task(max_retries=3, delay=1):
#     for attempt in range(1, max_retries + 1):
#         try:
#             result = await fail(attempt)
#             return result
#         except Exception as e:
#             print(f"Attempt {attempt} failed: {e}")
#             if attempt < max_retries:
#                 print(f"Retrying in {delay} seconds...")
#                 await asyncio.sleep(delay)
#             else:
#                 print("Max retries reached.")
#                 raise
# async def main():
#     try:
#         result = await retryable_task()
#         print(f"Final result: {result}")
#     except Exception as e:
#         print(f"Task ultimately failed: {e}")
# asyncio.run(main())

# Create your own 
# class that implements __await__ 
# and use it inside asyncio.

class MyAwait:
    def __init__(self, value, delay):
        self.value = value
        self.delay = delay
        
    def __await__(self):
        return self.sleep_cor().__await__()
    async def sleep_cor(self):
        await asyncio.sleep(self.delay)
        return self.value
async def main():
    print('START')
    res = await MyAwait('PY 11', 2)
    print(res)
    print('END')


asyncio.run(main())


    


