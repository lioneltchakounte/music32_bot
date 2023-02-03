import telebot
from telebot import types
import requests

bot = telebot.TeleBot("6117113366:AAGtNGafMcvsw5UTApM85Gwic1Wa58E_Wxw")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm a music bot. Send me a song title and I'll try to download it for you!")


@bot.message_handler(func=lambda message: True)
def send_music(message):
    song_title = message.text
    api_url = "http://api.musixmatch.com/ws/1.1/track.search?apikey=Your API Key&q_track=" + song_title
    response = requests.get(api_url).json()
    track_id = response['message']['body']['track_list'][0]['track']['track_id']
    download_url = "http://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey=Your API Key&track_id=" + str(track_id)
    music = requests.get(download_url).json()
    music_file = music['message']['body']['lyrics']['music_file']
    bot.send_audio(message.chat.id, music_file)


bot.polling()
