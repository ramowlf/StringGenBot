from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="𝑠𝑒𝑠𝑠𝑖𝑜𝑛 𝑜𝑙𝑢𝑠̧𝑡𝑢𝑟", callback_data="gensession")],
        [
            InlineKeyboardButton(text="s𝑢𝑝𝑝𝑜𝑟𝑡", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="𝐾𝑎𝑛𝑎𝑙", url="https://t.me/BotAltyapi"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="𝑏𝑒𝑘𝑙𝑒 𝑜𝑙𝑚𝑎𝑧𝑠𝑎 𝑡𝑒𝑘𝑟𝑎𝑟 𝑑𝑒𝑛𝑒", callback_data="gensession")]]
)
