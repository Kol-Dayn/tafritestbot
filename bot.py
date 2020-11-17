import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
from random import randint
import json
from discord.ext import commands
import datetime
import time
import os
import discord
from urllib.parse import urlparse
from discord import utils
import pip  
import io
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot( command_prefix = '!' )
client.remove_command('help')

# SlowMode
@client.command(aliases=['slowmode','SlowMode','Slowmode','SLOWMODE'])
@commands.has_permissions(manage_channels = True)
async def slowMode(ctx,delay:int = None):
    if delay == None:
        await ctx.send(embed = discord.Embed(title = "<:error:777151328912539699> Ошибка",description = "Укажите время в секундах. Например: 21600(6ч)",color = discord.Color.red()))
        return
    if delay > 21600:
        await ctx.send(embed = discord.Embed(title = "<:error:777151328912539699> Ошибка",description = "Нельзя использовать время больше 21600с(6ч)",color =        discord.Color.red()))
        return
    if delay > 0:
        await ctx.channel.edit(slowmode_delay = delay)
        await ctx.send(embed = discord.Embed(title='Задержка между Сообщениями',description = f"Успешно! Установлена задержка между сообщениями {delay} секунд на участника",color = discord.Color.green()))

    if delay == 0:
        await ctx.channel.edit(slowmode_delay = delay)
        await ctx.send(embed = discord.Embed(title = "Задержка между Сообщениями",description = "Успешно! Задержка между сообщениями в этом канале была Отключена",color = discord.Color.green()))
        return
# Say
@client.command(aliases=['Say', 'SAY'])
@commands.cooldown(1, per = 120, type = discord.ext.commands.BucketType.member )
async def say(ctx, *, text=None):
    if text is None:
      emb = discord.Embed(title='<:ispolzvnkmd:777965160501346334> Использование', description = '!say <Текст>', color=0xff8c00)
      await ctx.send(embed=emb, delete_after = 10)
    else: 
      await ctx.send(embed = discord.Embed(description=f'**Сообщение от: {ctx.message.author.mention}**\n**Содержимое: {text}**' ,color = 0xf5ce42))

# ASay
@client.command(aliases=['Asay', 'ASAY'])
@commands.cooldown(1, per = 120, type = discord.ext.commands.BucketType.member )
async def asay(ctx, *, text=None):
    if text is None:
      emb = discord.Embed(title='<:ispolzvnkmd:777965160501346334> Использование', description = '!asay <Текст>', color=0xff8c00)
      await ctx.send(embed=emb, delete_after = 10)
    else: 
      await ctx.channel.purge(limit = 1)
      await ctx.send(embed = discord.Embed(description=f'**Анонимное сообщение**\n**Содержимое: {text}**' ,color = 0xf5ce42))

# Authors
@client.command(aliases=['Authors','AUTHORS'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def authors(ctx):
    emb = discord.Embed(title='Автор бота: Sleim#2191',color=0xf5ce42)
    emb.set_footer(text="Пожалуйста не пишите в лс за кодом!")
    await ctx.send(embed=emb)

# Pashalka
@client.command(aliases=['11vlad111dun','11vlad111DUN','11VLAD111DUN','11VLAD111dun'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def _11vad111dun(ctx):
    emb = discord.Embed(title='Главный дундук: влад#8945',color=0xf5ce42)
    emb.set_footer(text="Очень опасный дундук! Сожрёт нафиг!")
    await ctx.send(embed=emb)

# Pashalka2
@client.command(aliases=['Piskogriz','PISKOGRIZ'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def piskogriz(ctx):
    emb = discord.Embed(title='Опасный Писко-Грыз: ПЁСЕЛЬ#9447',color=0xf5ce42)
    emb.set_footer(text="Отгрызёт пипискю Нафиг! Опасно!")
    await ctx.send(embed=emb)

# Idea
@client.command()
@commands.cooldown(1, per = 300, type = discord.ext.commands.BucketType.member )
async def idea(ctx, *, idea=None):
    if idea is None:
        embed = discord.Embed(title="<:ispolzvnkmd:777965160501346334> Использование", description="!idea <Идея>", color=0xff8c00)
        await ctx.send(embed=embed,delete_after=10)
    else:
        member = await client.fetch_user(user_id=624491783522484225)
        embed = discord.Embed(title="Новая Идея!", description=f"**Отправитель:\n**{ctx.message.author.mention}\n**Айди:**\n{ctx.author.id}\n**Идея:**\n{idea}", color=discord.Color.green())
        await member.send(embed=embed)
        embed2 = discord.Embed(title="Успешно!", description=f"Идея была успешно отправлена создатаелю\n**Содержимое:**\n{idea}", color=discord.Color.green())
        await ctx.send(embed=embed2)

# Bag
@client.command()
@commands.cooldown(1, per = 300, type = discord.ext.commands.BucketType.member )
async def bag(ctx, *, idea=None):
    if idea is None:
        embed = discord.Embed(title="<:ispolzvnkmd:777965160501346334> Использование", description="!bag <Баг>", color=0xff8c00)
        await ctx.send(embed=embed,delete_after=5)
    else:
        member = await client.fetch_user(user_id=624491783522484225)
        embed = discord.Embed(title="Новый Баг!", description=f"**Отправитель:\n**{ctx.message.author.mention}\n**Айди:**\n{ctx.author.id}\n**Идея:**\n{idea}", color=discord.Color.red())
        await member.send(embed=embed)
        embed2 = discord.Embed(title="Успешно!", description=f"Баг был успешно отправлена создатаелю\n**Содержимое:**\n{idea}", color=discord.Color.green())
        await ctx.send(embed=embed2)

# Help
@client.command(aliases=['Help', 'HELP','h','H'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def help(ctx, text=None):
    if text is None:
        emb = discord.Embed(title='Помощь по коммандам', description='Чтобы посмотреть команды раздела, напишите: `!help <раздел>`', color=0xf5ce42)
        emb.add_field(name='• Модерация', value = 'Команды помогут админам и модераторам!')
        emb.add_field(name='• Информация', value = 'Команды для просмотра информации о `сервере` и `пользователях`')
        emb.add_field(name='• Утилиты', value = '`Полезные` команды для сервера')
        emb.add_field(name='• Игры', value = 'Команды для разных `мини-игр`',)
        emb.add_field(name='• Полезности', value = 'Разные команды, как `погода`, `напомнить` и другие')
        emb.add_field(name='• Весёлости', value = '`Шутки` и `анекдоты` которые поднимут вам настроения')
        emb.set_footer(text="© Tafri? Все права защищены! || BETA - Версия", icon_url='https://cdn.discordapp.com/attachments/756984631655661621/759119830186983444/cartoon-monster-face-avatar-halloween-monster_6996-1159.jpg')
        await ctx.send(embed=emb)
    elif text == "Модерация":
        emb = discord.Embed(title='Помощь по командам', description='Вы выбрали раздел: Модерация', color=0xf5ce42)
        emb.add_field(name='Все команды:', value='`!kick`,`!ban`,`!mute`,`!warn`,`!clear`,`!poll`,`!ads`')
        await ctx.send(embed=emb)
    elif text == "модерация":
        emb = discord.Embed(title='Помощь по командам', description='Вы выбрали раздел: Модерация', color=0xf5ce42)
        emb.add_field(name='Все команды:', value='`!kick`,`!ban`,`!mute`,`!warn`,`!clear`,`!poll`,`!ads`')
        await ctx.send(embed=emb)
    elif text == "МОДЕРАЦИЯ":
        emb = discord.Embed(title='Помощь по командам', description='Вы выбрали раздел: Модерация', color=0xf5ce42)
        emb.add_field(name='Все команды:', value='`!kick`,`!ban`,`!mute`,`!warn`,`!clear`,`!poll`,`!ads`')
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title='<:error:777151328912539699> Ошибка', description='Раздел не найден!', colour=discord.Color.red())
        await ctx.channel.purge(limit = 1)
        await ctx.send(embed=emb)

# Avatar
@client.command(aliases=['AVATAR', 'Avatar', 'Ava', 'ava', 'AVA'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def avatar(ctx, *,  avamember : discord.Member=None):
    if avamember is None:
        avamember = ctx.author
    userAvatarUrl = avamember.avatar_url
    emb=discord.Embed(title=f'Аватар пользователя {avamember.name}:', description=f'[Скачать]({avamember.avatar_url})', color=0xf5ce42)
    emb.set_image(url=f'{userAvatarUrl}')
    await ctx.send(embed=emb)

# Kiss
@client.command(aliases=['Kiss', 'KISS'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def kiss(ctx, *, member : discord.Member):
        
        if member == ctx.author:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Вы не можете поцеловать Себя!')
            await ctx.send(embed=emb, delete_after=10)
 
            return

        elif member == ctx.bot.user:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Меня нельзя поцеловать!')
            await ctx.send(embed=emb, delete_after=10)   

        else:
            emb=discord.Embed(title='Поцелуй', description=f'{ctx.message.author.mention} поцеловал(а) {member.mention}', color=0xFF69B4)
            await ctx.send(embed=emb)

# Hug
@client.command(aliases=['Hug', 'HUG'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def hug(ctx, *, member : discord.Member):
        
        if member == ctx.author:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Вы не можете обнять Себя!')
            await ctx.send(embed=emb, delete_after=10)
 
            return

        elif member == ctx.bot.user:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Меня нельзя обнять!')
            await ctx.send(embed=emb, delete_after=10)   

        else:
            emb=discord.Embed(title='Обнятие', description=f'{ctx.message.author.mention} обнял(а) {member.mention}', color=0xFF69B4)
            await ctx.send(embed=emb)

# Bump
@client.command(aliases=['Bump', 'BUMP'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def bump(ctx, *, member : discord.Member):
        
        if member == ctx.author:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Вы не можете ударить Себя!')
            await ctx.send(embed=emb, delete_after=10)
 
            return

        elif member == ctx.bot.user:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Меня нельзя ударить!')
            await ctx.send(embed=emb, delete_after=10)   

        else:
            emb=discord.Embed(title='Удар', description=f'{ctx.message.author.mention} ударил(а) {member.mention}', color=0x4682B4)
            await ctx.send(embed=emb)

# Invite
@client.command(aliases=['Invite', 'INVITE', 'inv', 'Inv', 'INV'])
@commands.cooldown(1, per = 300, type = discord.ext.commands.BucketType.member )
async def invite(ctx):
    emb=discord.Embed(title=f'Пригласить бота на сервер:', description=f'[Здесь](https://discord.com/oauth2/authorize?client_id=759039852246466630&permissions=8&scope=bot)', color=0xf5ce42)
    await ctx.send(embed=emb)

# UserInfo
@client.command(aliases=['Usernfo', 'USERINFO'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def userinfo(ctx,member:discord.Member = None):
    if member is None:
        member = ctx.author
    sts = str(member.status)
    if sts == "dnd":
        
        emb = discord.Embed(description=f'**Информация о пользователе {member}**',color=0xf5ce42)
        emb.add_field(name='Настоящее имя:',value=member.name)
        emb.add_field(name='Изменённое имя:',value=member.display_name)
        emb.add_field(name="Статус:", value=f'<:ne_besp:756986604844744895>  Не беспокоить', inline=False)
        emb.add_field(name='Когда присоеденился:',value=member.joined_at,inline=False)
        emb.add_field(name="Дата регистрации:", value="{}".format(member.created_at)[:-7], inline=False)
        emb.add_field(name="Высшая роль:", value=f'{member.top_role.mention}', inline=False)
        emb.add_field(name="Пользовательский статус:", value=f'{member.activity.name}'.split('.')[-1].title(), inline=True)
        emb.add_field(name='ID:',value=member.id,inline=False)
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed = emb)

    elif sts == "online":
        
        emb = discord.Embed(description=f'**Информация о пользователе {member}**',color=0xf5ce42)
        emb.add_field(name='Настоящее имя:',value=member.name)
        emb.add_field(name='Изменённое имя:',value=member.display_name)
        emb.add_field(name="Статус:", value=f'<:online:756986578731139213>  Онлайн', inline=False)
        emb.add_field(name='Когда присоеденился:',value=member.joined_at,inline=False)
        emb.add_field(name="Дата регистрации:", value="{}".format(member.created_at)[:-7], inline=False)
        emb.add_field(name="Высшая роль:", value=f'{member.top_role.mention}', inline=False)
        emb.add_field(name="Пользовательский статус:", value=f'{member.activity.name}'.split('.')[-1].title(), inline=True)
        emb.add_field(name='ID:',value=member.id,inline=False)
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed = emb)

    elif sts == "idle":
        
        emb = discord.Embed(description=f'**Информация о пользователе {member}**',color=0xf5ce42)
        emb.add_field(name='Настоящее имя:',value=member.name)
        emb.add_field(name='Изменённое имя:',value=member.display_name)
        emb.add_field(name="Статус:", value=f'<:ne_activ:756986590852546701>   Не активен', inline=False)
        emb.add_field(name='Когда присоеденился:',value=member.joined_at,inline=False)
        emb.add_field(name="Дата регистрации:", value="{}".format(member.created_at)[:-7], inline=False)
        emb.add_field(name="Высшая роль:", value=f'{member.top_role.mention}', inline=False)
        emb.add_field(name="Пользовательский статус:", value=f'{member.activity.name}'.split('.')[-1].title(), inline=True)
        emb.add_field(name='ID:',value=member.id,inline=False)
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed = emb)

    elif sts == "offline":
        
        emb = discord.Embed(description=f'**Информация о пользователе {member}**',color=0xf5ce42)
        emb.add_field(name='Настоящее имя:',value=member.name)
        emb.add_field(name='Изменённое имя:',value=member.display_name)
        emb.add_field(name="Статус:", value=f'<:offline:756986562801172512>    Оффлайн', inline=False)
        emb.add_field(name='Когда присоеденился:',value=member.joined_at,inline=False)
        emb.add_field(name="Дата регистрации:", value="{}".format(member.created_at)[:-7], inline=False)
        emb.add_field(name="Высшая роль:", value=f'{member.top_role.mention}', inline=False)
        emb.add_field(name="Пользовательский статус:", value=f'{member.activity.name}'.split('.')[-1].title(), inline=True)
        emb.add_field(name='ID:',value=member.id,inline=False)
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed = emb)

# Lot
@client.command(aliases=['Lot','LOT'])
async def lot(ctx, arg = None):
    if arg == None:
        embed = discord.Embed(
            title = 'Лотерея', 
            description = 'Напиши свой ответ, от 1 до 3', 
            color = 0xf5ce42
        )

        await ctx.send(embed=embed)

    else:
            
           choice = random.choice(["1", "2", "3"])

    if arg == choice:
            embed = discord.Embed(
                title = 'Лотерея', 
                description = 'Ты победил!', 
                color = 0xf5ce42
            )

            await ctx.send(embed=embed)

    else:
            embed = discord.Embed(
                title = 'Лотерея', 
                description = 'Ты проиграл(а)..', 
                color = 0xf5ce42
            )

            await ctx.send(embed=embed)

# 8Ball
@client.command(aliases=['8ball', '8BALL', '8Ball'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def _8ball(ctx, *, question=None):
    if question is None:
      emb = discord.Embed(title='<:ispolzvnkmd:777965160501346334> Использование', description = '!8ball <Вопрос>', color=0xff8c00)
      await ctx.send(embed=emb, delete_after = 10)
    else:
      responses = ['Это точно.',
                 'Без сомнений.',
                 'Загадочный ответ.',
                 'Определённо - Да.',
                 'Вы можете положиться на него.',
                 'Знаки указывают на да.',
                 'Прогноз хороший.',
                 'Наверняка.',
                 'Да.',
                 'Ответ туманный, попробуй ещё раз.',
                 'Спроси позже.',
                 'Очень сомнительно.',
                 'Лучше не говорить тебе сейчас.',
                 'Не могу сейчас предсказать.',
                 'Сконцентрируйся и спроси снова.',
                 'Не рассчитывай на это.',
                 'Мой ответ нет.',
                 'Мои источники говорят нет.',
                 'Прогноз не очень хороший.']

    emb = discord.Embed(title='🎱 Шар',color=0xf5ce42)
    emb.add_field(name='Вопрос:', value=question, inline=False)
    emb.add_field(name='Предсказание:',value=random.choice(responses))
    await ctx.channel.send(embed=emb)

# Poll
@client.command(aliases=['Poll', 'POLL'])
@commands.has_permissions( manage_messages = True )
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def poll(ctx, *, message):
    emb=discord.Embed(title='📢 Голосование', color=0xEE82EE, description=f':bar_chart: {message}')
    await ctx.channel.purge(limit = 1)
    msg=await ctx.send(embed=emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    

# Pig
pig= [
    "https://cdn.iz.ru/sites/default/files/styles/640x360/public/news-2018-02/200910224_gaf_u46_4944.jpg?itok=v0eul4qO",
    "https://o-prirode.ru/wp-content/uploads/2018/10/1600x1000-03.jpg",
    "https://cdn.fishki.net/upload/post/2018/02/13/2511394/tn/svinya-porosnok-zagorod-kopyta-krupnyy-plan-lico-78678-1920x1200.jpg",
    "https://simple-fauna.ru/wp-content/uploads/2015/10/morskaya-svinka-1.jpg",
    "https://svinki.ru/media/original_images/27072811-416-640x585_pMBrO4C.jpg",
    "https://zooclub.ru/attach/34000/34411.jpg",
    "https://opt-1031816.ssl.1c-bitrix-cdn.ru/upload/resize_cache/iblock/a0a/750_400_1/texel_svinka.jpg?1528195922120417",
    "https://lemurrr.ru/medias/sys_master/images/hca/h91/8904033435678.jpg",
    "https://faunistics.com/wp-content/uploads/2019/08/6-7.jpg",
    "https://3.bp.blogspot.com/-sZsfIdK_ELA/V1WS4yvg-lI/AAAAAAAAJyg/USz8nT7L2wc9b_taQTZ-VWHvryhRuefBgCLcB/s1600/bg3-1024x708.jpg",
    "https://3.bp.blogspot.com/-sZsfIdK_ELA/V1WS4yvg-lI/AAAAAAAAJyg/USz8nT7L2wc9b_taQTZ-VWHvryhRuefBgCLcB/s1600/bg3-1024x708.jpg",
    "https://wildfrontier.ru/wp-content/uploads/2018/12/1-1-700x461.jpg",
    "https://msvinkam.ru/wp-content/uploads/2018/12/1-17.jpg",
    "https://vplate.ru/images/article/thumb/480-0/2019/03/spisok-imen-dlya-morskih-svinok.jpg",
    "https://i.simpalsmedia.com/point.md/news/thumbnails/large/be77fc0f5dd94388b7e8d3fb952fda52.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Two_adult_Guinea_Pigs_%28Cavia_porcellus%29.jpg/275px-Two_adult_Guinea_Pigs_%28Cavia_porcellus%29.jpg",
    "https://ptichka.net/wp-content/uploads/kormlenie-morskix-svinok-300x225.jpg",
    "https://homkin.ru/wp-content/uploads/2018/06/pig21-651x381.jpg",
    "https://svinki.ru/media/original_images/03_mrD4Tj1.jpg",
    "https://zoozov.com/wp-content/uploads/attachpost/1988/post-1988-0.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR862u0cIxAgGeLwqG9lT68WqEsI4Q_vpfvEg&usqp=CAU",
    "https://s1.1zoom.ru/prev2/391/390089.jpg",
    "https://vplate.ru/images/article/thumb/480-0/2019/03/porody-morskih-svinok-6.jpg",
    "https://svinki.ru/media/original_images/self.jpg",
    "https://www.zoospravka.ru/Rabbit/images/guinea_pig.jpg",
    "https://msvinkam.ru/wp-content/uploads/2018/01/1-2.jpg",
    "https://svinki.ru/media/original_images/04_8bl3PFw.jpg",
    "https://homkin.ru/wp-content/uploads/2018/07/70.2-678x381.jpg"
]
@client.command(aliases=['Pig', 'PIG'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def pig(ctx):
    emb=discord.Embed(title=f'Свинка по вашему запросу:', color = 0xf5ce42)
    emb.set_image(url=f'{random.choice(pig_url)}')
    await ctx.channel.send(embed=emb)

# Rabbit
@client.command(aliases=['Rabbit', 'RABBIT'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def rabbit(ctx):
    emb=discord.Embed(title=f'Эта комманда в стадии Разработки!', description=f'Идея от: влад#8945', color=0xf5ce42)
    await ctx.channel.send(embed=emb)

# Anime
anime_url=[
    "https://cs10.pikabu.ru/post_img/big/2019/12/01/6/1575187650162046634.jpg",
    "https://cs10.pikabu.ru/post_img/big/2019/11/08/10/1573232625120584589.jpg",
    "https://i08.kanobu.ru/r/98337ae40ef114cf07c92cac8dbb9688/1040x700/u.kanobu.ru/editor/images/51/c48787a0-4259-47a3-b32a-ddb4f311c753.jpg",
    "https://handskill.ru/assets/i/ai/4/7/7/i/3279083.jpg",
    "https://studlive.by/wp-content/uploads/2019/06/87afef76100d0b704ca5b6039468a736.jpg",
    "https://i.pinimg.com/736x/23/5b/9d/235b9d214577a12e7ecbd6a455c07a21.jpg",
    "https://javasea.ru/uploads/posts/2019-06/1561478293_udivlennaya-anime-devushka-v-naushnikah.jpg",
    "https://aiger.s3-ap-northeast-1.amazonaws.com/vecherniymagadanrf/uploads/common/2018/10/03/v_rossii_nachnet_veschanie_pervyiy_tsifrovoy_anime_kanal-79076-b.jpg",
    "https://aiger.s3-ap-northeast-1.amazonaws.com/vecherniymagadanrf/uploads/common/2018/10/03/v_rossii_nachnet_veschanie_pervyiy_tsifrovoy_anime_kanal-79076-b.jpg",
    "https://pbs.twimg.com/profile_images/879892012169809920/nSMKcU7G_400x400.jpg",
    "https://www.goha.ru/s/A:NX/Xj/utWvPIbVmY.jpg",
    "https://cdnimg.rg.ru/i/photogallery/2020/05/05/134b96b981987aa/134b96b981987aa1588674946.jpg",
    "https://img2.akspic.ru/image/145951-anime-zvukovoe_oborudovanie-krasnyj_cvet-multfilm-art-1080x1920.jpg",
    "https://i.pinimg.com/originals/04/56/d0/0456d04b6dc2b5131af7f539677b2f5f.jpg",
    "https://lh3.googleusercontent.com/proxy/gctNQXGnFkEeiBvo043B7F5S-A-intL0aVbA6x1bCohcqrVAs3YxHj3u-VdJLtKRZeOJPRq8BJsTZWw5nADzmmiJVO4OK6VcFe1apSFFz0FvgtDK",
    "https://lh3.googleusercontent.com/proxy/i_OxH1XOWGFP7H9EBRzr0WcPsr8x2flouof5d3P3soA9pZVi0ffdkdWrRIlnmsDsfXXq2iONV1TnVFqm2WmICiAFJhDB1_GWkYJPxU2dRZqLEkHGhdTL26IMQOp4EyMUGyF_cyUYhpOEpp5pvIZ5RMRu_9vw8g",
    "https://s16.stc.all.kpcdn.net/putevoditel/serialy/wp-content/uploads/2020/04/anime-naruto-19895-1024x751.jpg",
    "https://proprikol.ru/wp-content/uploads/2019/11/kartinki-anime-s-ushkami-3.jpg",
    "https://trikky.ru/wp-content/blogs.dir/1/files/2020/03/29/image-8-1.jpg",
    "https://sharp-worlds.ru/wp-content/uploads/2019/10/27b8d3c4ad0edaeef6b058c48d77e15c-559x445.jpg",
    "https://a.wattpad.com/cover/154264104-288-k993235.jpg",
    "https://novostivl.ru/media/article/2020/04-11/WYL798c.JPG",
    "https://avatars.mds.yandex.net/get-zen_doc/95163/pub_5d722f45febcd400adcc7e7d_5d7230ae3d873600ae6a7653/scale_1200",
    "https://i.gifer.com/72TP.gif",
    "https://acegif.com/wp-content/uploads/anime-kiss-m.gif",
    "https://steamuserimages-a.akamaihd.net/ugc/847094437699170356/AADF1CAE39E607CE0109B9543956577241D6DFFE/",
    "https://i.pinimg.com/originals/59/37/1e/59371e16bf2c92a158a0bf84e1e70bb6.gif",
    "https://anime-chan.me/uploads/posts/2017-01/1485468525_anime-elsword-chung-elsword-anime-gif-3626491.gif",
    "https://i.imgur.com/WdwvW6I.gif",
    "https://i.gifer.com/Eykb.gif",
    "https://thumbs.gfycat.com/LivelyRawErmine-size_restricted.gif",
    "https://i.pinimg.com/originals/3a/f1/cc/3af1cc2e440012b9a79255b4f19190fc.gif",
    "https://thumbs.gfycat.com/WellwornForcefulLcont-size_restricted.gif",
    "https://i.gifer.com/Td9n.gif",
    "https://pa1.narvii.com/6691/94711cbd92c5fd6634bb970b1472c4293f8e1ee0_hq.gif",
    "https://giffiles.alphacoders.com/129/129852.gif",
    "https://cs5.pikabu.ru/post_img/big/2015/01/04/11/1420398784_174128187.jpg",
    "https://lh3.googleusercontent.com/proxy/x7Q4WPNYHrzLIxHGpXObBw6ldgaqW6KC472iDLOGAutsdpGKiFaF0kvyyoID5w7SFLgbCCg66KQgSo5JAsPZZ7RQvfSPYxe2kOHsOQ43CKu_GNfdYX7RtiTRQwG-zbE",
    "https://cdn.humoraf.ru/wp-content/uploads/2017/07/anime-gifs-03.gif",
    "https://lh3.googleusercontent.com/proxy/ID1tcoSOKjZ3fut6_ibuBXbZxwpi8D_S2tTNBF6_7zBN2Otg78vsERbOdgIB2hPuwc5r_8FeE3ToU3Ozkxa6qYJ-Zczp8x5z49rv071rVrsrvjGeNwlk9njP1fHQy1KmQFITM5SGB6C3xfF_kBMnWlCJDf2splC64oaF"
    "https://lh3.googleusercontent.com/proxy/lujWpeEUhJeWX3HYwW9VohDUJbJavnKYMA6OoWjewCv8v9dlPdvq1U6ZDK2f0ooV0WuhF5S14Z8HjGBBEzDaEkA7z5NTtm7q8UQ0WpgEMmTe4oBERnKMud9F77mFh57ewd72ozM-Kw_kUCRQEWmbmuKZ47jB0ntZVZssftdXYKq2aqDhvemhz8JLsmZQ1X0G-ZRKtfdH3-tKaEnERi604QU6B0AkrA5j",
    "https://99px.ru/sstorage/86/2016/12/image_862712160326125610113.gif",
    "https://lh3.googleusercontent.com/proxy/6ctR_lMklYh3yJbnyeeguJPfmjVwbqRi-etc70rLQfBHi0AojgyvqIn0CEtHegFxU_XrB62F3BeApWC649Zu4UneVitRi8zQ23H0i6DYfznQtTHirdG6OaLu0fdVQMZrZUOMeaH8PQpp9_3yFFRxWdzoM-PTcAo-aRV5k7934DLqvg",
    "https://thumbs.gfycat.com/PhonyVainBlackandtancoonhound-size_restricted.gif"

]
@client.command(aliases=['Anime', 'ANIME'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def anime(ctx):
    emb=discord.Embed(title=f'Аниме по вашему запросу:', color = 0xf5ce42)
    emb.set_image(url=f'{random.choice(anime_url)}')
    await ctx.channel.send(embed=emb)

# Turtle
turtle_url=[
    "https://friendofthesea.org/wp-content/uploads/turtle-logo-piccolo-1024x728.jpg",
    "https://i.ytimg.com/vi/riFyKUyGb4k/maxresdefault.jpg",
    "https://cdn.cnn.com/cnnnext/dam/assets/181205104053-01-turtle-plastic-super-tease.jpg",
    "https://api.timeforkids.com/wp-content/uploads/2020/04/turtle1.jpg?w=1455&h=970",
    "https://chinadialogueocean.net/wp-content/uploads/2018/08/sea-turtle-547162_1920-e1534168069327.jpg",
    "https://chinadialogueocean.net/wp-content/uploads/2019/02/F5A919-1440x720.jpg",
    "https://cdn.britannica.com/s:800x450,c:crop/66/195966-138-F9E7A828/facts-turtles.jpg",
    "https://www.insureandgo.com.au/images/1905-header-world-turtle-day-797x57px_tcm1005-547715.jpg"
]
@client.command(aliases=['Turtle', 'TURTLE'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def turtle(ctx):
    emb=discord.Embed(title=f'Черепаха по вашему запросу:', color = 0xf5ce42)
    emb.set_image(url=f'{random.choice(turtle_url)}')
    await ctx.channel.send(embed=emb)

# Cat
cat_url =[
    "https://ichef.bbci.co.uk/news/976/cpsprodpb/15C06/production/_109449098_catsstaring.jpg",
    "httphttps://cdn22.img.ria.ru/images/154903/39/1549033902_0:75:541:480_1400x0_80_0_0_174613c57e45339661874ee511d7dee6.jpgs://img.gazeta.ru/files3/501/12982501/upload-05-pic4_zoom-1500x1500-18539.jpg",
    "https://cdn22.img.ria.ru/images/154903/39/1549033902_0:75:541:480_1400x0_80_0_0_174613c57e45339661874ee511d7dee6.jpg",
    "https://cdn24.img.ria.ru/images/156350/82/1563508223_0:133:360:336_1400x0_80_0_0_3fd9fcd6e96fdc256ef6dce17dcb5f04.jpg",
    "https://s1.stc.all.kpcdn.net/putevoditel/projectid_103889/images/tild3133-3632-4366-b063-336638343832__cat-2934720_1280.jpg",
    "https://s1.stc.all.kpcdn.net/putevoditel/projectid_103889/images/tild3139-3265-4131-b134-323661643935__4.jpg",
    "https://cdn-st1.rtr-vesti.ru/vh/pictures/xw/194/594/0.jpg",
    "https://cdnimg.rg.ru/i/gallery/27a08cd9/7_9c58af28.jpg",
    "https://cdn.iz.ru/sites/default/files/styles/900x506/public/news-2019-08/20190730_zaa_s145_008.jpg?itok=jA2jjra6",
    "https://cdnimg.rg.ru/img/content/185/55/80/iStock-1030294600_d_850.jpg",
    "https://u.kanobu.ru/editor/images/24/9c004ffd-12f0-4f06-b637-4a834d97152f.jpg",
    "https://www.proplan.ru/sites/owners.proplan.ru/files/2020-03/domoshnyaa-koska_0.jpg",
    "https://cdn22.img.ria.ru/images/155067/14/1550671447_0:120:3111:1870_1400x0_80_0_0_4ae491800c7747ea95e3d2a78b3f29ec.jpg",
    "https://cdn2.img.inosmi.ru/images/24522/99/245229923.jpg",
    "https://www.purinaone.ru/cat/sites/purinaone.ru/files/2020-06/skolko-zhivut-koshki.jpg",
    "https://b1.m24.ru/c/1363097.580xp.jpg",
    "https://i-fakt.ru/wp-content/uploads/2013/04/fakty-koshka.jpg",
    "https://www.sobaka.ru/images/image/01/29/06/03/_normal.jpg",
    "https://www.dw.com/image/39366795_303.jpg",
    "https://www.purinaone.ru/cat/sites/purinaone.ru/files/2018-09/strahi-koshek_0.jpg",
    "https://funik.ru/wp-content/uploads/2018/12/75c255685547f880d166-700x607.jpeg",
    "https://centerslon.ru/wp-content/uploads/2018/07/pochemu-kot-ne-est.jpg",
    "https://kurjer.info/wp-content/uploads/2020/02/200226_cat-2.jpg",
    "https://files.hightech.plus/photos/article-09c7e10d-721f-443c-86dc-cb9647eddebd/c3d8a1aa-1b2d-4cdc-b891-1684c1390e39.jpeg",
    "https://cdn1.img.inosmi.ru/images/24367/66/243676638.jpg",
    "https://s3.nat-geo.ru/images/2019/9/24/24a9e840909a42f4b4df6e3d235f0e17.max-1200x800.jpg",
    "https://cs7.pikabu.ru/post_img/big/2019/09/01/5/1567319290160261184.jpg",
    "https://www.belta.by/images/storage/news/with_archive/2020/000029_1586962975_387408_big.jpg",
    "https://www.dw.com/image/38763482_303.jpg",
    "https://img.rl0.ru/385c4846625191729ea6ec92d3df62ae/c615x400i/https/news.rambler.ru/img/2020/03/15/102110.878527.1896.jpeg",
]
@client.command(aliases=['Cat', 'CAT'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def cat(ctx):
    emb=discord.Embed(title=f'Кошка по вашему запросу:', color = 0xf5ce42)
    emb.set_image(url=f'{random.choice(cat_url)}')
    await ctx.channel.send(embed=emb)

# Dog
url_dog=[
    "https://primamedia.gcdn.co/f/main/1937/1936556.jpg?ca2c24aa472396beadfd4a5eb8bf8a22",
    "https://dogdiary.ru/wp-content/uploads/2018/07/shhenok-zolotistogo-retrivera.jpg",
    "https://cdn25.img.ria.ru/images/151560/46/1515604661_0:0:2000:1126_600x0_80_0_0_e394110b29d3027cdb75d906476035fb.jpg",
    "https://s9.stc.all.kpcdn.net/share/i/12/11121956.wr-1200.sh-18.jpg",
    "https://dinozoopasaule.lv/ru/getimage/uploads/news/ikkXHS-2AesJFyftXGg2mEg82YscHLdd.png?w=600&h=400&fit=crop",
    "https://www.alpinabook.ru/upload/resize_cache/iblock/663/700_700_1/663f4c67619485c224c5b149b1f65eab.jpg",
    "https://brasil.ru/wp-content/uploads/2017/11/stock_606221315-719x480.jpg",
    "https://i.ytimg.com/vi/l_IvDxOBGJM/maxresdefault.jpg",
    "https://s1.stc.all.kpcdn.net/putevoditel/projectid_103889/images/tild3037-3231-4134-a333-303139306331__-5.jpg",
    "https://img.gorodskievesti.ru/wp-content/uploads/2020/08/sobaka1.jpg",
    "https://cdnimg.rg.ru/img/content/177/25/24/iStock-1026229726_t_650x433.jpg",
    "https://blog.thezoo.ru/wp-content/uploads/2013/05/0a2b847cadea7ad1c3c4fc302c57e2b8-640x375.jpg",
    "https://i.pinimg.com/originals/d9/e2/87/d9e28749db2fd3646cae1ae95c3489f4.jpg",
    "https://img.gazeta.ru/files3/724/12850724/Depositphotos_239584058_xl-2015-pic905-895x505-92650.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRdyyO7cDFVYl44zMswiQ339TjfEoYCZonbHg&usqp=CAU",
    "https://imgtest.mir24.tv/uploaded/images/crops/2018/March/870x489_0x34_detail_crop_b079576b4aec2553c0f4998f752dd8b2999ca6bd288775ddf9c87bd835f0e92d.jpg",
    "https://dressirovkavtomske.ru/wp-content/uploads/2019/03/maxresdefault.jpg",
    "https://s.hi-news.ru/wp-content/uploads/2018/06/dog_and_brain-2-750x499.jpg",
    "https://static.mk.ru/upload/entities/2017/12/28/articles/detailPicture/28/35/c2/84/c21033e59c396cc576fc5f48343ebccc.jpg",
    "https://radio1.news/files/image/06/10/30/-lg!08kx.jpg",
    "https://kubnews.ru/upload/resize_cache/iblock/f54/800_533_2/f54abab117936480884e26b2e9d1da2d.jpg",
    "https://simple-fauna.ru/wp-content/uploads/2018/01/sobaka-stala-agressivnoj.jpg",
    "https://avatars.mds.yandex.net/get-zen_doc/52716/pub_5d134e153c083200afc2b549_5d134e1c04d59300afd94eb2/scale_1200",
    "https://www.purinaone.ru/dog/sites/purinaonedog.ru/files/2020-06/alabai_1.jpg"
]
@client.command(aliases=['Dog', 'DOG'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def dog(ctx):
    emb=discord.Embed(title=f'Собака по вашему запросу:', color = 0xf5ce42)
    emb.set_image(url=f'{random.choice(url_dog)}')
    await ctx.channel.send(embed=emb)

# Battle
@client.command(aliases=['Battle', 'BATTLE'])
@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.member )
async def battle( ctx, member: discord.Member = None ):
    if member is None:
        emb = discord.Embed( title = f'<:ispolzvnkmd:777965160501346334> Использование', description='!battle <@Пользователь>', color = 0xff8c00)
        await ctx.send( embed = emb )
    elif member.id == ctx.author.id:
            emb = discord.Embed(title = '<:error:777151328912539699> Ошибка', description = f"Вы не можете сразится с собой!", color = 0xff8c00)
            await ctx.send( embed = emb )
    else:
        a = random.randint(1,2)
        if a == 1:
            emb = discord.Embed( title = f"Победитель - {ctx.author}", color = 0x00FF7F )
            await ctx.send( embed = emb )

            emb = discord.Embed( title = f"Проигравший - {member}", color = 0xFA8072    )
            await ctx.send( embed = emb )
        else:
            emb = discord.Embed( title = f"Победитель - {member}", color = 0x00FF7F)
            await ctx.send( embed = emb )

            emb = discord.Embed( title = f"Проигравший - {ctx.author}", color = 0xFA8072    )
            await ctx.send( embed = emb )

# Kick
@client.command(aliases=['Kick','KICK'])
@commands.has_permissions(kick_members = True)
@commands.cooldown(1, per = 60, type = discord.ext.commands.BucketType.member )
async def kick(ctx,member:discord.Member, *,reason='Причина не указанна!'):

        if member == ctx.bot.user:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Меня может кикнуть только Основатель сервера!')
            await ctx.send(embed=emb, delete_after=10)
 
            return

        elif member == ctx.author:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Вы не можете кикнуть себя!')
            await ctx.send(embed=emb, delete_after=10)
 
            return
 
        elif member == ctx.guild.owner:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Вы не можете кикнуть Основателя сервера!')
            await ctx.send(embed=emb, delete_after=10)
 
            return

        elif ctx.author.top_role < member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Вы не можете кикнуть участника с ролью выше чем у вас!')
            await ctx.send(embed=emb, delete_after=10)

        elif ctx.author.top_role == member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Вы не можете кикнуть участника с такой же ролью!')
            await ctx.send(embed=emb, delete_after=10)
 
            return
 
        else:
            emb = discord.Embed(title="Кик",color=0xFA8072)
            emb.add_field(name='Модератор: ',value=ctx.message.author.mention,inline=False)
            emb.add_field(name='Нарушитель: ',value=member.mention,inline=False)
            emb.add_field(name='Причина: ',value=reason,inline=False)
            await member.kick(reason=reason)
            await ctx.send( embed = emb )

            emb = discord.Embed(title="Информация",color=0xf5ce42)
            emb.add_field(name='Вы были кикнуты модератором:',value=f'{ctx.message.author.mention}')
            emb.add_field(name='По причине: ',value=reason,inline=False)
            emb.add_field(name='С сервера: ',value=f'{ ctx.guild.name }',inline=False)
            emb.set_footer(text=f'Если это было ошибкой, обратитесь к Основателю Сервера { ctx.guild.name }')
            await member.send( embed = emb)

# Ban
@client.command(aliases=['Ban','BAN'])
@commands.has_permissions(ban_members = True)
@commands.cooldown(1, per = 60, type = discord.ext.commands.BucketType.member )
async def ban(ctx,member:discord.Member, *,reason='Причина не указанна!'):

        if member == ctx.bot.user:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Меня может забанить только Основатель сервера!')
            await ctx.send(embed=emb, delete_after=10)
 
            return

        elif member == ctx.author:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Вы не можете забанить себя!')
            await ctx.send(embed=emb, delete_after=10)
 
            return
 
        elif member == ctx.guild.owner:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Вы не можете забанить Основателя сервера!')
            await ctx.send(embed=emb, delete_after=10)
 
            return

        elif ctx.author.top_role < member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Вы не можете забанить участника с ролью выше чем у вас!')
            await ctx.send(embed=emb, delete_after=10)

        elif ctx.author.top_role == member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:error:777151328912539699> Ошибка', value = 'Вы не можете забанить участника с такой же ролью!')
            await ctx.send(embed=emb, delete_after=10)
 
            return
 
        else:
            emb = discord.Embed(title="Бан",color=0xFA8072)
            emb.add_field(name='Модератор: ',value=ctx.message.author.mention,inline=False)
            emb.add_field(name='Нарушитель: ',value=member.mention,inline=False)
            emb.add_field(name='Причина: ',value=reason,inline=False)
            await member.ban(reason=reason)
            await ctx.send( embed = emb )

            emb = discord.Embed(title="Информация",color=0xf5ce42)
            emb.add_field(name='Вы были забанены модератором:',value=f'{ctx.message.author.mention}')
            emb.add_field(name='По причине: ',value=reason,inline=False)
            emb.add_field(name='С сервера: ',value=f'{ ctx.guild.name }',inline=False)
            emb.set_footer(text=f'Если это было ошибкой, обратитесь к Основателю Сервера { ctx.guild.name }')
            await member.send( embed = emb)

# Errors
@client.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed = discord.Embed(title = '<:error:777151328912539699> Ошибка', description = f'Такой команды не существует!', colour = discord.Color.red()), delete_after=10)

@help.error
async def help_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@kiss.error
async def kiss_error(ctx, error):
    if isinstance( error, commands.errors.MissingRequiredArgument ):
        emb = discord.Embed(color=0xff8c00)
        emb.add_field( name = '<:ispolzvnkmd:777965160501346334> Использование', value = '!kiss <@Пользователь>' )
        await ctx.send( embed = emb, delete_after=10 )
    if isinstance(error, commands.BadArgument):
        emb = discord.Embed(colour = discord.Color.red())
        emb.add_field( name = '<:error:777151328912539699> Ошибка', value = 'Пользователь не найден!', inline = False)
        await ctx.send( embed = emb, delete_after=10 )  
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@hug.error
async def hug_error(ctx, error):
    if isinstance( error, commands.errors.MissingRequiredArgument ):
        emb = discord.Embed(color=0xff8c00)
        emb.add_field( name = '<:ispolzvnkmd:777965160501346334> Использование', value = '!hug <@Пользователь>' )
        await ctx.send( embed = emb, delete_after=10 )
    if isinstance(error, commands.BadArgument):
        emb = discord.Embed(colour = discord.Color.red())
        emb.add_field( name = '<:error:777151328912539699> Ошибка', value = 'Пользователь не найден!', inline = False)
        await ctx.send( embed = emb, delete_after=10 )  
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@bump.error
async def bump_error(ctx, error):
    if isinstance( error, commands.errors.MissingRequiredArgument ):
        emb = discord.Embed(color=0xff8c00)
        emb.add_field( name = '<:ispolzvnkmd:777965160501346334> Использование', value = '!bump <@Пользователь>' )
        await ctx.send( embed = emb, delete_after=10 )
    if isinstance(error, commands.BadArgument):
        emb = discord.Embed(colour = discord.Color.red())
        emb.add_field( name = '<:error:777151328912539699> Ошибка', value = 'Пользователь не найден!', inline = False)
        await ctx.send( embed = emb, delete_after=10 )
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        emb = discord.Embed(colour = discord.Color.red())
        emb.add_field( name = '<:error:777151328912539699> Ошибка', value = 'Пользователь не найден!', inline = False)
        await ctx.send( embed = emb, delete_after=10 )
 
    if isinstance( error, commands.errors.MissingRequiredArgument ):
        emb = discord.Embed(title='**<:ispolzvnkmd:777965160501346334> Использование команды `!kick`**\nВыгнать пользователя с возможностью возврата',color=0xff8c00)
        emb.add_field( name = 'Использование', value = '`!kick <@Пользователь> [причина]`', inline = False)
        emb.add_field( name = 'Пример 1', value = '`!kick <@Пользователь>`\n┗Кикнет указанного пользователя без причины.', inline = False)
        emb.add_field( name = 'Пример 2', value = '`!kick <@Пользователь> [причина]`\n┗Кикнет указанного пользователя с указанной причиной.', inline = False)
        await ctx.send( embed = emb, delete_after=10 )
 
    if isinstance(error, commands.MissingPermissions):
        emb=discord.Embed(title =f'<:error:777151328912539699> Недостаточно для кика пользователей!', colour=discord.Color.red())
        emb.add_field(name='Нужные права:', value='\n Выгонять участников')
        await ctx.send(embed=emb, delete_after = 10)

    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        emb = discord.Embed(colour = discord.Color.red())
        emb.add_field( name = '<:error:777151328912539699> Ошибка', value = 'Пользователь не найден!', inline = False)
        await ctx.send( embed = emb, delete_after=10 )
 
    if isinstance( error, commands.errors.MissingRequiredArgument ):
        emb = discord.Embed(title='**<:ispolzvnkmd:777965160501346334> Использование команды `!ban`**\nВыгнать пользователя без возможности возврата',color=0xff8c00)
        emb.add_field( name = 'Использование', value = '`!kick <@Пользователь> [причина]`', inline = False)
        emb.add_field( name = 'Пример 1', value = '`!ban <@Пользователь>`\n┗Забанит указанного пользователя без причины.', inline = False)
        emb.add_field( name = 'Пример 2', value = '`!ban <@Пользователь> [причина]`\n┗Кикнет указанного пользователя с указанной причиной.', inline = False)
        await ctx.send( embed = emb, delete_after=10 )
 
    if isinstance(error, commands.MissingPermissions):
        emb=discord.Embed(title =f'<:error:777151328912539699> Недостаточно прав для бана пользователей', colour=discord.Color.red())
        emb.add_field(name='Нужные права:', value='\n Банить участников')
        await ctx.send(embed=emb, delete_after = 10)

    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@poll.error
async def poll(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        emb=discord.Embed(title='<:ispolzvnkmd:777965160501346334> Использование', description='!poll <Текст>', color=0xff8c00)
        await ctx.send(embed=emb, delete_after=10)
    if isinstance(error,commands.MissingPermissions):
        emb=discord.Embed(description =f'<:error:777151328912539699> Недостаточно прав для создания голосования!', colour=discord.Color.red())
        emb.add_field(name='Нужные права:', value='\n Управления сообщениями')
        await ctx.send(embed=emb, delete_after=10) 
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@asay.error
async def asay_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``8ball``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@idea.error
async def idea_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@bag.error
async def bag_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@invite.error
async def invite_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

@_11vad111dun.error
async def _11vlad111dun_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
        title='<:error:777151328912539699> Ошибка',
        description=f"У вас еще не прошел кулдаун на команду ``11vald111dun``!\nПодождите еще {error.retry_after:.2f} секунд", colour=discord.Color.red()), delete_after=10)

# Anti - Ls
@client.event
async def on_message(message):
    try:
        try:
            if isinstance(message.channel, discord.DMChannel):
                return
        except AttributeError:
            return
        await client.process_commands(message)
    except TypeError:
        return

# Connect
stats = cycle(['!help', 'Sleim - Лучший!','!bag','!idea'])
@client.event
async def on_ready():
  change_stats.start()
  print('Login!')
@tasks.loop(seconds = 10)
async def change_stats():
  await client.change_presence( status = discord.Status.online, activity = discord.Game(name = next(stats)))
  print('Prefix - Reload!')

token = os.environ.get('BOT_TOKEN')