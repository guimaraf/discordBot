#coding: utf-8
import discord, json, requests, random
token = open('tk.dan', 'r').read()
jsonStringsanTexts = json.load(open('data.json', encoding='utf-8'))
functionsStrings = json.load(open('reservWords.json', encoding='utf-8'))
ignoreUser = 'TGM_BOT#5835'
client = discord.Client()

@client.event
async def on_message(message):
    versionBot = '0.2.5'
    global jsonStringsanTexts
    contWords = 0
    msg = ''
    if message.author == client.user:
        return

    if message.author != ignoreUser:
        try:
            msg = eval(message.content)
            await client.send_message(message.channel, msg)
            msg = 'Operação solicitada por {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)
        except:
            for itemIndex in functionsStrings:
                if contWords < 1:
                    if itemIndex in message.content.lower():
                        contWords = 1
                        if 'bitcoin' in message.content.lower() or 'btc' in message.content.lower():
                            await client.send_message(message.channel, 'O valor atual do Dólar é R$' + str(CurrentDollarValue()) + ' '.format(message))
                            await client.send_message(message.channel, 'O valor do Bitcoin em Dólar é $ ' + str(BtcCurrent(jsonCurrency)) + ' '.format(message))
                            msg = 'O valor do Bitcoin em Reais é R$ ' + str(round(CalculateBitcoinToReal(), 2)) + ''.format(message)
                            await client.send_message(message.channel, msg)
                            msg = 'Requisição do feita por {0.author.mention}'.format(message)
                        
                        elif "meme" in message.content.lower():
                            msg = RandomImage()  + ' {0.author.mention}'.format(message)
                        
                        elif "piada" in message.content.lower():
                            msg = RandomJoker()  + ' {0.author.mention}'.format(message)
                        
                        elif "/ajuda" in message.content.lower() or "/help" in message.content.lower():
                            await client.send_message(message.channel, 'Boot desenvolvido por Frederico Oliveira, versão' + versionBot + ' '.format(message))
                            msg = HelpBot()  + 'Informações de ajuda solicitada por {0.author.mention}'.format(message)

                        elif "enquete jam" in message.content.lower():
                            temasJson = json.load(open('temasJam.json', encoding='utf-8'))
                            await client.send_message(message.channel, 'Escolha o tema da Jam com emoji na opção que mais gostar.'.format(message))
                            await client.send_message(message.channel, 'Para manter um ambiente democrático, não vote em mais de 1 "uma" opção'.format(message))
                            contTemas = 0
                            for i in temasJson:
                                contTemas += 1
                                msg = 'Tema ' +  str(contTemas) + ' ```' + temasJson[i] + '``` '
                                await client.send_message(message.channel, msg)
                            msg = 'Requisição da enquete feita por {0.author.mention}'.format(message)
                                
                        elif "newCurrency" in message.content.lower():
                            NewCurrency()
                            msg = "Atualizado cotação " + BtcCurrent(jsonCurrency) + ' {0.author.mention}'.format(message)
                        await client.send_message(message.channel, msg)
                        break
        
        if contWords == 0:
            messagerDiscord = ''
            result = Words(message.content, jsonStringsanTexts, messagerDiscord)
            if result != '':
                msg = result + ' {0.author.mention}'.format(message)
                await client.send_message(message.channel, msg)
                messagerDiscord = ""

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def Words(discordString, json, msgDiscord):
    for item in json:
        if item in discordString.lower():
            msgDiscord = json[item]
    return msgDiscord

def RandomImage():
    lines = open('imagens.txt', 'r').read().splitlines()
    lines = random.choice(lines)
    return 'https://i.imgur.com/' + lines
    lines.close()

def RandomJoker():
    lines = open('piadaProgramacao.txt', 'r').read().splitlines()
    lines = random.choice(lines)
    return 'https://i.imgur.com/' + lines
    lines.close()

def BtcCurrent(jsonValues):
    return jsonValues['bpi']['USD']['rate']

def NewCurrency():
    try:
        jsonCriptoSource = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
        jsonText = json.loads(jsonCriptoSource.text)
        return jsonText
    except Exception as e:
        return "Erro ao acessar a API de criptomoedas"

def HelpBot():
    fileHelpBot = open('help.txt', 'r', encoding='utf-8').read()
    return fileHelpBot
    fileHelp.close()

def CurrentyValueRequestAPI():
    try:
        req = requests.get("https://economia.awesomeapi.com.br/json/USD-BRL/1")
        resposta = json.loads(req.text)
        return resposta[0]['high']
    except:
        return (" ")

def CurrentDollarValue():
    if dollarVallueBr == ' ':
        return ' '
    else:
        return dollarVallueBr

def CalculateBitcoinToReal():
    a = float(dollarVallueBr)
    b = float(BtcCurrent(jsonCurrency).replace(',' , ''))
    return a * b

jsonCurrency = NewCurrency()
dollarVallueBr = CurrentyValueRequestAPI()
print(dollarVallueBr)
client.run(token)