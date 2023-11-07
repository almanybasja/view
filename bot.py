import os
from config import Config 
import telebot
import re
import requests

API_TOKEN = '6943535165:AAEPery-VNC5Lsk0atc2cBwNQv2UMnmeDRk'
bot = telebot.TeleBot(API_TOKEN)

admin = 6509622797

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "مرحبا بك عزيزي في بوت رشق المشاهدات المجاني\n"
                             "ارسل الرابط التيليكرام لطلب 1000 مشاهده مجانيه", parse_mode="Markdown")

@bot.message_handler(func=lambda message: re.search(r't\.me', message.text))
def send_views(message):
    chat_id = message.chat.id
    link = message.text
    response = send_request(link)
    
    if response:
        bot.send_message(chat_id, f"تم الارسال المشاهدات للرابط: {link}", )
    else:
        bot.send_message(chat_id, "فشل الارسال، حاول مجددا بعد قليل", parse_mode="Markdown")
        bot.send_message(admin, "عزيزي ادمن البوت:\nهنالك مشاكل في الاتصالات والطلبات تتم رفضها.\n"
                                       "اغلب الاسباب:\n- تم حظر حسابك في الموقع بسبب انتهاكيات الاستخدام\n"
                                       "- ان API_KEY_SITE غلط",)

@bot.message_handler(func=lambda message: not re.search(r't\.me', message.text))
def invalid_link(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "يرجى إرسال الرابط بشكل صحيح!\n\nمثال:\n[https://t.me/UI_XB/3560]",)

def send_request(link):
    response = requests.get(f"https://smm-speed.com/api/v2?action=add&service=2666&link={link}&quantity=1000&key=1ccfd5366337d76a4c56df9c60203358")
    data = response.json()
    return data.get('order', False)

if __name__ == '__main__':
    bot.polling(none_stop=True)
