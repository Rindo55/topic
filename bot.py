import asyncio
import re
from pyrogram import Client, filters, idle
from config import Config
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


from uvloop import install
from contextlib import closing, suppress
from pyrogram.types import Message, MessageEntity
from string import ascii_letters, ascii_uppercase, digits
from base64 import standard_b64encode, standard_b64decode
logging.getLogger("pyrogram").setLevel(logging.WARNING)
class app(Client):
   

    def __init__(self):
        super().__init__(

            session_name="Captioner",

            bot_token = Config.BOT_TOKEN,

            api_id = Config.API_ID,

            api_hash = Config.API_HASH,
            workers = 20,

            plugins = dict(

                root="Plugins"

            )

        )

           

   




def str_to_b64(__str: str) -> str:

    str_bytes = __str.encode('ascii')

    bytes_b64 = standard_b64encode(str_bytes)

    b64 = bytes_b64.decode('ascii')


    
    


if __name__ == "__main__":
    app().run()
