#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [ZeinzoCheckerMember Telegram bot by TeLe TiPs] (https://github.com/teletips/DATE_TIME_USERBOT-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/ZeinzoCheckerMember

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import asyncio
from texts.zein import *

ZeinzoCheckerMember = Client(
    name = "ZeinzoCheckerMember",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)
CHANNEL_OR_GROUP_LIST = [i.strip() for i in os.environ.get("CHANNEL_OR_GROUP_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])

print(zein_1)
async def main_ZeinzoCheckerMember():
    async with ZeinzoCheckerMember:
        try:
            while True:
                print(zein_2)
                edit_message_text_teletips = "**📈 | Number of group members and channels zein has"
                for CHANNEL_OR_GROUP in CHANNEL_OR_GROUP_LIST:
                    try:
                        get_chat_zein = await ZeinzoCheckerMember.get_chat(int(CHANNEL_OR_GROUP))   
                        if get_chat_zein.type == "channel":
                            edit_message_text_teletips += f"\n\n📣  **{get_chat_zein.title}**\n👤 ├ <i>{get_chat_zein.members_count} Subscribers</i>\n🔗 └ <i>[Link]({get_chat_zein.invite_link})</i>"
                        else:
                            edit_message_text_teletips += f"\n\n💬  **{get_chat_zein.title}**\n👤 ├ <i>{get_chat_zein.members_count} Members</i>\n🔗 └ <i>[Link]({get_chat_zein.invite_link})</i>" 
                        await asyncio.sleep(2)
                    except ValueError:
                        print(f'ID not found: {CHANNEL_OR_GROUP }. Skipping...')                       
                edit_message_text_teletips += f"\n\n<i>Automatically refreshes every 15 minutes</i>"
                try:
                    await ZeinzoCheckerMember.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, edit_message_text_teletips, disable_web_page_preview=True)
                except Exception:
                    pass    
                print(zein_3)              
                await asyncio.sleep(900) # 15 minutes = 900 seconds
        except FloodWait as e:
            await asyncio.sleep(e.x)

@ZeinzoCheckerMember.on_message(filters.command("status", "!") & filters.me)
async def alive(_, message: Message):
    await message.edit("Your MemberCounter is alive!")
    await asyncio.sleep(10)
    await message.delete()                   
                        
ZeinzoCheckerMember.run(main_ZeinzoCheckerMember())

#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
