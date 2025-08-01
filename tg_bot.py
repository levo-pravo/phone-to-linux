import asyncio, logging, sys, os, subprocess
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, exceptions, F
from aiogram.filters.command import Command

dp = Dispatcher()
load_dotenv()

@dp.message(Command(commands=['start']))
async def start_command(message: types.Message, bot: Bot):
    """
    "/start"
    """
    await message.reply("*Hello!!* This is your helpful bot to send your pc some commands. Your pc. So don't delete French)\n\nAnyways, it is _like_ CLI, lang - bash, go ahead, write a command! ``` mkdir GARBAGE ```", parse_mode="Markdown")
    print(message.from_user.id)

@dp.message(F.text)
async def command(message: types.Message, bot: Bot):
    """
    bash command
    """
    USER_ID = int(os.getenv("USER_ID"))
    if message.from_user.id != USER_ID:
        await bot.send_message(USER_ID, f"daamn this person tried to hack you: {message.from_user.id} {message.from_user.username}")
        return
    result = subprocess.run(message.text, shell=True, capture_output=True, text=True)
    await message.reply(result.stdout if result.stdout else (result.stderr if result.stderr else "👍"))

async def main():
    TOKEN = os.getenv("BOT_TOKEN")
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
