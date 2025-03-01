from pyrogram import Client, filters
import config
import os
import yt_dlp
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment

# Bot Setup
bot = Client(
    "AdvancedBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# ✅ /start command
@bot.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("Hello! I'm your Advanced Bot 🚀")

# ✅ Download YouTube Video
@bot.on_message(filters.command("yt"))
def youtube_download(client, message):
    url = message.text.split(" ", 1)[-1]
    message.reply_text(f"Downloading video from: {url}...")

    ydl_opts = {"format": "best"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    message.reply_video(video=filename, caption="Here is your video! 🎥")

# ✅ Speech to Text (Audio Recognition)
@bot.on_message(filters.voice)
def recognize_speech(client, message):
    message.reply_text("Processing voice message... 🎤")

    file_path = message.download()
    audio = AudioSegment.from_file(file_path)
    audio.export("converted.wav", format="wav")

    recognizer = sr.Recognizer()
    with sr.AudioFile("converted.wav") as source:
        audio_data = recognizer.record(source)

    text = recognizer.recognize_google(audio_data)
    message.reply_text(f"Recognized Text: {text}")

# ✅ Text to Speech (TTS)
@bot.on_message(filters.command("say"))
def text_to_speech(client, message):
    text = message.text.split(" ", 1)[-1]
    tts = gTTS(text=text, lang="en")
    tts.save("tts.mp3")

    message.reply_voice("tts.mp3", caption="Here is your audio! 🔊")

# ✅ Run the bot
bot.run()
