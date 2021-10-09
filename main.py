import asyncio
from pyrogram import Client, filters
from pyrogram.errors import QueryIdInvalid, FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent

from configs import Config

Quotee_Robot = Client(session_name=Config.SESSION_NAME, api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)
DEFAULT_SEARCH_MARKUP = [
                    [InlineKeyboardButton("privacy policy 🍀", url="https://telegra.ph/Quotee-Robot-Privacy-Policy-10-09")],
                    [InlineKeyboardButton("Support 🩹", url="https://t.me/senuinfinitygroup")],
                    [InlineKeyboardButton("👨‍💻Updates channel ", url="https://t.me/senuinfinity")]
                ]


@Quotee_Robot.on_message(filters.command("start"))
async def start_handler(_, message: Message):
    try:
        await message.reply_sticker("CAACAgUAAxkBAAIDFmFhoElBHoMtp19rgK-wckP3nQXwAAIzBAACqsGQVmP_dWUaSa51HgQ")
        await message.reply_text(
            text="😋Hello, Welcome! to @Quotee_Robot. ⁇\n"
                 "ZQuoteeBot is available to create quotes that can be easily used anywhere.\n\n"
                 "from here, all the text you provide will be created as a quote. \n\nBy using our service you must agree to our privacy policy",
            disable_web_page_preview=True,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(DEFAULT_SEARCH_MARKUP)
        )
    except FloodWait as e:
        print(f"[{Config.SESSION_NAME}] - Sleeping for {e.x}s")
        await asyncio.sleep(e.x)
        await start_handler(_, message)

Quotee_Robot.run()
        
