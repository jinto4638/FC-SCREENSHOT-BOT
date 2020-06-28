from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..config import Config
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(Filters.private & Filters.command("start"))
async def start(c, m):
    
    if not await c.db.is_user_exist(m.chat.id):
        await c.db.add_user(m.chat.id)
        await c.send_message(
            Config.LOG_CHANNEL,
            f"New User [{m.from_user.first_name}](tg://user?id={m.chat.id}) started."
        )
    
    await m.reply_text(
        text=f"𝔀𝓮𝓵𝓬𝓸𝓶𝓮/സ്വാഗതം/स्वागत हे {m.from_user.first_name}.\n\nI'm a simple Screenshot Generator Bot. I can provide screenshots from your video files with out downloading the entire file (almost instantly). \n i'm mainly working for @fcfilmcorner just do folllow for latest movies in any language . \n\nFor more details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Source Code', url='https://github.com/jinto4638/FC-SCREENSHOT-BOT'),
                    InlineKeyboardButton('follow', url='https://t.me/fcfilmcornercc')
                ],
            ]
        )
    )
