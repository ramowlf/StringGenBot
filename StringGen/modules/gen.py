import asyncio

from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout

from config import SUPPORT_CHAT
from StringGen import Anony
from StringGen.utils import retry_key


async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"ᴛᴇʟᴇᴛʜᴏɴ"
    elif old_pyro:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v1"
    else:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v2"

    await message.reply_text(f"» 𝑠𝑒𝑠𝑠𝑖𝑜𝑛 𝑜𝑙𝑢𝑠̧𝑡𝑢𝑟𝑚𝑎 {ty} 𝑏𝑎𝑠̧𝑙𝑎𝑡𝚤𝑙𝚤𝑦𝑜𝑟...")

    try:
        api_id = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» 𝐴𝑝𝑖 𝑖𝑑 𝑔𝑖𝑟 :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» 𝟻 𝑑𝑎𝑘𝑖𝑘𝑎𝑙ı𝑘 𝑠ü𝑟𝑒 𝑠ı𝑛ı𝑟ı𝑛𝑎 𝑢𝑙𝑎şı𝑙𝑑ı..\n\n𝐿ü𝑡𝑓𝑒𝑛 𝑜𝑡𝑢𝑟𝑢𝑚 𝑜𝑙𝑢ş𝑡𝑢𝑟𝑚𝑎𝑦ı 𝑡𝑒𝑘𝑟𝑎𝑟 𝑏𝑎ş𝑙𝑎𝑡ı𝑛.",
            reply_markup=retry_key,
        )

    if await cancelled(api_id):
        return

    try:
        api_id = int(api_id.text)
    except ValueError:
        return await Anony.send_message(
            user_id,
            "» 𝐺ö𝑛𝑑𝑒𝑟𝑑𝑖ğ𝑖𝑛𝑖𝑧 𝐴𝑃𝐼 𝐼𝐷 𝑔𝑒ç𝑒𝑟𝑠𝑖𝑧..\n\n𝐿ü𝑡𝑓𝑒𝑛 𝑜𝑡𝑢𝑟𝑢𝑚 𝑜𝑙𝑢ş𝑡𝑢𝑟𝑚𝑎𝑦ı 𝑡𝑒𝑘𝑟𝑎𝑟 𝑏𝑎ş𝑙𝑎𝑡ı𝑛..",
            reply_markup=retry_key,
        )

    try:
        api_hash = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» 𝐴𝑝𝑖 𝐻𝑎𝑠ℎ 𝐺𝑖𝑟 :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» 𝟻 𝑑𝑎𝑘𝑖𝑘𝑎𝑙ı𝑘 𝑠ü𝑟𝑒 𝑠ı𝑛ı𝑟ı𝑛𝑎 𝑢𝑙𝑎şı𝑙𝑑ı..\n\n𝐿ü𝑡𝑓𝑒𝑛 𝑜𝑡𝑢𝑟𝑢𝑚 𝑜𝑙𝑢ş𝑡𝑢𝑟𝑚𝑎𝑦ı 𝑡𝑒𝑘𝑟𝑎𝑟 𝑏𝑎ş𝑙𝑎𝑡ı𝑛.",
            reply_markup=retry_key,
        )

    if await cancelled(api_hash):
        return

    api_hash = api_hash.text

    if len(api_hash) < 30:
        return await Anony.send_message(
            user_id,
            "» 𝐺ö𝑛𝑑𝑒𝑟𝑑𝑖ğ𝑖𝑛𝑖𝑧 𝐴𝑃𝐼 𝐻𝐴𝑆𝐻 𝑔𝑒ç𝑒𝑟𝑠𝑖𝑧..\n\n𝐿ü𝑡𝑓𝑒𝑛 𝑜𝑡𝑢𝑟𝑢𝑚 𝑜𝑙𝑢ş𝑡𝑢𝑟𝑚𝑎𝑦ı 𝑡𝑒𝑘𝑟𝑎𝑟 𝑏𝑎ş𝑙𝑎𝑡ı𝑛..",
            reply_markup=retry_key,
        )

    try:
        phone_number = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» 𝑇𝐸𝐿𝐸𝐹𝑂𝑁 𝑁𝑈𝑀𝐴𝑅𝐴𝑁𝐼 𝐺𝐼̇𝑅 :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» 𝟻 𝑑𝑎𝑘𝑖𝑘𝑎𝑙ı𝑘 𝑠ü𝑟𝑒 𝑠ı𝑛ı𝑟ı𝑛𝑎 𝑢𝑙𝑎şı𝑙𝑑ı..\n\n𝐿ü𝑡𝑓𝑒𝑛 𝑜𝑡𝑢𝑟𝑢𝑚 𝑜𝑙𝑢ş𝑡𝑢𝑟𝑚𝑎𝑦ı 𝑡𝑒𝑘𝑟𝑎𝑟 𝑏𝑎ş𝑙𝑎𝑡ı𝑛.",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    await Anony.send_message(user_id, "» 𝑁𝑢𝑚𝑎𝑟𝑎𝑦𝑎 𝑘𝑜𝑑 𝑔𝑜̈𝑛𝑑𝑒𝑟𝑖𝑙𝑖𝑦𝑜𝑟...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="Anony", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()

    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)

    except FloodWait as f:
        return await Anony.send_message(
            user_id,
            f"» 𝐺𝑖𝑟𝑖𝑠̧ 𝑖𝑐̧𝑖𝑛 𝑘𝑜𝑑 𝑔𝑜̈𝑛𝑑𝑒𝑟𝑚𝑒 𝑏𝑎𝑠̧𝑎𝑟𝚤𝑠𝚤𝑧 𝑜𝑙𝑑𝑢.\n\n𝐿𝑢̈𝑡𝑓𝑒𝑛 {f.value or f.x} 𝑠𝑎𝑛𝑖𝑦𝑒 𝑏𝑒𝑘𝑙𝑒𝑦𝑖𝑛.",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Anony.send_message(
            user_id,
            "» 𝐴𝑝𝑖 ℎ𝑎𝑠ℎ 𝑣𝑒𝑦𝑎 𝐴𝑝𝑖 𝑖𝑑 𝑦𝑎𝑛𝑙𝚤𝑠̧.\n\n𝑙𝑢̈𝑡𝑓𝑒𝑛 𝑡𝑒𝑘𝑟𝑎𝑟 𝑑𝑒𝑛𝑒𝑦𝑖𝑛.",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Anony.send_message(
            user_id,
            "» ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪɴᴠᴀʟɪᴅ.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )

    try:
        otp = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴛʜᴇ ᴏᴛᴘ sᴇɴᴛ ᴛᴏ {phone_number}.\n\nɪғ ᴏᴛᴩ ɪs <code>12345</code>, ᴩʟᴇᴀsᴇ sᴇɴᴅ ɪᴛ ᴀs <code>1 2 3 4 5.</code>",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 10 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )

    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await Anony.send_message(
            user_id,
            "» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs <b>ᴡʀᴏɴɢ.</b>\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Anony.send_message(
            user_id,
            "» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs <b>ᴇxᴩɪʀᴇᴅ.</b>\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Anony.ask(
                identifier=(message.chat.id, user_id, None),
                text="» ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴘᴀssᴡᴏʀᴅ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ :",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Anony.send_message(
                user_id,
                "» ᴛɪᴍᴇᴅ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
                reply_markup=retry_key,
            )

        if await cancelled(pwd):
            return
        pwd = pwd.text

        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await Anony.send_message(
                user_id,
                "» ᴛʜᴇ ᴩᴀssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await Anony.send_message(user_id, f"ᴇʀʀᴏʀ : <code>{str(ex)}</code>")

    try:
        txt = "ʜᴇʀᴇ ɪs ʏᴏᴜʀ {0} sᴛʀɪɴɢ sᴇssɪᴏɴ\n\n<code>{1}</code>\n\nᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ <a href={2}>ғᴀʟʟᴇɴ ᴀssᴏᴄɪᴀᴛɪᴏɴ</a>\n☠ <b>ɴᴏᴛᴇ :</b> ᴅᴏɴ'ᴛ sʜᴀʀᴇ ɪᴛ ᴡɪᴛʜ ʏᴏᴜʀ ɢɪʀʟғʀɪᴇɴᴅ."
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                link_preview=False,
                parse_mode="html",
            )
            await client(JoinChannelRequest("@FallenAssociation"))
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                disable_web_page_preview=True,
            )
            await client.join_chat("FallenAssociation")
    except KeyError:
        pass
    try:
        await client.disconnect()
        await Anony.send_message(
            chat_id=user_id,
            text=f"sᴜᴄᴄᴇssғᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʏᴏᴜʀ {ty} sᴛʀɪɴɢ sᴇssɪᴏɴ.\n\nᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs ғᴏʀ ɢᴇᴛᴛɪɴɢ ɪᴛ.\n\nᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ <a href={SUPPORT_CHAT}>ғᴀʟʟᴇɴ ᴀssᴏᴄɪᴀᴛɪᴏɴ</a>.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        pass


async def cancelled(message):
    if "/cancel" in message.text:
        await message.reply_text(
            "» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss.", reply_markup=retry_key
        )
        return True
    elif "/restart" in message.text:
        await message.reply_text(
            "» sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴛᴀʀᴛᴇᴅ ᴛʜɪs ʙᴏᴛ.", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss.", reply_markup=retry_key
        )
        return True
    else:
        return False
