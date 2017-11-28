import requests, discord, asyncio
from discord.ext import commands

RAW_API_CHAMPS_DATA = requests.get("https://nightfirec.at/realmeye-api/?player=kupapookup&filter=player+characters+class+last_server")
JSON_CHAMPS_DATA=RAW_API_CHAMPS_DATA.json()
srv = JSON_CHAMPS_DATA['characters']['class'==0]['last_server']
print(srv)

###test = requests.get("https://discordapp.com/api/v6/users/username", headers={'Authorization': 'Bot MzgzNzM4Mjg5OTcyMTgzMDUx.DPshvg.n6aCnTi6HW8im6LxvQx5jUMQ-kc'})
###json_test=test.json()
###print(json_test)
###name = discord.User.display_name

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('/serwer') or message.content.startswith('/server'):
        RAW_API_CHAMPS_DATA = requests.get("https://nightfirec.at/realmeye-api/?player=kupapookup&filter=player+characters+class+last_server")
        JSON_CHAMPS_DATA = RAW_API_CHAMPS_DATA.json()
        srv = JSON_CHAMPS_DATA['characters']['class' == 0]['last_server']
        msg = 'Cześć, gramy na serwerze '+srv+', zapraszamy!'.format(message)
        await client.send_message(message.channel, msg)
        print("ok")
    elif message.content.startswith('jebacdisa'):
        msg = 'SYNA DIABŁA!'.format(message)
        await client.send_message(message.channel, msg)
        print("jd")
    elif message.content.startswith('prowadzący to?'):
        msg = 'PIZDA!'.format(message)
        await client.send_message(message.channel, msg)
        print("bronzowe")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('MzgzNzM4Mjg5OTcyMTgzMDUx.DPsRLg.QgI7BGLX2JInmgejxxRGrDqdhTE')
###print(RAW_API_CHAMPS_DATA)
###print(type(JSON_CHAMPS_DATA))
###parsed_json=json.dumps(json_string)
###print(parsed_json["class"])