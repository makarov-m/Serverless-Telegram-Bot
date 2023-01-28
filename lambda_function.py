import os
import telebot
import json
import random

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        message_chat_id = data['message']['chat']['id']
        message_first_name = data['message']['chat']['first_name']
        message_username = data['message']['chat']['username']
        message_text = data['message']['text']
        
        if '/start' in message_text or '/help' in message_text:
            msg_reply = f''' Привет {message_first_name}, чем я могу тебе помочь?\nСопровождением пассажиров корабле занимается @..., по всем техническим вопросам прошу обращаться к моему старпому @... . '''
            bot.send_message(message_chat_id, msg_reply)
        elif '/fact' in message_text:
            with open("facts_Magellan.json", "r") as file:
                data = json.load(file)
            random_num = str(random.randint(0,len(data)))
            msg_reply = data[random_num]
            bot.send_message(message_chat_id, msg_reply)  
        else:
            bot.send_message(message_chat_id, "Хочешь поговорить о чем-то ещё? Нет у меня на это времени! Бросить в карцер этого трусливого, вонючего, как мои сапоги, предателя!")
    except:  
        print ("Smth went wrong")
