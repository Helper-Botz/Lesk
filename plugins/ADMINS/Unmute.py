from datetime import datetime, timedelta
from time import time
import asyncio
from utils import temp
from pyrogram.enums import ChatMemberStatus, ChatType
from pyrogram.types import Message
from pyrogram.enums import MessageEntityType
from pyrogram import Client, filters
from info import SUPPORT_CHAT_ID, ADMINS
from datetime import datetime, timedelta
from pyrogram.types import ChatPermissions
import os 
import pyrogram
from info import ADMINS, SUPPORT_CHAT_ID, SUPPORT_CHAT_RULES, MOVIE_RULES, UPDATE_CHANNEL_ID, PRINT_ID, GRP_LNK, LOW_SIZE, SUPPORT_CHAT

@Client.on_message(filters.group  & filters.regex("@") | filters.regex("/settings@KOCHU_KALLAN_RoBOT") | filters.regex("/settings@KOCHU_KALLAN_RoBOT") | filters.regex("/settings@MINNAL_MURALI_ROBOT") | filters.regex("/settings@NASRANI_ROBOT") | filters.regex("/settings@KOCHU_KALLAN_RoBOT") | filters.regex("/start@KOCHU_KALLAN_RoBOT") | filters.regex("/start@MINNAL_MURALI_ROBOT") | filters.regex("/start@NASRANI_ROBOT") | filters.regex("r'https?://[^\s]+"))
async def nolinks(bot,message):
    if message.chat.id and message.from_user.id != SUPPORT_CHAT_ID and ADMINS:			                               
        user_id = message.from_user.id if message.from_user else None
        chat_id = message.chat.id
        try: 
            k=await message.reply_text(text=f"{message.from_user.mention} 𝐖𝐡𝐚𝐭 𝐘𝐨𝐮 𝐖𝐨𝐧'𝐭...??🤣")		
            await bot.restrict_chat_member(chat_id, user_id, ChatPermissions(),
            datetime.now() + timedelta(seconds=60)) #### timedelta(days=1))
            await message.delete()          
        except:
	        return
	        
	                
