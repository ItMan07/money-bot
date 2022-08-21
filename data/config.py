from random import randint

# ====================== НАСТРОЙКИ ДЛЯ ПОДКЛЮЧЕНИЯ =======================

BOT_TOKEN = "5106190156:AAGQQdV5QU9MLRG2B4WRggzReE4WJlIxRL8"

ADMIN_ID = 1069565512

APP_URL = "https://money-bot-v2.herokuapp.com/" + BOT_TOKEN

DB_URI = "postgres://wcvxulvlyzfexk:27aa3e2d8c399f749935ec72cf154023246d469fae9df4c66e5e3f9f2371baa1" \
         "@ec2-34-253-119-24.eu-west-1.compute.amazonaws.com:5432/d62jvfrevnv5j0"

# ============================== НАСТРОЙКИ ===============================

reg_money = 5000                # начальный баланс
default_admin = False           # выдавать админку при регистрации

# ========================== НАСТРОЙКИ КАЗИНО ============================

chance = randint(1, 8)
chanseCasino = [1, 2, 3]
min_stavka = 100                # минимальная ставка

# ========================================================================
