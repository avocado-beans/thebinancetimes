from telethon import TelegramClient, events
from datetime import datetime
from fastapi import FastAPI
import threading
import uvicorn
import asyncio
import time
import cmc
import os

api_id=os.environ['ID']
api_hash=os.environ['HASH']
cmc_key=os.environ['CMC_KEY']

announcement_source='t.me/BWEnews'
record='t.me/thebinancetimes'

app = FastAPI()
@app.get("/")
async def confirm():
    return """My process is purely logistical, narrowly focused by design."""
def mask():
    uvicorn.run(app)

async def IncomingMessageListener(event):
    message = event.message.message + f"\n\nTime: {datetime.now()}"
    print(message)
    await client.send_message(entity=record,message=message)
    if 'Binance' in message:
        try:
            symbol = message.split('(')[1].split(')')[0]
            message = cmc.cmc_stats(symbol, cmc_key) + f"\n\nTime: {datetime.now()}"
        except:
            message = "Not a listing announcement/not a new token."
        print(message)
        await client.send_message(entity=record,message=message)
async def con():
    await client.connect()
    print("Connected")
    try:
        await client.run_until_disconnected()
    except:
        pass
async def discon(timer):
    await asyncio.sleep(timer)
    print("Disconnected")
    await client.disconnect()
async def parallel(timer):
    await asyncio.gather(con(), discon(timer))
    print("Killed")

url_mask = threading.Thread(target=mask)
url_mask.start()

while True:
    client = TelegramClient('anon', api_id, api_hash,)
    client.add_event_handler(IncomingMessageListener, events.NewMessage(chats=announcement_source,incoming=True))
    with client:
        client.loop.run_until_complete(parallel(600))
