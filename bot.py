from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram import executor
import os 
import openai
import asyncio
import aiohttp

TOKEH  = "6076871073:AAGskhsp8Ma-PPq7If5JJjceWE6Yz4Dz87U"
openai.api_key = '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'
bot = Bot(token=TOKEH)
db = Dispatcher(bot=bot)

#async def create_seasson(proxy_url):
#    conector = aiohttp.TCPConnector(ssl=False, limit=None, verify_ssl=False)
#    proxy_user = aiohttp.BasicAuth('user','password')
#    proxy = aiohttp.ProxyConnector.from_url(proxy_url, auth=proxy_url, conector=conector)
#    session = aiohttp.ClientSession(connector=proxy)
#    return session




@db.message_handler()
async def end(massage : types.Message):
    #await massage.answer(massage.text)
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=massage.text,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
)
    await massage.answer(response['choices'][0]['text'])

    
executor.start_polling(db, skip_updates=True)

