import os
import asyncio
import sys
import git
import heroku3
# Changed root to DOLLSPAM
from DollXSpamBot import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9
from DollXSpamBot import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, deadlyversion
from DollXSpamBot import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
# alive Pic By Default It's Will Show Our
from DollXSpamBot import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

DOLL_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/f8d63b1dc5676fc9988f1.jpg"


DOLL = "✯ 𝙍𝙖𝙟𝙥𝙪𝙩 ✘ 𝙎𝙥𝙖𝙢 𝙃𝙀𝙍𝙀 ✯\n\n"
DOLL += f"**꧁🇮🇳 😈 𝐉𝐀𝐘 𝐒𝐇𝐑𝐄𝐄 𝐑𝐀𝐌 😈 🇮🇳꧂**\n"
DOLL += f"━───────╯•╰───────━\n"
DOLL += f"• **𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽** : `3.10.1`\n"
DOLL += f"• **𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽** : `{version.__version__}`\n"
DOLL += f"• **𝙳𝙾𝙻𝙻 𝚇 𝚂𝙿𝙰𝙼 𝙱𝙾𝚃 𝚅𝙴𝚁𝚂𝙸𝙾𝙽**  : `{deadlyversion}`\n"
DOLL += f"• **ᴄʜᴀɴɴᴇʟ** : [Join.](https://t.me/RajputChannels)\n"
DOLL += f"• **Source Code** : [•Repo•](https://github.com/Devilkingyt44/DollXSpamBot)\n"
DOLL += f"━───────╮•╭───────━\n\n"   
                                  
@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sdoll(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await BOT0.send_file(event.chat_id,
                                  DOLL_PIC,
                                  caption=DOLL,
                                  buttons=[
        [
        Button.url("☺️ᴄʜᴀɴɴᴇʟ☺️", "https://t.me/RajputChannels"),
        Button.url("🇮🇳sᴜᴘᴘᴏʀᴛ🇮🇳", "https://t.me/RajputChat")
        ],
        [
        Button.url("• 🙂ʀᴇᴘᴏ🙂 •", "https://github.com/Devilkingyt44/DollXSpamBot")
        ]
        ]
        )
