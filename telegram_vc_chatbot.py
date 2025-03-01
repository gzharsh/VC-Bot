import asyncio
import os
import speech_recognition as sr
from gtts import gTTS
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped

API_ID = 9470694
API_HASH = 8f9f93417aec3ccb7d961c39fb65e6c9
BOT_TOKEN = 7514054618:AAH1ZkFQ3PltgUia0mX8TG9bbL2elJh--WE

app = Client("vc_chatbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call = PyTgCalls(app)

active_calls = {}

# 🎤 Speech-to-Text Function
def recognize_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="hi-IN")  # Hindi Support
        return text
    except sr.UnknownValueError:
        return "Mujhe samajh nahi aaya!"
    except sr.RequestError:
        return "Speech Recognition Error!"

# 🔊 Text-to-Speech Function
def text_to_speech(text):
    tts = gTTS(text=text, lang="hi")
    tts.save("response.mp3")

@app.on_message(filters.command("join"))
async def join_vc(client, message):
    chat_id = message.chat.id

    if chat_id in active_calls:
        await message.reply_text("✅ Bot already in Voice Chat!")
        return

    await call.join_group_call(chat_id, AudioPiped("response.mp3"))
    active_calls[chat_id] = True
    await message.reply_text("🔊 Bot joined Voice Chat!")

@app.on_message(filters.command("leave"))
async def leave_vc(client, message):
    chat_id = message.chat.id

    if chat_id not in active_calls:
        await message.reply_text("❌ Bot is not in Voice Chat!")
        return

    await call.leave_group_call(chat_id)
    del active_calls[chat_id]
    await message.reply_text("🚪 Bot left Voice Chat!")

@app.on_message(filters.command("speak"))
async def speak_message(client, message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        await message.reply_text("❌ Usage: /speak [message]")
        return

    text = " ".join(message.command[1:])
    text_to_speech(text)
    
    await call.join_group_call(chat_id, AudioPiped("response.mp3"))
    await message.reply_text("🗣️ Bot Speaking!")

@app.on_message(filters.command("listen"))
async def listen_audio(client, message):
    chat_id = message.chat.id

    if "voice" not in message:
        await message.reply_text("❌ Please send a voice message!")
        return

    voice = message.voice
    file_path = await client.download_media(voice)
    
    recognized_text = recognize_audio(file_path)
    await message.reply_text(f"🎤 You said: {recognized_text}")

    text_to_speech(f"Tune bola: {recognized_text}")
    await call.join_group_call(chat_id, AudioPiped("response.mp3"))
    await message.reply_text("🔊 Bot Responded!")

async def main():
    await app.start()
    print("🤖 Telegram Voice Chat Bot Started!")
    await asyncio.get_event_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())
