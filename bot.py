import asyncio
import os
import re
import time
import aiohttp
import requests
import aiofiles
from base64 import standard_b64encode, standard_b64decode
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


from config import Config

logging.getLogger("pyrogram").setLevel(logging.WARNING)
app = Client(
            "Bot",
            bot_token = Config.BOT_TOKEN,
            api_id = Config.API_ID,
            api_hash = Config.API_HASH)


    
test="AniwatchZone | Table of Contents.\n\nView the button for the complete set of the **Table of Contents.**"
repl_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Ani FAQ's",
                     url=f"https://t.me/c/1944303479/31491/32422",
                ),
                InlineKeyboardButton(
                    text="W2G FAQ's",
                    url="https://t.me/c/1944303479/31491/32524",
                ),
            ],
             [
                InlineKeyboardButton(
                    text="Rules",
                    url="https://t.me/c/1944303479/31491/32403",
                ),
                InlineKeyboardButton(
                    text="MangaR FAQ's",
                    url="https://t.me/c/1944303479/31491/32695",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="How to Ask Support",
                                url="https://t.me/c/1944303479/31491/32781",
                ),
                    
                InlineKeyboardButton(
                    text="Bugs & Suggestions",
                    url="https://t.me/c/1944303479/31491/32792",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="↻ Back to the top",
                                url="https://t.me/c/1944303479/31491/32398",              
                ),
            ],
        ],
    ) 
@app.on_message(filters.command("send"))
async def start(bot, cmd: Message):
    usr_cmd = cmd.text.split("_", 1)[-1]
    kay_id = -1001944303479
    rep_id = 31491
    if usr_cmd == "/start":
       await app.send_message(
                      chat_id=kay_id,
                      text=test,
                      reply_markup=repl_markup,
                      reply_to_message_id=rep_id
       ) 
    
          
    
app.start()
print("Powered by @animxt")
idle()
