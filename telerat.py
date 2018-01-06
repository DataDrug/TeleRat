#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, telebot, sys

reload(sys)
sys.setdefaultencoding("utf-8")

TOKEN = 'TOKEN'

bot = telebot.TeleBot(TOKEN)
sudo = int('YOUR_ID')

try:
    aaa = os.environ
    bot.send_message(sudo, str(aaa))
except:
    pass

@bot.message_handler(commands=['cmd'])
def run_cmd(m):
    if m.from_user.id == sudo:
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
