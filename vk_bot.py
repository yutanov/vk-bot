#!/usr/bin/env python

import itertools
import database
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text

# connection to vk
group_id = '' # enter group id
secret = '' # enter key

bot_token = secret
bot_group_id = group_id
vk = Bot(bot_token, bot_group_id)


# getting data from database
cat1 = database.categories[0]
cat2 = database.categories[1]
cat3 = database.categories[2]

cat = [cat1, cat2, cat3]

goods_cat1 = database.cat1
goods_cat2 = database.cat2
goods_cat3 = database.cat3
items = [
goods_cat1,
goods_cat2,
goods_cat3,
]

list_of_goods = list(itertools.chain(*items))

names = database.names
desc = database.descriptions
images = database.images
items_and_desc = dict(zip(names, desc))


# keyboard menu
@vk.on.private_message(text=[
    'Начать', 'начать', '/mm', 'menu', 'меню', 'Menu', 'Меню', 'Start', 'start',
])
@vk.on.private_message(payload={'cmd': 'menu'})
async def menu(message: Message):
    await message.answer(
        message='Что бы вы пожелали?',
        keyboard=(
            Keyboard(one_time=False, inline=False)
            .add(Text(cat1), color=KeyboardButtonColor.POSITIVE)
            .add(Text(cat2), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text(cat3), color=KeyboardButtonColor.POSITIVE)
        )
    )


@vk.on.private_message(text = cat)
async def menu(message: Message):
    msg = message.text
    i = cat.index(msg)
    await message.answer(
        message=msg,
        keyboard=(
            Keyboard(one_time=False, inline=False)
            .add(Text(items[i][0]), color=KeyboardButtonColor.POSITIVE)
            .add(Text(items[i][1]), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text(items[i][2]), color=KeyboardButtonColor.POSITIVE)
            .add(Text(items[i][3]), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('Назад', payload={'cmd': 'menu'}))
        )
    )


@vk.on.private_message(text = list_of_goods)
async def menu(message: Message):
    msg = message.text
    i = list_of_goods.index(msg)
    await message.answer(
        attachment=images[i],
        message=items_and_desc[msg],
        keyboard=(
            Keyboard(one_time=False, inline=False)
            .add(Text('Назад', payload={'cmd': 'menu'}))
        )
    )


@vk.on.private_message()
async def main(message):
    await message.answer('Пожалуйста, выберите что-нибудь из этих вкусностей :)')


vk.run_forever()
