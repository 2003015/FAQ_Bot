import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import asyncio
import aiohttp

bot = commands.Bot(command_prefix="~")

helpfile = "C:\\Users\\Reese\\Desktop\\nohelp.txt"
faqfile = "C:\\Users\\Reese\\Desktop\\faq.txt"
listfile = "C:\\Users\\Reese\\Desktop\\list.txt"

print("Online")

async def send(message, user, response):

    print("Message: "+message.content)
    print("Response: "+response)

    f = open(faqfile, "a")
    f.write("Message: "+message.content+"\r\n")
    f.write("Response: "+response+"\r\n\r\n")
    f.close()

    await bot.send_message(message.channel, user.mention+response)

def inhelp(id):
    if id == "339567608338710530":
        return True
    else:
        f = open(helpfile, "r")
        lines = f.readlines()
        f.close()
        for line in lines:
            if id in line:
                return True
        return False

def inlist(id):
    f = open(listfile, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        if id in line:
            return True
    return False

@bot.command(pass_context=True)
async def nohelp(ctx):
    if not inhelp(ctx.message.author.id):
        print("No help: "+ctx.message.author.display_name)
        f = open(helpfile,"a")
        f.write(ctx.message.author.id+"\r\n")
        f.close()
        await bot.say(ctx.message.author.mention+" You have opted out of FAQ help. Opt back in with ~yeshelp")

@bot.command(pass_context=True)
async def yeshelp(ctx):
    if inhelp(ctx.message.author.id):
        print("Yes help: "+ctx.message.author.display_name)
        f = open(helpfile, "r")
        lines = f.readlines()
        f.close()
        f = open(helpfile, "w")
        f.writelines([item for item in lines if ctx.message.author.id not in item and not item.isspace()])
        f.close()
        await bot.say(ctx.message.author.mention+" You have opted back into FAQ help.")

@bot.command(pass_context=True)
async def clear(ctx):
    if "450680633560399872" in [role.id for role in ctx.message.author.roles] or "449385190926712863" in [role.id for role in ctx.message.author.roles] or "339613815849353219" in [role.id for role in ctx.message.author.roles]:
        server = ctx.message.author.server
        async for message in (ctx.message.channel.history()):
            if message.author == bot.user:
                await message.delete()

@bot.command(pass_context=True)
async def sayin(ctx, *args):
    if "450680633560399872" in [role.id for role in ctx.message.author.roles] or "449385190926712863" in [role.id for role in ctx.message.author.roles] or "339613815849353219" in [role.id for role in ctx.message.author.roles]:
        message = ""
        for word in args[1:]:
            message += word
            message += " "
        await bot.send_message(ctx.message.channel_mentions[0], message)
        print(message)

@bot.command(pass_context=True)
async def listadd(ctx, user: discord.Member):
    if "451240245468332033" in [role.id for role in ctx.message.author.roles] or "339613815849353219" in [role.id for role in ctx.message.author.roles] or "450680633560399872" in [role.id for role in ctx.message.author.roles] or "449385190926712863" in [role.id for role in ctx.message.author.roles]:
        if not inlist(user.id):
            f = open(listfile, "a")
            f.write(user.id+"|"+str(user.display_name.encode('unicode_escape'))+"\r\n")
            f.close()
            await bot.say(user.mention+" has been added to the list.")
        else:
            await bot.say(user.mention+" is already on the list.")

@bot.command(pass_context=True)
async def listremove(ctx, user: discord.Member):
    if "451240245468332033" in [role.id for role in ctx.message.author.roles] or "339613815849353219" in [role.id for role in ctx.message.author.roles] or "450680633560399872" in [role.id for role in ctx.message.author.roles] or "449385190926712863" in [role.id for role in ctx.message.author.roles]:
        if inlist(user.id):
            f = open(listfile, "r")
            lines = f.readlines()
            f.close()
            f = open(listfile, "w")
            f.writelines([item for item in lines if user.id not in item and not item.isspace()])
            f.close()
            await bot.say(user.mention+" has been removed from the list.")
        else:
            await bot.say(user.mention+" is not on the list.")

@bot.command(pass_context=True)
async def list(ctx, i=10):
    guild = ctx.message.channel.server
    f = open(listfile, "r")
    reading = f.readlines()
    l = len(reading)
    f.close()
    if i > l:
        i = l
    f = open(listfile, "r")
    lines = []
    x = 0
    while x < i:
         lines.append(f.readline())
         x+=1
    f.close()
    await bot.send_message(guild.get_channel("452213143926734859"),"List:")
    n=0
    for line in lines:
        print(line)
        if len(line) > 1:
            index = line.find("|")
            name = line[index+1:]
            n+=1
            await bot.send_message(guild.get_channel("452213143926734859"),str(n)+". "+name)
    await bot.send_message(guild.get_channel("452213143926734859"), "Listed "+str(i)+" out of "+str(l)+".")

@bot.command(pass_context=True)
async def next(ctx):
    if "451240245468332033" in [role.id for role in ctx.message.author.roles] or "339613815849353219" in [role.id for role in ctx.message.author.roles] or "450680633560399872" in [role.id for role in ctx.message.author.roles] or "449385190926712863" in [role.id for role in ctx.message.author.roles]:
        guild = ctx.message.channel.server
        f = open(listfile, "r")
        lines = f.readlines()
        for line in lines:
            index = line.find("|")
            id = line[:index]
            member = guild.get_member(str(id))
            if member.status == guild.get_member(bot.user.id).status:
                break
        await bot.say(member.mention+" is the next online person on the list.")

@bot.command(pass_context=True)
async def listinsert(ctx, pos: int, user: discord.Member):
    if "451240245468332033" in [role.id for role in ctx.message.author.roles] or "339613815849353219" in [role.id for role in ctx.message.author.roles] or "450680633560399872" in [role.id for role in ctx.message.author.roles] or "449385190926712863" in [role.id for role in ctx.message.author.roles]:
        if not inlist(user.id):
            f = open(listfile, "r")
            lines = f.readlines()
            f.close()
            lines.insert(pos-1,user.id+"|"+user.display_name+"\r\n")
            f = open(listfile, "w")
            f.writelines(lines)
            f.close()
            await bot.say(user.mention+" has been inserted into the list at position "+str(pos)+".")
        else:
            await bot.say(user.mention+" is already on the list. Please remove them first.")

@bot.command(pass_context=True)
async def listlocate(ctx, user: discord.Member = None):
    if user == None:
        user=ctx.message.author
    f = open(listfile,"r")
    lines = f.readlines()
    f.close()
    temp = 0
    pos = 0
    for line in lines:
        temp += 1
        if user.id in line:
            pos = temp
            break
    if pos > 0:
        await bot.say(user.mention+" is in position "+str(pos)+" on the list.")
    else:
        await bot.say(user.mention+" is not on the list.")

@bot.event
async def on_message(message):

    user = message.author

    f = open(helpfile,"r")
    lines = f.readlines()
    f.close()

    if not inhelp(user.id):

        m = message.content.lower()
        if len(m) < 51:

            if "how" in m and "ascend" in m and ("do" in m or "can" in m):
                response = " You have to click the candle when it is off and hope no one turns it back off for 777 seconds. We have an organized list of who will ascend in which order, please ask to be added by a List Keeper in <#450922435915677697>"
                await send(message, user, response)
            if "what" in m and ("ascension" in m or "ascending" in m) and ("is" in m or "does" in m):
                response = " Ascension allows you to get out of the hole early. You also receive 51 dedication points and the ability to create a VIP room later."
                await send(message, user, response)
            if "how" in m and ("join" in m or "hand" in m or "get in" in m or "enter" in m or ("create" in m and "account" in m)) and "joined" not in m and "joining" not in m and ("can" in m or "do" in m) and "hole" not in m:
                response = " To join the church, keep refreshing the main page until you see a hand in the bottom left corner. It appears every 336 seconds. You can use https://poppy-church.glitch.me/hand to help."
                await send(message, user, response)
            if "how" in m and "hole" in m and ("get in" in m or "enter" in m or "work" in m) and ("do" in m or "can" in m):
                response = " To enter the hole, click the self destruct button on your personal report page."
                await send(message, user, response)
            if "how" in m and "hole" in m and ("get out" in m or "leave" in m or "long" in m) and ("do" in m or "can" in m):
                response = " You automatically leave the hole after 24 hours, or you can ascend."
                await send(message, user, response)
            if ("how" in m or "what" in m) and "guardian" in m and ("do" in m or "is" in m):
                response = " Guardians are picked by Poppy, herself. They are usually highly active members of the community."
                await send(message, user, response)
            if "help " in m and "email" in m and "is" in m:
                response = " The email is help@poppy.church"
                await send(message, user, response)
            if "change" in m and "avatar" in m and ("do" in m or "can" in m):   
                response = " You can change your your avatar at https://poppy.church/settings"
                await send(message, user, response)
            if ("should" in m or "do " in m or "can " in m) and ("click" in m or "touch" in m) and "candle" in m and "not" not in m:
                response = " Only click the candle if it is your turn to ascend! To ascend with it, you must be the last person to turn it on before it reaches 0!"
                await send(message, user, response)
            if "what" in m and "candle" in m and "happens" not in m:
                response = " The candle is used to ascend."
                await send(message, user, response)
            if "what" in m and "hole" in m and ("is" in m or "does" in m):
                response = " The hole is the only real game part of the website right now. Once in the hole, you can try to ascend."
                await send(message, user, response)
            if "how" in m and ("get" in m or "earn" in m or "gain " in m or "receive" in m) and ("points" in m or "dedication" in m or "loyalty" in m or "faith" in m) and ("do" in m or "does" in m or "can" in m):
                response = " They seem to increase over time, multiple people have reported getting points if they have their personal report page open at 3:36 PST. You also get 51 dedication by ascending."
                await send(message, user, response)
            if ("will" in m or "is" in m) and ("be" in m or "potential" in m) and "chat" in m and "there" in m:
                response = "  It is coming, as confirmed by poppy.church support email" 
                await send(message, user, response)
            if "change" in m and "signature" in m and ("do" in m or "can" in m):
                response = " You can change your signature by contacting the support email at help@poppy.church"
                await send(message, user, response)
            if "what" in m and "candle" in m and "happens" in m:
                response = " The candle will toggle between on and off. Only click it if it is your turn to ascend!"
                await send(message, user, response)
            if "what" in m and "are" in m and "whispers" in m:
                response = " Check out the pins in <#450469478342328327>."
                await send(message, user, response)
            if "what" in m and ("is" in m or "are" in m) and "popcoin" in m:
                response = " https://poppy.church/popcoin was found. We are unsure of what it does. Popcoin was the name given by us to the last section on the personal report."
                await send(message, user, response)
            if "what" in m and ("is" in m or "are" in m) and ("points" in m or "dedication" in m or "loyalty" in m or "faith" in m):
                response = " We aren't yet sure what the points on the reports are for."
                await send(message, user, response)
            if "what is love" in m:
                response = " Baby don't hurt me, don't hurt me, no more"
                await send(message, user, response)
            if "when" in m and ("floor" in m or "accepted" in m):
                response = " We aren't sure when, hopefully soon!"
                await send(message, user, response)
            if "what" in m and ("get" in m or "receive" in m or "earn" in m) and "ascend" in m:
                response = " You receive 51 dedication points and the ability to create a VIP room later."
                await send(message, user, response)
            if "what" in m and "vip" in m:
                response = " You get the ability to create a VIP room by ascending. Nothing else is known about it."
                await send(message, user, response)
            if "can" in m and "see" in m and ("click" in m or "touch" in m) and "candle" in m:
                response = " We used to be able to, but it led to harassment and the ability was removed."
                await send(message, user, response)
            if "what" in m and "self" in m and "destruct" in m:
                response = " Self-destructing takes you to the hole."
                await send(message, user, response)
            if "what" in m and "hand" in m and ("is" in m or "do" in m):
                response = " The hand allows you to join the church without a blessing."
                await send(message, user, response)
            if "what" in m and ("happens" in m or ("do" in m and ("get" in m or "receive" in m or "earn" in m))) and "leave" in m and "hole" in m:
                response = " If you ascend, you gain 51 dedication and the ability to make a VIP room later. If you leave after 24 hours, nothing but freedom."
                await send(message, user, response)
            if "what" in m and "countdown" in m and ("do" in m or "for" in m):
                response = " The countdown is long as long as the candle is on. Once it reaches 0, someone ascends."
                await send(message, user, response)
            if "what" in m and "phone number" in m:
                response = " 831-777-6779"
                await send(message, user, response)
            if "339567608338710530" in m and "love" in m and "you" in m:
                response = " I love you, too."
                await send(message, user, response)
            if "where" in m and "is" in m and "candle" in m:
                response = " The candle is in the hole"
                await send(message, user, response)
            if ("we" in m or "i" in m) and " not in a cult" in m:
                await bot.send_message(message.channel, message.content)
            if "would you wear it" in m:
                await bot.send_message(message.channel, "Wear a carrot?")

    await bot.process_commands(message)

bot.run("MzM5NTY3NjA4MzM4NzEwNTMw.De-IuA.RIgXji1OzYdYsmS42a_OjV27Ay0")