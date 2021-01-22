import json

import telegram

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .myForm import MessageForm 
from .models import Message

from django.conf import settings

TOKEN = settings.TELEGRAM_TOKEN

global bot
bot = telegram.Bot(token=TOKEN)

@csrf_exempt
def telBot(request):

    if request.method == "POST":
        print(json.loads(request.body))
        tele_data = json.loads(request.body)
        text = tele_data['message']
        print("text",text['text'],tele_data['message']['from']['id'])
        chatId = tele_data['message']['chat']['id']
        text_message= text['text'].lstrip("/").strip()

        if text_message == "start":

            welcomeMsg =  """
            Hello! welcome to TelegramBot 
            """
            bot.sendMessage(chat_id=chatId, text=welcomeMsg, reply_to_message_id=text['message_id'])
            return "ok"

        else:

            data = {
                    "text":text_message,
                    "userId":tele_data['message']['from']
                }
            messageForm =MessageForm(data)

            if messageForm.is_valid():

                new_contact = messageForm.save(commit=False)
                uId = new_contact.userId
                count = Message.objects.filter(userId = uId).count()
                new_contact.save()
                messageForm.save_m2m()
                bot.sendMessage(chat_id=chatId, text=str(count + 1), reply_to_message_id=text['id'])
                return "ok"

            else:
                return bot.sendMessage(chat_id=chat_id, text="I don't understand", reply_to_message_id=text['id'])
