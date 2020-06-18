#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater, MessageHandler, Filters
import yaml

with open('credential') as f:
	credential = yaml.load(f, Loader=yaml.FullLoader)

tele = Updater(credential['bot_token'], use_context=True) # @GroupHub_bot

HELP_MESSAGE = '''
群组频道推荐：

平权观察 @equality_and_rights
英文学习 @english_learning_discuss
行动派公民联盟 @citizen_united
政治观察 @freedom_watch
读书分享 @dushufenxiang
程序员之家 @useless_project_ideas
新闻播报 @news_pdf
豆瓣精选 @douban_read
女权观察 @feminist_watch
网摘精选 @web_feed
写作交流 @writing_discuss
性别议题 @daily_feminist
文宣中国 @VoiceofCN
日语学习 @jp_study
微博精选 @weibo_read
频道合集 @channel_push
读书讨论 @dushufenxiang_chat
写作讨论 @writing_exchange

推荐群组，请联系 @b4cxb
'''

def handle(update, context):
	update.message.reply_text(HELP_MESSAGE)

if __name__ == '__main__':
	dp = tele.dispatcher
	dp.add_handler(MessageHandler(Filters.any, handle))
	tele.start_polling()
	tele.idle()