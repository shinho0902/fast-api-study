# 동시성(Concurrency)과 async / await

# 비동기 : 기능1, 기능2, 기능3 이 있을때, 가장 느린 3 을 처리하는 동안 1,2 등 다른 일을 처리함

async def get_burgers(number: int):
    # Do some asynchronous stuff to create the burgers
    burgers = number
    return burgers

# get_burgers(3)

# asyncio 이벤트 루프에서 실행
import asyncio
burgers = asyncio.run(get_burgers(3))
print(burgers)


