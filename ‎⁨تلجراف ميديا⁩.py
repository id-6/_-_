from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep
from telegraph import upload_file
import os
app=Client(
    "topac_mustafa",
    api_id = 18421930,#ايبي ايدي
    api_hash = "9cf3a6feb6dfcc7c02c69eb2c286830e",#ايبي هاش
    bot_token = '6590737463:AAEGgq8aPyjoOdKMcXHX-v6Ux8KMpShyvKM'#توكن بوتك
)

@app.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f""" - هلا {message.from_user.mention}
ـ================
بوت تحويل ميديا لرابط مباشر

الصيغ المدعومه : jpeg - png - jpg - mp4 - gif
ـ================
ـ BY- [ TOPAC](https://t.me/iiit5)"""
    await app.send_message(message.chat.id, text, disable_web_page_preview=True)
    

@app.on_message(filters.media & filters.private)
async def glink(client, message):
    try:
        text = await app.send_video(message.chat.id, video="https://telegra.ph/file/837353d8c05588243a5bc.mp4", caption='معليك بل متحركه 😂\n جار المعالجه')
        async def progress(current, total):
            await text.edit_text(f"📥 جار التحميل... {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            lo = await message.download(location, progress=progress)
            await text.edit_text("📤 جار الرفع ...")
            up = upload_file(lo) 
            await text.edit_text(f"**🌐 | رابط تليجراف **:\n\n<code>https://telegra.ph{up[0]}</code>")     
            os.remove(lo) 
        except Exception as e:
            await text.edit_text(f"**❌ | حدث خطأ **\n\n<i>**السبب**: {e}</i>")
            os.remove(lo) 
            return                 
    except Exception:
        pass        
                      
print('')
sleep(2)
print("   تم التشغيل")
app.run()
