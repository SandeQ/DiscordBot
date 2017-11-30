import requests, discord, asyncio, re
from discord.ext import commands

client = discord.Client()

@client.event
async def on_message(message):
    #taking nickname from command to pass it to request later
    nickname = message.content.partition("/serwer ")[2]

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # we want to get the info about the last server where the nickname been
    if message.content.startswith('/serwer {0}'.format(nickname)):
        #connecting to API
        RAW_API_CHAMPS_DATA = requests.get("https://nightfirec.at/realmeye-api/?player={0}&filter=player+characters+class+last_server".format(nickname))
        #taking JSON data from the API
        JSON_CHAMPS_DATA = RAW_API_CHAMPS_DATA.json()
        #taking the server, which was recently used by nickname[when switching characters, it moves to forst position on charlist]
        srv = JSON_CHAMPS_DATA['characters']['class' == 0]['last_server']
        #setting the msg where the nickname is playing now/was playing last time
        msg = 'Cześć, '+nickname+' znajduje się na serwerze '+srv+', wbijaj ziomuś! JP2GMD '.format(message)
        #telling the app we want to send the message to server asynchronously, allowing other user to do the command in the same time
        await client.send_message(message.channel, msg)
        #DEBUG TEXT
        print("ok")
    elif message.content.startswith('jebacdisa'):
        #setting the message
        msg = 'SYNA DIABŁA!'.format(message)
        #telling app to send it async
        await client.send_message(message.channel, msg)
        #DEBUG TEXT
        print("jd")
    elif message.content.startswith('prowadzący to?'):
        #setting the message
        msg = 'PIZDA!'.format(message)
        #telling the app to send it async
        await client.send_message(message.channel, msg)
        #DEBUG TEXT
        print("bronzowe")


@client.event
#showing actual login info
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
#starting the discord bot
client.run('')

###just some trash underneath, maybe will be useful in the future

###print(RAW_API_CHAMPS_DATA)
###print(type(JSON_CHAMPS_DATA))
###parsed_json=json.dumps(json_string)
###print(parsed_json["class"])

#RAW_API_CHAMPS_DATA = requests.get("https://nightfirec.at/realmeye-api/?player=kupapookup&filter=player+characters+class+last_server")
#JSON_CHAMPS_DATA=RAW_API_CHAMPS_DATA.json()
#srv = JSON_CHAMPS_DATA['characters']['class'==0]['last_server']
#print(srv)

###test = requests.get("https://discordapp.com/api/v6/users/username", headers={'Authorization': 'Bot MzgzNzM4Mjg5OTcyMTgzMDUx.DPshvg.n6aCnTi6HW8im6LxvQx5jUMQ-kc'})
###json_test=test.json()
###print(json_test)
###name = discord.User.display_name

