import logging
import os
import time

import psycopg2
import telebot
from flask import Flask, request
from telebot import types

from data.config import *

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

# connect to data base
db = psycopg2.connect(DB_URI, sslmode="require")
sql = db.cursor()
