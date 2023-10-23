# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @imnot_avanish
#     MY ALL BOTS :- BrokenAssociation 
#     GITHUB :- KingEvil55 ""

from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from Alone import AloneX as pbot

AloneXX = "https://graph.org/file/59454c2dbad2cb44fc690.jpg"


@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=AloneXX,
        caption=f"""✨ **ʜᴇʏ {message.from_user.mention},**

**ᴏᴡɴᴇʀ  : [𝙸𝚖𝙽𝚘𝚝 ⁪⁬⁮⁮⁮⁮‌𝑬𝒓𝒆𝒏 𝒀𝒆𝒂𝒈𝒆𝒓😵😵‍](https://t.me/imnot_avanish)**
**ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{y()}`
**ʟɪʙʀᴀʀʏ ᴠᴇʀꜱɪᴏɴ :** `{o}`
**ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{s}`
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ :** `{z}`
** ᴇɴᴊᴏʏ**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗕ʀᴏᴋᴇɴ Mᴜsɪᴄ", url="https:t.me/BrokenXMusic"
                    ),
                    InlineKeyboardButton(
                        "𝗕ʀᴏᴋᴇɴ Rᴏʙᴏᴛ", url="https://t.me/BrokenXRoBot"
                    ),
                ]
            ]
        ),
    )
