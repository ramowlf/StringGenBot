from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"𝑀𝑒𝑟ℎ𝑎𝑏𝑎 {message.from_user.first_name},\n\n๏ 𝑏𝑢 𝑏𝑜𝑡 {Anony.mention},\n𝑇𝑒𝑙𝑒𝑔𝑟𝑎𝑚 𝑆𝑡𝑟𝑖𝑛𝑔 𝑠𝑒𝑠𝑠𝑖𝑜𝑛 𝑜𝑙𝑢𝑠̧𝑡𝑢𝑟𝑚𝑎 𝑏𝑜𝑡𝑢𝑑𝑢𝑟.",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
