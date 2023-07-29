

import asyncio

async def get_name():
    return 'Тимур'
async def hello():
    name = await get_name()
    print('hello, ' + name)

loop = asyncio.new_event_loop()
loop.run_until_complete(hello())



