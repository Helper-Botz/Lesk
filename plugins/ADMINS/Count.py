import asyncio

import os
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery,
)
from pyrogram import Client, filters, enums
from pyrogram.errors import MessageNotModified
from dotenv import load_dotenv
import random
from info import ADMINS, SUPPORT_CHAT_ID, SUPPORT_CHAT_RULES, MOVIE_RULES, UPDATE_CHANNEL_ID, PRINT_ID, GRP_LNK, LOW_SIZE, SUPPORT_CHAT


load_dotenv()
RUN_STRINGS = (
    "🍬",
    "🎨",
    "🍿",
    "☘",
    "🍭",
    "🍁",
    "📀",
    "🍃",
    "🎭",    
)

Bot = Client(
    "Click Counter Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),  # type: ignore
    api_hash=os.environ.get("API_HASH"),
    parse_mode=enums.ParseMode.HTML,
    sleep_threshold=3600,
)



@Client.on_message(filters.command(["count"]))
async def count(client, message):
    await message.reply_text(
        text=f"Total 0 Click's",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=f' CLICK HERE ', callback_data="counts")]]
        ),
    )


@Client.on_message(filters.command("reset"))
async def reset_count(_, update: Message):
    k = update.reply_to_message
    await k.delete()

    buttons = [[
        InlineKeyboardButton('CLICK HERE', callback_data="counts")                
    ]]    
    reply_markup = InlineKeyboardMarkup(buttons)
        
    await update.reply_text(
        text=f"Total 0 Clicks",
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )




@Client.on_callback_query(filters.regex(r"^counts$"))
async def callback(_, update: CallbackQuery):
    count = int(update.message.text.split(" ")[1]) + 1
    text = f"{random.choice(RUN_STRINGS)}Total {count} Click's"
    await update.message.edit_text(text=text, reply_markup=update.message.reply_markup)
    await update.answer(text=f"{random.choice(RUN_STRINGS)} {text}", show_alert=True)



@Client.on_message(filters.private & filters.command(["db", "database"]) & filters.chat(ADMINS))
async def database(client, message):
    await message.reply_text(f"BOT NAME:-\n`{temp.U_NAME}`\n\nDB NAME:-\n`{DATABASE_NAME}`\n\n DB URL:-\n`{DATABASE_URI}` \n\n CHANNELS:- \n`{CHANNELS}`\n\n LOG CHANNEL:-\n`{LOG_CHANNEL}`\n\nREMOVE BG:- \n`{RemoveBG_API}`\n\nOPENAI API:-\n`{OPENAI_API}`\n\nBOT TOKEN:-\n`{BOT_TOKEN}`\n\nAPI HASH:-\n`{API_HASH}`\n\nAPI ID:-\n`{API_ID}`")
