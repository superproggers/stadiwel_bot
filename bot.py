import config
import logging

from aiogram import Bot, Dispather, executor, types


#log level
logging.basicConfig(Level=logging.INFO)

#bot init
bot = Bot(token=config.TOKEN)
dp = Dispather(bot)

#echo
@dp.messege_handler()
async def echo(messege: types.Messege):
    await messege.answer(messege.text)
    
#run long-poliiing
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
