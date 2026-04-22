from pyrogram import filters
from pyrogram.types import Message, ChatPermissions, ChatPrivileges

from AviaxMusic import app
from AviaxMusic.misc import SUDOERS
from AviaxMusic.utils.decorators.language import language


ban = ["ban", "boom"]
unban = ["unban"]
mute = ["mute", "silent", "shut"]
unmute = ["unmute", "speak", "free"]
kick = ["kick", "out", "nikaal", "nikal"]
promote = ["promote", "adminship"]
fullpromote = ["fullpromote", "fulladmin"]
demote = ["demote", "lelo"]


@app.on_message(filters.command(["ina", "inata"], prefixes=["h", "H"]) & SUDOERS)
@language()
async def restriction_app(_, m: Message):

    # ❗ check args
    if len(m.command) < 2:
        return await m.reply_text("Usage: reply + action")

    # ❗ must reply
    if not m.reply_to_message:
        return await m.reply_text("Reply to a user.")

    chat_id = m.chat.id
    user_id = m.reply_to_message.from_user.id
    action = m.command[1].lower()

    # 🚫 protect sudo users
    if user_id in SUDOERS:
        return await m.reply_text("Cannot restrict sudo users.")

    try:
        if action in ban:
            await app.ban_chat_member(chat_id, user_id)
            await m.reply_text("✅ User banned.")

        elif action in unban:
            await app.unban_chat_member(chat_id, user_id)
            await m.reply_text("✅ User unbanned.")

        elif action in kick:
            await app.ban_chat_member(chat_id, user_id)
            await app.unban_chat_member(chat_id, user_id)
            await m.reply_text("✅ User kicked.")

        elif action in mute:
            await m.chat.restrict_member(
                user_id,
                ChatPermissions(can_send_messages=False)
            )
            await m.reply_text("🔇 User muted.")

        elif action in unmute:
            await m.chat.restrict_member(
                user_id,
                ChatPermissions(can_send_messages=True)
            )
            await m.reply_text("🔊 User unmuted.")

        elif action in promote:
            await app.promote_chat_member(
                chat_id,
                user_id,
                privileges=ChatPrivileges(
                    can_delete_messages=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                    can_manage_chat=True
                )
            )
            await m.reply_text("⭐ User promoted.")

        elif action in fullpromote:
            await app.promote_chat_member(
                chat_id,
                user_id,
                privileges=ChatPrivileges(
                    can_change_info=True,
                    can_delete_messages=True,
                    can_invite_users=True,
                    can_restrict_members=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                    can_manage_chat=True
                )
            )
            await m.reply_text("👑 User fully promoted.")

        elif action in demote:
            await app.promote_chat_member(
                chat_id,
                user_id,
                privileges=ChatPrivileges()
            )
            await m.reply_text("⬇️ User demoted.")

        else:
            await m.reply_text("❌ Unknown action.")

    except Exception as e:
        await m.reply_text(f"Error: {str(e)}")
