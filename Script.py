class script(object):

    START_TXT = """<blockquote><b>ʜᴇʏ {}, <i>{}</i></blockquote>
    
<blockquote>ɪ ᴀᴍ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴡɪᴛʜ ʟɪɴᴋ sʜᴏʀᴛᴇɴᴇʀ ʙᴏᴛ. ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴀꜱ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴡɪᴛʜ ʟɪɴᴋ sʜᴏʀᴛᴇɴᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ... ɪᴛ'ꜱ ᴇᴀꜱʏ ᴛᴏ ᴜꜱᴇ ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ᴍᴏᴠɪᴇꜱ ᴡɪᴛʜ ʏᴏᴜʀ ʟɪɴᴋ ꜱʜᴏʀᴛᴇɴᴇʀ... ♻️</blockquote>

<blockquote>👨🏻‍💻ᴅᴇᴠᴇʟᴏᴘᴇʀ - <a href=https://telegram.me/KING_WMP>Chethmina Kavishan</a></b></blockquote>"""

    MY_ABOUT_TXT = """<blockquote><b>🤖 ᴍʏ ɴᴀᴍᴇ: <a href=https://t.me/AutoFilterCK_Bot>Auto Filter Bot</a></blockquote>
<blockquote>👨🏻‍💻 𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕣: <a href=https://t.me/KING_WMP>Chethmina Kavishan</a></blockquote>
<blockquote>📡 𝕊𝕖𝕧𝕖𝕣: <a href=https://app.koyeb.com/>Koyeb</a></blockquote>
<blockquote>🗄 𝔻𝕒𝕥𝕒𝕓𝕒𝕤𝕖: <a href=https://www.mongodb.com>MongoDB</a></blockquote>
<blockquote>📝 𝕃𝕒𝕟𝕘𝕦𝕒𝕘𝕖: <a href=https://www.python.org>Python</a></blockquote>
<blockquote>📚 𝕃𝕚𝕓𝕣𝕒𝕣𝕪: <a href=https://pyrogram.org>Pyrogram</a></blockquote>
<blockquote>📢 𝕌𝕡𝕕𝕒𝕥𝕖𝕤: <a href=https://t.me/CK4U2>Click</a></b></blockquote>"""

    MY_OWNER_TXT = """<blockquote><b>👨🏻‍💻 ℕ𝕒𝕞𝕖: Chethmina Kavishan</blockquote>
<blockquote>🔎 𝕌𝕤𝕖𝕣𝕟𝕒𝕞𝕖: @KING_WMP</blockquote>
<blockquote>🔮 𝔸𝕓𝕠𝕦𝕥: @About_KingWMP</blockquote>
<blockquote>🔑 𝕀𝔻: <code>5042338756</code></blockquote>
<blockquote>🌍 ℂ𝕠𝕦𝕟𝕥𝕣𝕪: Sri Lanka🇱🇰</b></blockquote>"""

    STATUS_TXT = """<blockquote>🗂 𝕋𝕠𝕥𝕒𝕝 𝔽𝕚𝕝𝕖𝕤: <code>{}</code></blockquote>
<blockquote>👤 𝕋𝕠𝕥𝕒𝕝 𝕌𝕤𝕖𝕣𝕤: <code>{}</code></blockquote>
<blockquote>👥 𝕋𝕠𝕥𝕒𝕝 ℂ𝕙𝕒𝕥𝕤: <code>{}</code></blockquote>
<blockquote>🤑 ℙ𝕣𝕖𝕞𝕚𝕦𝕞 𝕌𝕤𝕖𝕣𝕤: <code>{}</code></blockquote>
<blockquote>✨ 𝕌𝕤𝕖𝕕 𝕊𝕥𝕠𝕣𝕒𝕘𝕖: <code>{}</code></blockquote>
<blockquote>🗳 𝔽𝕣𝕖𝕖 𝕊𝕥𝕠𝕣𝕒𝕘𝕖: <code>{}</code></blockquote>
<blockquote>🚀 𝔹𝕠𝕥 𝕌𝕡𝕥𝕚𝕞𝕖: <code>{}</code></blockquote>"""

    NEW_GROUP_TXT = """#NewGroup
Title - {}
ID - <code>{}</code>
Username - {}
Total - <code>{}</code>"""

    NEW_USER_TXT = """#NewUser
★ Name: {}
★ ID: <code>{}</code>"""

    NOT_FILE_TXT = """👋 Hello {},

I can't find the <b>{}</b> in my database! 🥲

👉 Google Search and check your spelling is correct.
👉 Please read the Instructions to get better results.
👉 Or not been released yet.

📮 Send Your Requested Movie to <b><a href=https://telegram.me/RequestCK_Bot>this bot</a></b>"""
    
    EARN_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ꜰʀᴏᴍ ᴛʜɪs ʙᴏᴛ

➥ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴜsɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.

» sᴛᴇᴘ 1:- ғɪʀsᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ.

» sᴛᴇᴘ 2:- ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ <a href=https://telegram.me/how_to_download_channel/14>mdisklink.link</a> [ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴏᴛʜᴇʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ]

» sᴛᴇᴘ 3:- ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

➥ ᴛʜɪꜱ ʙᴏᴛ ɪs ꜰʀᴇᴇ ꜰᴏʀ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғᴏʀ ꜰʀᴇᴇ ᴏꜰ ᴄᴏꜱᴛ.</b>"""

    HOW_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ‼️

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ᴛʜᴇɴ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴇᴛᴀɪʟs ɪɴ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

➥ ғᴏʀᴍᴀᴛ ↓↓↓

<code>/set_shortlink sʜᴏʀᴛɴᴇʀ sɪᴛᴇ sʜᴏʀᴛɴᴇʀ ᴀᴘɪ</code>

➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓

<code>/set_shortlink mdisklink.link 5843c3cc645f5077b2200a2c77e0344879880b3e</code>

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ /get_shortlink

📝 ɴᴏᴛᴇ:- ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b>"""

    IMDB_TEMPLATE = """<blockquote>✅ 𝕀 𝔽𝕠𝕦𝕟𝕕: <code>{query}</code></blockquote>

<blockquote>🏷 𝕋𝕚𝕥𝕝𝕖: <b><a href={url}>{title}</a></b>
🎭 𝔾𝕖𝕟𝕣𝕖𝕤: <b>{genres}</b>
📆 𝕐𝕖𝕒𝕣: <b><a href={url}/releaseinfo>{year}</a></b>
🌟 ℝ𝕒𝕥𝕚𝕟𝕘: <b><a href={url}/ratings>{rating} / 10</a></b>
🔊 𝕃𝕒𝕟𝕘𝕦𝕒𝕘𝕖𝕤: <b>{languages}</b>
⏰ ℝ𝕦𝕟𝕋𝕚𝕞𝕖: <b>{runtime} Minutes</b></blockquote>

<blockquote>🙋🏻‍♂ ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝔹𝕐: {message.from_user.mention}</blockquote>
<blockquote>𝔾𝕣𝕠𝕦𝕡 ℕ𝕒𝕞𝕖: <b>{message.chat.title}</b></blockquote>

<blockquote>⚡ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕐: <a href=https://telegram.me/CK4U2>CK4U2</a></b></blockquote>"""

    FILE_CAPTION = """<blockquote><b>🎞ℕ𝕒𝕞𝕖:</b> <code>{file_name}</code></blockquote>
<blockquote><b>📥𝕊𝕚𝕫𝕖: {file_size}</b></blockquote>

<blockquote>⚡ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕐: <a href=https://telegram.me/CK4U2>CK4U2</a></b></blockquote>"""

    WELCOME_TEXT = """👋 Hello {mention}, Welcome to {title} group! 💞"""

    HELP_TXT = """<b>Note - <spoiler>Try each command without any argument to see more details 😹</spoiler></b>"""
    
    ADMIN_COMMAND_TXT = """<b>Here is bot admin commands 👇

/index_channels - to check how many index channel id added
/stats - to get bot status
/delete - to delete files using query
/delete_all - to delete all indexed file
/broadcast - to send message to all bot users
/grp_broadcast - to send message to all groups
/pin_broadcast - to send message as pin to all bot users.
/pin_grp_broadcast - to send message as pin to all groups.
/restart - to restart bot
/leave - to leave your bot from particular group
/unban_grp - to enable group
/ban_grp - to disable group
/ban_user - to ban a users from bot
/unban_user - to unban a users from bot
/users - to get all users details
/chats - to get all groups
/invite_link - to generate invite link
/set_pm_search - to do pm search on/off
/index - to index bot accessible channels</b>"""
    
    USER_COMMAND_TXT = """<b>Here is bot user commands 👇

/start - to check bot alive or not
/settings - to change group settings as your wish
/set_shortlink - group admin can set custom shortlink
/get_custom_settings - to get your group settings details
/set_welcome - to set custom new joined users welcome message for group
/set_tutorial - to set custom tutorial link in result page button
/id - to check group or channel id</b>"""
    
    SOURCE_TXT = """<blockquote><b>🔮𝕊𝕠𝕦𝕣𝕔𝕖 ℂ𝕠𝕕𝕖- <a href=https://t.me/+VhJIV2F3RxljNTNl>Click Here</a></blockquote>

<blockquote>👨🏻‍💻𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕣 - <a href=https://telegram.me/KING_WMP>Chethmina Kavishan</a></blockquote>
<blockquote>⚡ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕐 - <a href=https://telegram.me/CK4U2>CK4U2</a></b></blockquote>"""

    PREMIUM_PLAN_TEXT = """<b><i><u>- ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs - </u>

- 30ʀs - 1 ᴡᴇᴇᴋ
- 50ʀs - 1 ᴍᴏɴᴛʜs
- 120ʀs - 3 ᴍᴏɴᴛʜs
- 220ʀs - 6 ᴍᴏɴᴛʜs

<u>🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁</u>

○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ
○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs                                                                         
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ   

✨ ᴜᴘɪ ɪᴅ - <code>{}</code>

ᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan

💢 ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ

‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ</i></b>"""

