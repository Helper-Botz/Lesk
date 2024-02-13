import os 
import pyrogram
from pyrogram import Client, filters
from info import ADMINS, SUPPORT_CHAT_ID, ADMINS





@Client.on_message(filters.group & filters.regex(r'https?://[^\s]+'))                                  
async def nolink(bot,message):
        if message.chat.id != SUPPORT_CHAT_ID:
                try:
                        await message.delete()
                except:
                        return


