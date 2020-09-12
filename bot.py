import discord
from discord.utils import get





client = discord.Client()
user = discord.User
guild = discord.Guild
roleUser = discord.Member
result = []


@client.event
async def on_ready():
    print('Бот зашел: {0.user}'.format(client))
    


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    

test = 0
@client.event
async def on_member_join(ctx):
    nameUser = str(ctx) # Получаем имя пользователя + тег
    buffName = nameUser[0]+nameUser[1]+nameUser[2] # извлекаем номер группы
    try:
        test = int(buffName)
        if(isinstance(test,int)): # Проверяем если buffName принадлежит к типу int то вначале имени пользователя написана группа и нам нужно дать роль
            
            #print(roles[buffName])
            role = discord.utils.get(ctx.guild.roles, name = buffName + " группа") 
            await ctx.add_roles(role)
            print("Студенту - "+ nameUser + " добавили роль "+buffName)
            
    except: # Если не int то это преподаватель и у него в начале имени нет цифр
        print("Новый участник")
        #role = discord.utils.get(ctx.guild.roles, name = "Преподаватели") #Получаем id или позицию роли
        #await ctx.add_roles(role) # Команда добавления роли | ctx(Member) контекст
        #print("Преподаватель - "+ nameUser + " добавлен")
		

roles = { # Просто пусть будет вдруг пригодится
    '101': "101 группа",
    '103': "103 группа",
    '104': "104 группа",
    '105': "106 группа",
    '107': "107 группа",
    '108': "108 группа",
    '109': "109 группа",
    '114': "114 группа",
    '201': "201 группа",
    '203': "203 группа",
    '204': "204 группа",
    '205': "205 группа",
    '206': "206 группа",
    '207': "207 группа",
    '209': "209 группа",
    '301': "301 группа",
    '303': "303 группа",
    '304': "304 группа",
    '306': "306 группа",
    '307': "307 группа",
    '314': "314 группа",
    '401': "401 группа",
    '403': "403 группа",
    '404': "404 группа",
    '405': "405 группа",
    '406': "406 группа",
    '407': "407 группа",
    '415': "415 группа"
}

client.run('NjkyNjM2MTUwMTYyMjYwMDc5.XnxZrg.X7H6yCs5tDtZ73LqvZgQ_uzczus')

