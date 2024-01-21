import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, InputFile, InputMediaPhoto
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
from aiogram.types.input_file import FSInputFile

TOKEN = getenv('BOT_TOKEN')

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
	await bot.delete_webhook()
	video_file_id = 'DQACAgIAAxkBAAIBZGWqqUTCB-3UjzqAUqS9YUGvkCw3AAIBQQACOzkwSWuOC4dO6oamNAQ'
	await bot.send_video_note(message.from_user.id, video_file_id)

	await message.answer(f"{hbold(message.from_user.full_name)}, приветствую тебя!😍\nНа связи Кристина Плахотникова\nИ если ты здесь, значит самое время вывести твой блог на новый уровень🔥\n\nЯ знаю, что тебе тяжело совмещать работу с ведением блога и совсем не хватает времени на то, чтобы каждый день придумывать идеи для сторис…\n\nНо не переживай! У меня есть то, что поможет тебе💯\n\nЯ создала для тебя готовый контент-план для сторис на целую неделю, которые ты сможешь снимать, даже не выходя из дома!\n\nХочешь получить контент-план?👇🏼", reply_markup=InlineKeyboardBuilder().add(types.InlineKeyboardButton(text='ДА, ХОЧУ😍', callback_data='button_1')).as_markup())


@dp.callback_query(F.data == "button_1")
async def button_1(callback: types.CallbackQuery):
	await callback.message.answer(f'Отлично, твой контент-план для сторис уже готов!🤩\n\nНо чтобы он принес тебе желаемый результат в виде высоких охватов, большой вовлеченности аудитории и качественного прогрева к твоим услугам\n\nДавай пройдемся по всем важные элементам УПАКОВКИ твоего аккаунта и проверим, продает ли она тебя как сильного эксперта\n\nТы же не хочешь потерять потенциальных клиентов только из-за отсутствия продающей упаковки аккаунта?', reply_markup=InlineKeyboardBuilder().add(types.InlineKeyboardButton(text='ПРОВЕРИТЬ УПАКОВКУ', callback_data='button_2')).as_markup())
	await callback.answer()


@dp.callback_query(F.data == 'button_2')
async def button_2(callback: types.CallbackQuery):
	await callback.message.answer(f'Шапка профиля, после которой захочется подписаться😏\n\nЕсли в жизни встречают по одежке, то в соцсетях — по упаковке, и первое, что видит твой потенциальный клиент — это именно шапка профиля\n\nС первого взгляда на шапку людям должно быть понятно, кто ты, чем занимаешься и как ты можешь быть им полезен\n\nЕсли она не зацепит, то человек дальше не пойдет❌\n\nЯ подготовила для тебя подробный урок, как создать шапку профиля, после которой на тебя захочется подписаться и следить за твоим контентом\n\nПрямо сейчас жми на кнопку внизу👇🏼 и проверь, отражает ли твоя шапка блога тебя как сильного эксперта', reply_markup=InlineKeyboardBuilder().add(types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК', callback_data='button_3')).as_markup())
	await callback.answer()


@dp.callback_query(F.data == 'button_3')
async def button_3(callback: types.CallbackQuery):
	lesson1_id = 'BAACAgIAAxkBAAIBSGWqpRxOwQa0PulZsi0fUGRINmYuAAJrOwACh_tQSeHiSBnHiA8qNAQ'
	await bot.send_video(callback.from_user.id, lesson1_id)

	await callback.message.answer(f'Не забудь надеть шапку!\nОй, то есть, оформить шапку😏\n\nПомни, что любой рост начинается с новых действий, и даже если ты уже 100 раз менял свою шапку профиля, посмотри урок и проверь не упустил ли ты ничего важного✅\n\nДаже самый маленький и незначительный на первый взгляд элемент может стать ключевым в желании человека подписаться на тебя\n\nКак только закончишь просмотр, жми по кнопке внизу👇🏼, чтобы проверить следующий важный элемент упаковки твоего блога', reply_markup=InlineKeyboardBuilder().add(types.InlineKeyboardButton(text='УЖЕ ПОСМОТРЕЛ✅', callback_data='button_4')).as_markup())
	await callback.answer()


@dp.callback_query(F.data == 'button_4')
async def button_4(callback: types.CallbackQuery):
	await callback.message.answer(f'Актуальные сторис, которые продают за тебя💸\n\nПоздравляю!🥳 Теперь ты знаешь, как оформить себе продающую шапку профиля, которая зацепит твою целевую аудиторию\n\nНо помни, что люди покупают у людей, а для этого им нужно узнать тебя поближе, поэтому следующее, куда они пойдут — это твои актуальные сторис\n\nИменно в них мы можем подробно раскрыть себя как интересную личность, сильного эксперта, и поделиться, какие услуги и продукты помогут решить проблемы наших  потенциальных клиентов\n\nБлагодаря правильным актуальным сторис, твой блог будет продавать, даже если ты не выходишь в сторис 24/7\n\nЯ подготовила для тебя короткий видеоурок, чтобы ты смог проверить себя на правильность оформления продающих актуальных сторис, жми на кнопку внизу👇🏼 и переходи к просмотру', reply_markup=InlineKeyboardBuilder().add(types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК', callback_data='button_5')).as_markup())
	await callback.answer()


@dp.callback_query(F.data == 'button_5')
async def button_5(callback: types.CallbackQuery):
	lesson2_id = 'BAACAgIAAxkBAAIBPGWqoFtaAAEc_EQ925O6COTXZNeeeAACVEIAApf7WUk-eC3xh7HGxjQE'
	await bot.send_video(callback.from_user.id, lesson2_id)

	await callback.message.answer(f'Уже посмотрел урок? Там просто куча инсайтов🤯\n\nТакую информацию можно получить только на моих стратегических консультациях, но тебе я отдаю её абсолютно бесплатно\n\nТолько после одного урока по продающим сторис, мои ученики повышают охваты минимум в 2 раза, а их подписчики начинают вовлекаться, ставить реакции и отвечать на опросы🔥\n\nА если ты уже закончил просмотр урока, то жми по кнопке внизу👇🏼, чтобы перейти к завершающему важному элемент упаковки твоего блога', reply_markup=InlineKeyboardBuilder().add(types.InlineKeyboardButton(text='ГОТОВ ИДТИ ДАЛЬШЕ✅', callback_data='button_6')).as_markup())
	await callback.answer()


@dp.callback_query(F.data == 'button_6')
async def button_6(callback: types.CallbackQuery):
	await callback.message.answer(f'Как выделяться среди конкурентов за счет дорогого и уникального визуала🤫\n\nСогласись, что все эти банальные фотографии с ноутбуком, ногточками, кофе и цветами всем уже давно приелись🫠\n\nВизуал — это один из важнейших элементов упаковки, по которому аудитория будет запоминать и узнавать тебя\n\nТолько благодаря одному качественному визуалу, ты уже можешь увеличить стоимость своих услуг в 2 раза🔝\n\nТак, как же выделяться среди конкурентов, за счет уникального стиля ведения блога? И какие фотографии выкладывать в ленту именно в твоей нише?\n\nЖми по кнопке внизу👇🏼 и смотри короткий видеоурок по составлению продающего визуала для твоего аккаунта', reply_markup=InlineKeyboardBuilder().add(types.InlineKeyboardButton(text='СМОТРЕТЬ УРОК', callback_data='button_7')).as_markup())
	await callback.answer()


@dp.callback_query(F.data == 'button_7')
async def button_7(callback: types.CallbackQuery):
	lesson3_id = 'BAACAgIAAxkBAAIBUGWqpqiF3DC8Zj1hvLtlqL0DiafXAAJ5OwACh_tQSQXBbtO5D4pTNAQ'
	await bot.send_video(callback.from_user.id, lesson3_id)

	await callback.message.answer(f'КАК ПОДНЯТЬ ОХВАТЫ В СТОРИС МИНИМУМ В 2 РАЗА🔝\n\nЗнакомьтесь, это Мария — эксперт по нейропсихологии, и она обратилась ко мне с проблемой, что подписчики совсем перестали реагировать на сторис и возникает такое чувство, будто разговариваешь сам с собой…\n\nот этого у Марии полностью пропало желание вообще вести сторис😔\n\nЯ проанализировала весь её контент и поняла, в чем, на самом деле, заключалась главная проблема — сторис Марии были хаотичны, они не раскрывали её как интересную личность и сильного эксперта , а соответственно подписчикам было просто неинтересно досматривать сторис до конца и реагировать на них\n\nНа консультации мы провели полноценную распаковку личности и экспертности Марии, достали нужные смыслы и темы для контента\n\nЯ рассказала по какой структуре нужно оформлять сторителлинги, чтобы они были не только интересными, но и прогревали подписчиков на покупку её услуг\n\nВ результате нашей консультации:\n\t⁃ охваты Марии сразу поднялись в 2 раза\n\t⁃ аудитория начала досматривать сторис до конца и реагировать на каждый опрос\n\t⁃ повысились лояльность и доверие к ней, как к эксперту\n\t⁃ появились заявки на её услуги и первые продажи консультаций с чеком 5.000₽\n\nТы тоже сможешь достичь таких же результатов, когда получишь мой готовый контент-план для сторис и начнешь внедрять его в свой блог🔥')

	file1 = 'AgACAgIAAxkBAAICemWrj0Uf9VNtXWJYpJdCKUYYjFM_AAJ71DEbKvRZSWvgiuOgpQyMAQADAgADcwADNAQ'
	file2 = 'AgACAgIAAxkBAAICfGWrj3e7r6vKHTrhPGl0pIXwTs_WAAJ-1DEbKvRZSfD3_QvLCyciAQADAgADcwADNAQ'
	media = []
	media.append(InputMediaPhoto(media=file1))
	media.append(InputMediaPhoto(media=file2))
	await bot.send_media_group(callback.from_user.id, media)

	await callback.message.answer(f'Ты ведь не забыл про свой подарок?🎁\n\nНе откладывай просмотр урока надолго, чтобы поскорее забрать свой долгожданный подарок\n\nПомни, что без качественной упаковки аккаунта, даже самый гениальный контент-план не принесет тебе новых подписчиков и регулярных продаж с блога \n\nКак только закончишь просмотр урока, смело жми по кнопке внизу👇🏼, чтобы получить то, ради чего ты оказался здесь', reply_markup=InlineKeyboardBuilder().add(types.InlineKeyboardButton(text='ГОТОВО✅', callback_data='button_8')).as_markup())
	await callback.answer()


@dp.callback_query(F.data == 'button_8')
async def button_8(callback: types.CallbackQuery):
	await callback.message.answer(f'Контент-план для сторис из дома на целую неделю🔥\n\nПоздравляю!🥳 Твоя продающая упаковка аккаунт готова, и теперь ты можешь забрать свой контент-план для сторис на целую неделю\n\nОсновное преимущество моего контент-плана — это то, что ты сможешь реализовать его даже из дома! Тебе не придется выходить на улицу, искать интересные локации, придумывать инфоповоды, нет, я уже обо всем позаботилась!\n\nТебе нужно лишь:\n\t1. Открыть готовый контент-план по кнопке внизу\n\t2. Внимательно изучить первую тему и адаптировать её под свою нишу\n\t3. Оформить серию сторис, следуя моим рекомендациям в контент-плане\n\nГотово! Ты молодец!🤩\nПопробуй вести сторис целую неделю по моему плану и смотри, как заметно будут увеличиваться твои охваты, вовлеченность и продажи🔥', reply_markup=InlineKeyboardBuilder().add(types.InlineKeyboardButton(text='«Забрать контент-план»', callback_data='button_9')).as_markup())
	await callback.answer()


@dp.callback_query(F.data == 'button_9')
async def button_9(callback: types.CallbackQuery):
	await bot.send_document(callback.from_user.id, 'BQACAgIAAxkBAAICq2WrkfconiSLRkIVvAlYQwrB469jAALVQwACKvRZSUGPjHkXv4EAATQE')

	await callback.answer()
	await asyncio.sleep(10)
	await callback.message.answer(f'У меня для тебя подарок!🎁\n\nДа, ты все правильно понял, еще один подарок, потому что ты этого заслуживаешь!\n\nДля того, чтобы удерживать внимание твоих подписчиков и делать регулярные продажи с блога, одной недели в сторис, к сожалению, будет недостаточно\n\nТебе нужен подробный план действий, что выкладывать в сторис и рилс именно в твоей нише, чтобы привлекать новых подписчиков и получать постоянные заявки на твои услуги\n\nЯ хочу подарить тебе личный бесплатный разбор, после которого ты получишь:\n\t• готовую стратегию продвижения твоего блога\n\t• индивидуальный подбор форматов и идей для контента, который будет набирать тысячи просмотров\n\t• эффективную воронку продаж для привлечения клиентов в твой блог\n\nДля того, чтобы получить бесплатный разбор, заполни короткую анкету по кнопке внизу👇🏼, и я лично напишу тебе, чтобы договориться о дате и времени проведения консультации❤️', reply_markup=InlineKeyboardBuilder().row(types.InlineKeyboardButton(text='ХОЧУ РАЗБОР', callback_data='button_10')).as_markup())


@dp.callback_query(F.data == 'button_10')
async def button_10(callback: types.CallbackQuery):
	
	await asyncio.sleep(3)
	await callback.message.answer(f'Ссылка на анкету', reply_markup=InlineKeyboardBuilder().row(types.InlineKeyboardButton(text='Анкета', url='https://forms.gle/ALWtWKh7ZJikPa3p8')).as_markup())
	await callback.answer()


async def main():
	await dp.start_polling(bot)


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO, stream=sys.stdout)
	asyncio.run(main())
