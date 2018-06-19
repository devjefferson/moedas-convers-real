import urllib.request



content = urllib.request.urlopen("https://bithoje.com/bitcoin-hoje/").read()
content = str(content)
find = '<input type="text" id="real" value="'
posicao = int(content.index(find) + len(find))
bitcoin = content[ posicao : posicao + 8]
bitcoin = bitcoin.replace(",",'.')
valorint = float(bitcoin)

print('BITCOIN: {}'.format(valorint))


content = urllib.request.urlopen("https://bithoje.com/litecoin-hoje/").read()
content = str(content)
find = '<input type="text" id="real" value="'
posicao = int(content.index(find) + len(find))
litecoin = content[ posicao : posicao + 6]
litecoin = litecoin.replace(",",'.')
valorltc = float(litecoin)

print('LITECOIN: {}'.format(valorltc))

content = urllib.request.urlopen("https://bithoje.com/dogecoin-hoje/").read()
content = str(content)
find = '<input type="text" id="real" value="'
posicao = int(content.index(find) + len(find))
dogecoin = content[ posicao : posicao + 7]
doge2 = dogecoin.replace(",",'.')
valordge = float(doge2)

print('DOGECOIN: {}'.format(valordge))

content = urllib.request.urlopen("https://bithoje.com/iota-hoje/").read()
content = str(content)
find = '<input type="text" id="real" value="'
posicao = int(content.index(find) + len(find))
iota = content[ posicao : posicao + 3]
iota2 = iota.replace(",",'.')
valoriota = float(iota2)

print('IOTA: {}'.format(valoriota))

content = urllib.request.urlopen("https://bithoje.com/nem-hoje/").read()
content = str(content)
find = '<input type="text" id="real" value="'
posicao = int(content.index(find) + len(find))
nem = content[ posicao : posicao + 4]
nem2 = nem.replace(",",'.')
valornem = float(nem2)

print('NEM: {}'.format(valornem))


#Dinheiro

content = urllib.request.urlopen("https://www.dolarhoje.net.br/").read()
content = str(content)
find = '<input type="text" id="moeda" value="'
posicao = int(content.index(find) + len(find))
dolar = content[ posicao : posicao + 4]
dolar2 = dolar.replace(",",'.')
valordolar = float(dolar2)

print('Dolar: {}'.format(valordolar))


content = urllib.request.urlopen("https://www.dolarhoje.net.br/euro-hoje/").read()
content = str(content)
find = '<input type="text" id="moeda" value="'
posicao = int(content.index(find) + len(find))
euro = content[ posicao : posicao + 4]
euro2 = euro.replace(",",'.')
valoreuro = float(euro2)

print('Euro: {}'.format(valoreuro))
