import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import asyncio
import aiohttp


print("Online")

bot_prefix="~"
bot = commands.Bot(command_prefix=bot_prefix)

listDebugState = False
dataFileLocation = "C:\\Users\\" + os.getlogin() + "\\Desktop\\Poppy.Church"
print(os.getlogin())

dataFiles = {"help":dataFileLocation + "\\nohelp.txt",
				"faq":dataFileLocation + "\\faq.txt",
				"list":dataFileLocation + "\\list.txt",
				"go":dataFileLocation + "\\go.txt",
				"token":dataFileLocation + "\\token.txt",
				"lang":dataFileLocation + "\\lang.txt"
}

messages = {"nohelp":" You have opted out of FAQ help. Opt back in with ~yeshelp",
			"yeshelp":" You have opted back into FAQ help."
}

faqMessages = {
	"en":{"HowToAscend":" You have to click the candle when it is off and hope no one turns it back off for 777 seconds. We have an organized list of who will ascend in which order, please ask to be added by a List Keeper in <#450922435915677697>",
		"WhatIsAscension":" Ascension allows you to get out of the hole early. You also receive 51 dedication points and the ability to create a VIP room later.",
		"HowToJoinChurch":" To join the church, keep refreshing the main page until you see a hand in the bottom left corner. It appears every 336 seconds. You can use https://poppy-church.glitch.me/hand to help.",
		"HowToEnterHole":" To enter the hole, click the self destruct button on your personal report page.",
		"HowToGetOut":" You automatically leave the hole after 24 hours, or you can ascend.",
		"WhatIsGuardian":" Guardians are picked by Poppy, herself. They are usually highly active members of the community.",
		"WhatIsSupportEmail":" The email is help@poppy.church",
		"HowToChangeAvatar":" You can change your your avatar at https://poppy.church/settings",
		"ShouldIClickCandle":" Only click the candle if it is your turn to ascend! To ascend with it, you must be the last person to turn it on before it reaches 0!",
		"WhatIsCandle":" The candle is used to ascend.",
		"WhatIsHole":" The hole is the only real game part of the website right now. Once in the hole, you can try to ascend.",
		"HowToEarnPoint":" They seem to increase over time, multiple people have reported getting points if they have their personal report page open at 3:36 PST. You also get 51 dedication by ascending.",
		"IsThereAChat":" It is coming, as confirmed by poppy.church support email" ,
		"HowToChangeSignature":" You can change your signature by contacting the support email at help@poppy.church",
		"WhatHappensToCandle":" The candle will toggle between on and off. Only click it if it is your turn to ascend!",
		"WhatAreWhispers":" Check out the pins in <#450469478342328327>.",
		"WhatIsPopcoin":" https://poppy.church/popcoin was found. We are unsure of what it does. Popcoin was the name given by us to the last section on the personal report.",
		"WhatArePoints":" We aren't yet sure what the points on the reports are for.",
		"WhatIsLove":" Baby don't hurt me, don't hurt me, no more",
		"WhenWillIBeAccepted":" We aren't sure when, hopefully soon!",
		"WhatIsVip":" You get the ability to create a VIP room by ascending. Nothing else is known about it.",
		"WhoClicked":" We used to be able to, but it led to harassment and the ability was removed.",
		"WhatIsSelfDestruct":" Self-destructing takes you to the hole.",
		"WhatIsHand":" The hand allows you to join the church without a blessing.",
		"WhatIsResultOfLeaving":" If you ascend, you gain 51 dedication and the ability to make a VIP room later. If you leave after 24 hours, nothing but freedom.",
		"WhatIsCountDown":" The countdown is long as long as the candle is on. Once it reaches 0, someone ascends.",
		"WhatIsPhoneNumber":" 831-777-6779",
		"Loveyou":" I love you, too.",
		"WhereIsTheCandle":" The candle is in the hole",
		"WhoIsPoppy":" Poppy is our savior.",
		"WhatIsPoppyChurch":" Poppy.Church is the house of our savior (also it's an ARG)."},
	"es":{"HowToAscend":" Necesitas dar click a la vela cuando este apagada y esperar a que nadie la apague de nuevo por 777 segundos. Tenemos una lista organizada de quien va a ascender y en que orden,por favor pide que te añadan a la lista, mediante un List Keeper en #the-hole",
		"WhatIsAscension":" Ascender te permite salir del 'The Hole' mas rapido. Tambien recibiras *51 Dedications Points* y la habilidad de crear un Cuarto VIP mas adelante.",
		"HowToJoinChurch":" Para entrar a *Poppy's Church*, recarga la pagina principal hasta que veas un icono de mano en la esquina inferior izquierda. Esta aparece cada 336 segundos. Puedes usar https://poppy-church.glitch.me/hand para ayudarte.",
		"HowToEnterHole":" Para entrar a 'The Hole', haz click en el boton de *Self-Destruct* en tu pagina de reporte personal.",
		"HowToGetOut":" Despues de 24 horas, se te expulsara automaticamente de 'The Hole', o puedes ascender.",
		"WhatIsGuardian":" Los Guardianes son escogidos por Poppy. Usualmente son miembros muy activos de la comunidad.",
		"WhatIsSupportEmail":" El email es help@poppy.church",
		"HowToChangeAvatar":" Puedes personalizar tu avatar en https://poppy.church/settings",
		"ShouldIClickCandle":" Solo haz click a la vela cuando sea tu turno de ascender! Para ascender con la vela, deberas ser la ultima persona en prenderla antes de que llegue a 0!",
		"WhatIsCandle":" La vela es usada para ascender.",
		"WhatIsHole":" 'The Hole' es el unico juego que es parte del sitio en este momento. Una vez en el 'The Hole', puedes tratar de ascender.",
		"HowToEarnPoint":" Al parecer crecen con el tiempo, varias personas han reportado que han ganado puntos si tienen su pagina de reporte personal activa a las 3:36 PST. Tambien puedes obtener *51 Dedication points* al ascender.",
		"IsThereAChat":" Esta por llegar, esto esta confirmado por el email de soporte de poppy.church" ,
		"HowToChangeSignature":" Puedes cambiar tu firma contactando al email de soporte @ help@poppy.church",
		"WhatHappensToCandle":" La vela se puede prender o apagar. Solo da click cuando sea tu turno de ascender!",
		"WhatAreWhispers":" Checa los mensajes anclados en #the-whispers.",
		"WhatIsPopcoin":" Se encontro https://poppy.church/popcoin No estamos seguros de que hace. *Popcoin* fue el nombre dado por nosotros en la ultima sección de nuestro reporte personal.",
		"WhatArePoints":" No estamos completamente seguros del uso de los puntos en los reportes personales.",
		"WhatIsLove":" Baby don't hurt me, don't hurt me, no more",
		"WhenWillIBeAccepted":" No estamos seguros de cuando, esperamos que sea pronto!",
		"WhatIsVip":" Obtienes la hablidad de crear Cuartos VIP al ascender. No tenemos mas información al respecto.",
		"WhoClicked":" Antes era posible ver, pero dio como resultado acoso entre los miembros y la funcion fue removida.",
		"WhatIsSelfDestruct":" La auto-destruccion hace que entres al 'The Hole'.",
		"WhatIsHand":" La mano, de da la opción de unirte a *Poppy's Church* sin tener una bendición.",
		"WhatIsResultOfLeaving":" Si asciendes, se te dan *51 Dedication Points* y la habilidad de crear Cuartos VIP mas adelante. Si sales despues de 24 horas, obtienes solamente tu libertad.",
		"WhatIsCountDown":" El contador estara encendido mientras la vela lo este. Una vez que llegue a 0, alguien ascendera.   ",
		"WhatIsPhoneNumber":" 831-777-6779",
		"Loveyou":" Yo tambien te amó!",
		"WhereIsTheCandle":" La vela esta en *The Hole*",
		"WhoIsPoppy":" Poppy es nuestra salvadora.",
		"WhatIsPoppyChurch":" Poppy.Church es la casa de nuestra salvadora (tambien conocida como ARG)."}
}

def initializeDataFiles():
	for key, value in dataFiles.items():
		file = open(value, "r+")
		file.close()

def GetUserLanguage(id):
	userLang = "en"
	if inDataFile("lang", id):
		lines = getLines["lang"]
		for line in lines:
			data = line.split("|")
			userLang = data[1]
			break
	return userLang

def GetLangCode(language):
	langCode = ""
	if language == "es" or "spanish":
		langCode = "es"
	elif language == "en" or "english":
		langCode = "en"
	return langCode
	
async def send(message, user, response):
	print("Message: " + message.content)
	print("Response: " + response)
	file = open(dataFiles["faq"], "a")
	file.write("Message: " + message.content + "\n")
	file.write("Response: " + response+"\n\n")
	file.close()
	await bot.send_message(message.channel,user.mention + response)

def getLines(file):
	file = open(file, "r")
	lines = file.readlines()
	file.close()
	
	return lines
	
def addDataToFile(key, data):
	file = open(dataFiles[key],"a")
	file.write(data + "\n")
	file.close()
	
def inDataFile(key, element):
	return element in open(dataFiles[key],"r").read()
	
def inhelp(id):
	return id == "339567608338710530" or inDataFile("help", id)
	
def removeFromSupport(id):
	addDataToFile("help", id)
	
def addToSupport(id, lang="en"):
	lines = getLines(dataFiles["help"])
	"""AddList = lambda list, user : [item for item in list if user.id not in item and not item.isspace()]"""
	file = open(dataFiles["help"], "w")
	file.writelines([item for item in lines if id not in item and not item.isspace()])
	file.close()
	
def inlist(id):
	return inDataFile("list", (id))
	
@bot.command(pass_context=True)
async def lang(ctx, language):
	if len(language) < 15:
		if GetLangCode(language) != "":
			addDataToFile("lang", ctx.message.author.id + "|" + langCode)
		else:
			await bot.say(ctx.message.author.mention + " Sorry I do not speak " + language + " yet.")
	
@bot.command(pass_context=True)
async def nohelp(ctx):
	if not inhelp(ctx.message.author.id):
		print("No help: " + ctx.message.author.display_name)
		addToSupport(ctx.message.author)
		await bot.say(ctx.message.author.mention + messages["nohelp"])

@bot.command(pass_context=True)
async def yeshelp(ctx):
	if inhelp(ctx.message.author.id):
		print("Yes help: "+ctx.message.author.display_name)
		removeFromSupport(ctx.message.author.id)
		await bot.say(ctx.message.author.mention + messages["yeshelp"])

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
			message += word + " "
		await bot.send_message(ctx.message.channel_mentions[0], message)
		print(message)
	
def canEditList(user):
	return "451240245468332033" in [role.id for role in user.roles] or "339613815849353219" in [role.id for role in user.roles] or "450680633560399872" in [role.id for role in user.roles] or "449385190926712863" in [role.id for role in user.roles]
	
@bot.command(pass_context=True)
async def listadd(ctx, user: discord.Member):
	if canEditList(ctx.message.author):
		message = ""
		if not inlist(user.id):
			if "\\" in str(user.display_name.encode('unicode_escape')):
				index = str(user.display_name.encode('unicode_escape')).find("\\")
				name = str(user.display_name.encode('unicode_escape'))[2:index]
			else:
				name = user.display_name
			f = open(dataFiles["list"], "a")
			f.write(user.id+"|"+name+"\n")
			f.close()
			lines = getLines(dataFiles["list"])
			message = " has been added to the list."
		else:
			message = " is already on the list."
		await bot.say(user.display_name + message)

@bot.command(pass_context=True)
async def listremove(ctx, user: discord.Member):
	if canEditList(ctx.message.author):
		if inlist(user.id):
			lines = getLines(dataFiles["list"])	 
			file = open(dataFiles["list"], "w")
			file.writelines([item for item in lines if user.id not in item and not item.isspace()])
			file.close()
			await bot.say(user.display_name+" has been removed from the list.")
		else:
			await bot.say(user.display_name+" is not on the list.")

@bot.command(pass_context=True)
async def list(ctx):
	guild = ctx.message.channel.server
	lines = getLines(dataFiles["list"])
	
	index=0
	n=0
	output = ""
	embedSent = False

	toDelete=[]
	async for x in bot.logs_from(guild.get_channel("452213143926734859")):
		toDelete.append(x)
	if len(toDelete) > 1:
		await bot.delete_messages(toDelete)
	elif len(toDelete) == 1:
		await bot.delete_message(toDelete[0])

	for line in lines:
		if len(line) > 1:
			index = line.find("|")
			nums = line[:index]
			n += 1
			if listDebugState:
				print(nums)
			output += str(n)+". "+guild.get_member(str(nums)).display_name+"\n"
			if len(output) > 1930:
				if not embedSent:
					embed = discord.Embed(title="List:",description=output)
				else:
					embed = discord.Embed(description=output)
				await bot.send_message(guild.get_channel("452213143926734859"),embed=embed)
				output = ""
				embedSent = True

	goingList = getLines(dataFiles["go"])
	goingString = goingList[0]
	going = guild.get_member(str(goingString))
	output += going.display_name+" is going."
	if not embedSent:
		embed = discord.Embed(title="List:",description=output)
	else:
		embed = discord.Embed(description=output)
	await bot.send_message(guild.get_channel("452213143926734859"),embed=embed)

@bot.command(pass_context=True)
async def next(ctx, num: int = 0):
	if num >= 0:
		guild = ctx.message.channel.server
		lines = getLines(dataFiles["list"])
		count = 0
		for line in lines:
			index = line.find("|")
			id = line[:index]
			member = guild.get_member(str(id))
			if member.status == guild.get_member(bot.user.id).status:
				if count == num:
					break
				else:
					count += 1
		if (count+1)%10 == 1:
			await bot.say(member.display_name+" is the "+str(count+1)+"st next online person on the list.")
		elif (count+1)%10 == 2:
			await bot.say(member.display_name+" is the "+str(count+1)+"nd next online person on the list.")
		elif (count+1)%10 == 3:
			await bot.say(member.display_name+" is the "+str(count+1)+"rd next online person on the list.")
		else:
			await bot.say(member.display_name+" is the "+str(count+1)+"th next online person on the list.")

@bot.command(pass_context=True)
async def listinsert(ctx, pos: int, user: discord.Member):
	if canEditList(ctx.message.author):
		if not inlist(user.id):
			lines = getLines(dataFiles["list"])
			if "\\" in str(user.display_name.encode('unicode_escape')):
				index = str(user.display_name.encode('unicode_escape')).find("\\")
				name = str(user.display_name.encode('unicode_escape'))[2:index]
			else:
				name = user.display_name
			lines.insert(pos-1,user.id+"|"+name+"\n")
			f = open(dataFiles["list"], "w")
			f.writelines([item for item in lines if not item.isspace()])
			f.close()
			await bot.say(user.display_name+" has been inserted into the list at position "+str(pos)+".")
		else:
			await bot.say(user.display_name+" is already on the list. Please remove them first.")

@bot.command(pass_context=True)
async def listlocate(ctx, user: discord.Member = None):
	if user == None:
		user=ctx.message.author
	lines = getLines(dataFiles["list"])
	temp = 0
	pos = 0
	for line in lines:
		temp += 1
		if user.id in line:
			pos = temp
			break
			
	message = ""
	if pos > 0:
		message = " is in position " + str(pos) + " on the list."
	else:
		message = " is not on the list."
	await bot.say(user.display_name + message)

@bot.command(pass_context=True)
async def setgo(ctx, user: discord.Member):
	if canEditList(ctx.message.author):
		file = open(dataFiles["go"], "w")
		file.write(user.id)
		file.close()
		await bot.say(user.display_name + " has been set as going.")

@bot.command(pass_context=True)
async def whogo(ctx):
	guild = ctx.message.channel.server
	lines = getLines(dataFiles["go"])
	await bot.say(guild.get_member(lines[0]).display_name + " is going.")

@bot.command(pass_context=True)
async def listpos(ctx, pos: int):
	guild = ctx.message.channel.server
	lines = getLines(dataFiles["list"])
	index = lines[pos-1].find("|")
	nums = lines[pos-1][:index]
	name = guild.get_member(str(nums)).display_name
	await bot.say(name+" is in position "+str(pos)+" on the list.")

@bot.command(pass_context=True)
async def onlinelocate(ctx, user: discord.Member = None):
	guild = ctx.message.channel.server
	if user == None:
		user = ctx.message.author
	lines = getLines(dataFiles["list"])
	count = 1
	for line in lines:
		index = line.find("|")
		id = line[:index]
		member = guild.get_member(str(id))
		if member.status == guild.get_member(bot.user.id).status:
			if user.id in line:
				break
			else:
				count += 1
	if member.display_name != user.display_name:
		await bot.say(user.display_name+" is not on the list.")
	elif count%10 == 1:
		await bot.say(user.display_name+" is the "+str(count)+"st next online person on the list.")
	elif count%10 == 2:
		await bot.say(user.display_name+" is the "+str(count)+"nd next online person on the list.")
	elif count%10 == 3:
		await bot.say(user.display_name+" is the "+str(count)+"rd next online person on the list.")
	else:
		await bot.say(user.display_name+" is the "+str(count)+"th next online person on the list.")

@bot.command(pass_context=True)
async def listdebug(ctx, state: bool):
	if "219260963268984832" in ctx.message.author.id:
		global listDebugState 
		listDebugState = state


@bot.event
async def on_message(message):

	user = message.author
	m = message.content.lower()
	lines = getLines(dataFiles["help"])

	if not inhelp(user.id) and len(m) <= 50:
		responses = []
		
		if "how" in m and "ascend" in m and ("do" in m or "can" in m):
			responses.append("HowToAscend")
		if "what" in m and ("ascension" in m or "ascending" in m) and ("is" in m or "does" in m):
			responses.append("WhatIsAscension")
		if "how" in m and ("join" in m or "hand" in m or "get in" in m or "enter" in m or ("create" in m and "account" in m)) and "joined" not in m and "joining" not in m and ("can" in m or "do" in m) and "hole" not in m:
			responses.append("HowToJoinChurch")
		if "how" in m and "hole" in m and ("get in" in m or "enter" in m or "work" in m) and ("do" in m or "can" in m):
			responses.append("HowToEnterHole")
		if "how" in m and "hole" in m and ("get out" in m or "leave" in m or "long" in m) and ("do" in m or "can" in m):
			responses.append("HowToGetOut")
		if ("how" in m or "what" in m) and "guardian" in m and ("do" in m or "is" in m or "are" in m):
			responses.append("WhatIsGuardian")
		if "help " in m and "email" in m and "is" in m:
			responses.append("WhatIsSupportEmail")
		if "change" in m and "avatar" in m and ("do" in m or "can" in m):   
			responses.append("HowToChangeAvatar")
		if ("should" in m or "do " in m or "can " in m) and ("click" in m or "touch" in m) and "candle" in m and "not" not in m:
			responses.append("ShouldIClickCandle")
		if "what" in m and "candle" in m and "happens" not in m:
			responses.append("WhatIsCandle")
		if "what" in m and "hole" in m and ("is" in m or "does" in m):
			responses.append("WhatIsHole")
		if "how" in m and ("get" in m or "earn" in m or "gain " in m or "receive" in m) and ("points" in m or "dedication" in m or "loyalty" in m or "faith" in m) and ("do" in m or "does" in m or "can" in m):
			responses.append("HowToEarnPoint")
		if ("will" in m or "is" in m) and ("be" in m or "potential" in m) and "chat" in m and "there" in m:
			responses.append("IsThereAChat")
		if "change" in m and "signature" in m and ("do" in m or "can" in m):
			responses.append("HowToChangeSignature")
		if "what" in m and "candle" in m and "happens" in m:
			responses.append("WhatHappensToCandle")
		if "what" in m and "are" in m and "whispers" in m:
			responses.append("WhatAreWhispers")
		if "what" in m and ("is" in m or "are" in m) and "popcoin" in m:
			responses.append("WhatIsPopcoin")
		if "what" in m and ("is" in m or "are" in m) and ("points" in m or "dedication" in m or "loyalty" in m or "faith" in m):
			responses.append("WhatArePoints")
		if "what is love" in m:
			responses.append("WhatIsLove")
		if "when" in m and ("floor" in m or "accepted" in m):
			responses.append("WhenWillIBeAccepted")
		if "what" in m and ("get" in m or "receive" in m or "earn" in m) and "ascend" in m:
			responses.append("WhatIsAscension")
		if "what" in m and "vip" in m:
			responses.append("WhatIsVip")
		if "can" in m and "see" in m and ("click" in m or "touch" in m) and "candle" in m:
			responses.append("WhoClicked")
		if "what" in m and "self" in m and "destruct" in m:
			responses.append("WhatIsSelfDestruct")
		if "what" in m and "hand" in m and ("is" in m or "do" in m):
			responses.append("WhatIsHand")
		if "what" in m and ("happens" in m or ("do" in m and ("get" in m or "receive" in m or "earn" in m))) and ("leave" in m or "leaving " in m) and "hole" in m:
			responses.append("WhatIsResultOfLeaving")
		if "what" in m and "countdown" in m and ("do" in m or "for" in m):
			responses.append("WhatIsCountDown")
		if "what" in m and "phone number" in m:
			responses.append("WhatIsPhoneNumber")
		if "339567608338710530" in m and "love" in m and "you" in m:
			responses.append("Loveyou")
		if "where" in m and "is" in m and "candle" in m:
			responses.append("WhereIsTheCandle")
		if "who" in m and "is" in m and "poppy" in m:
			responses.append("WhoIsPoppy")
		if "what" in m and "is" in m and "poppy.church" in m:
			responses.append("WhatIsPoppyChurch")
		
		"""Special FAQ"""
		if ("we" in m or "i" in m) and " not in a cult" in m:
			await bot.send_message(message.channel,message.content)
		if "would you wear it" in m:
			await bot.send_message(message.channel,"Wear a carrot?")
		
		for answer in responses:
			await send(message, user, faqMessages[GetUserLanguage(user.id)][answer])
				
	await bot.process_commands(message)

@bot.event
async def on_member_remove(member):
	if inlist(member.id):
		lines = getLines(dataFiles["list"])
		file = open(dataFiles["list"], "w")
		file.writelines([item for item in lines if member.id not in item and not item.isspace()])
		file.close()
		print(member.display_name+" removal processed.")

initializeDataFiles()
bot.run(getLines(dataFiles["token"])[0])