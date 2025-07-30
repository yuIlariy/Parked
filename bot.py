from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKENS, THUMBNAIL_URL, REDIRECT_USERNAME, API_ID, API_HASH
import asyncio

SECONDARY_USERNAME = "AutoRenameTBot"

bots = [
    Client(
        f"bot_{i}",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=token
    )
    for i, token in enumerate(BOT_TOKENS)
]

for bot in bots:
    @bot.on_message(filters.private & filters.command("start"))
    async def redirect(_, message):
        await message.reply_photo(
            photo=THUMBNAIL_URL,
            caption=(
                "👋 Hey there!\n\nI'm currently parked and not handling requests.\n"
                f"Need file renaming? You’ve got **two powerful options**:\n\n"
                f"• 📁 [@{REDIRECT_USERNAME}](https://t.me/{REDIRECT_USERNAME})\n"
                f"• 👻 [@{SECONDARY_USERNAME}](https://t.me/{SECONDARY_USERNAME})\n\n"
                "Pick your flavor and rename away!"
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Go to Bot🚀", url=f"https://t.me/{REDIRECT_USERNAME}")],
                [InlineKeyboardButton("👻 Auto Rename?", url=f"https://t.me/{SECONDARY_USERNAME}")]
            ])
        )

    bot.start()

print("✅ All redirect bots are running.")

# Keep alive so bots don’t exit
asyncio.get_event_loop().run_forever()

