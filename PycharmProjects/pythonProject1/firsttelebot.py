import requests
import asyncio
token = '6393210025:AAFgflKYsQT8iH196edksHur23CPWYK3pzc'
URL = 'https://api.telegram.org/bot'

user_id = 5125276965
async def get_message():
    message = input('Ввидите ваше сообщение : ')
    await send_message(message)
async def send_message(message):
    message_data = {
        'chat_id': user_id,
        'text': message
    }
    requests.post(URL + token + '/sendMessage', data=message_data)
loop = asyncio.new_event_loop()
loop.run_until_complete(get_message())