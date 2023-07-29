import requests
import asyncio

token = '6393210025:AAFgflKYsQT8iH196edksHur23CPWYK3pzc'
URL = 'https://api.telegram.org/bot'
async def collect_update():
    Request = requests.post(URL + token + '/getupdates').json()
    print(Request)
loop = asyncio.new_event_loop()
loop.run_until_complete(collect_update())
