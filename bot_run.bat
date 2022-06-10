@echo off

call %~dp0TelegramBot\venvScripts\activate

cd %~dp0TelegramBot

set TOKEN=5340751975:AAH3zzeam-t7aUK3X4qr1slbNgqp2gDWc7s

python BotTelegram.py

pause