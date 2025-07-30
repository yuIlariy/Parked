from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKENS, THUMBNAIL_URL, REDIRECT_USERNAME

bots = [Client(f"bot_{i}", bot_token=token) for i, token in enumerate(BOT_TOKENS)]

for bot in bots:
    @bot.on_message(filters.private & filters.command("start"))
    async def redirect(_, message):
        await message.reply_photo(
            photo=THUMBNAIL_URL,
            caption=(
                "👋 Hey there!\n\nI'm currently parked and not handling requests.\n"
                f"Please use 👉 @{REDIRECT_USERNAME} to rename your files with ease!"
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Go to Bot 🚀", url=f"https://t.me/{REDIRECT_USERNAME}")]
            ])
        )

    bot.start()

print("✅ All redirect bots are running.")


