# Programa que gera poemas com a mesma estrutura
# O arquivo utilizado como banco de palavras foi criado manualmente a partir
# de um artigo científico aleatório

# Importação de bibliotecas utilizadas e criação dos dados analizados
import spacy
import random
from spacy.en import English
nlp = English()

path = "/Projetos/abc.txt"
with open(path, "r+") as file:
    parsedText = nlp(file.read())

# Declarando as arrays em que serão armazenadas cada tipo de dados
arrayAdj = []
arrayAdp = []
arrayAdv = []
arrayConj = []
arrayDet = []
arrayNoun = []
arrayPron = []
arrayPropn = []
arrayPunct = []
arrayVerb =[]

#Aramazenando as palavras em suas devidas arrays
for token in parsedText:
        # exist é utilizada para que não haja repetições de palavras nas arrays
	exist = 0
	# Há, para cada token, uma verificação de seu tipo,
	# para determinar em que array será armazenado
	if(token.pos_ == "ADJ"):
                # em cada verificação há um "for" para verificar se o token
                # já não foi armazenado em sua respectiva array
		for i in range(0, len(arrayAdj)):
                        # se houver dentro da array uma string identica ao token
                        # o valor de exist será alterado para 1e em seguida sairá do laço
			if(arrayAdj[i] == token.orth_):
				exist = 1
				break;
		# Após a verificação feita pelo laço, verifica o valor de exist
		# para dereminar se o token pode ou não ser armazenado na array
		if(exist == 0):
			arrayAdj.append(token.orth_)

		# Após isso, para garantir que não haverão problemas nos demais
		# tokens, o valor de exist torna a ser 0
		exist = 0
		
	if(token.pos_ == "ADP"):
		for i in range(0, len(arrayAdp)):
			if(arrayAdp[i] == token.orth_):
				exist = 1
				break;
		if(exist == 0):
			arrayAdp.append(token.orth_)
			
		exist = 0
	if(token.pos_ == "ADV"):
		for i in range(0, len(arrayAdv)):
			if(arrayAdv[i] == token.orth_):
				exist = 1
				break;
		if(exist == 0):
			arrayAdv.append(token.orth_)
			
		exist = 0
	if(token.pos_ == "CONJ"):
		for i in range(0, len(arrayConj)):
			if(arrayConj[i] == token.orth_):
				exist = 1
				break;
		if(exist == 0):
			arrayConj.append(token.orth_)
			
		exist = 0
	if(token.pos_ == "DET"):
		for i in range(0, len(arrayDet)):
			if(arrayDet[i] == token.orth_):
				exist = 1
				break;
		if(exist == 0):
			arrayDet.append(token.orth_)
			
		exist = 0
	if(token.pos_ == "NOUN"):
		for i in range(0, len(arrayNoun)):
			if(arrayNoun[i] == token.orth_):
				exist = 1
				break;
		if(exist == 0):
			arrayNoun.append(token.orth_)
			
		exist = 0
	if(token.pos_ == "PRON"):
		for i in range(0, len(arrayPron)):
			if(arrayPron[i] == token.orth_):
				exist = 1
				break;
		if(exist == 0):
			arrayPron.append(token.orth_)
			
		exist = 0
	if(token.pos_ == "PROPN"):
		for i in range(0, len(arrayPropn)):
			if(arrayPropn[i] == token.orth_):
				exist = 1
				break;
		if(exist == 0):
			arrayPropn.append(token.orth_)
			
		exist = 0
	if(token.pos_ == "PUNCT"):
		for i in range(0, len(arrayPunct)):
			if(arrayPunct[i] == token.orth_):
				exist = 1
				break;
		if(exist == 0):
			arrayPunct.append(token.orth_)
			
		exist = 0
	if(token.pos_ == "VERB"):
		for i in range(0, len(arrayVerb)):
			if(arrayVerb[i] == token.orth_):
				exist = 1
				break;
		if(exist == 0):
			arrayVerb.append(token.orth_)
			
		exist = 0

# Após armazernar as palavras em suas arrays é necessario criar a estrutura do poema
# Por agora, a estrutura foi retirada do modelo de "PoemGen", um software que gera
# poemas, escrito em JavaScript, que utiliza um padrão simples de compreender:
poemSentence = "The 5 1 6 3 the 1 ."+"// 5, 5 1 6 3 a 5, 5 1 ."+"// 2 is a 5 1 ."+"// 1 4 !"+"// The 1 4 like a 5 1 ."+"// 1 4 like 5 1 ."+"// Why does the 1 4 ?"+"// 4 6 like a 5 1 ."+"// 2, 2, and 2 ."+"// Where is the 5 1 ?"+"// All 1 3 5, 5 1s ."+"// Never 3 a 1 ."
for j in range(1, 3):
    # A Sentença escolhida deve ser tokenizada, para então criar um poema:
    parsedPoem = nlp(poemSentence)
    poem = ""
    for token in parsedPoem:
            if(token.pos_ == "NUM"):
                    if(token.orth_ == "1" or token.orth_ == "2"):
                            poem = poem + " " + random.choice(arrayNoun)
                    if(token.orth_ == "3" or token.orth_ == "4"):
                            poem = poem + " " + random.choice(arrayVerb)
                    if(token.orth_ == "5"):
                            poem = poem + " " + random.choice(arrayAdj)
                    if(token.orth_ == "6"):
                            poem = poem + " " + random.choice(arrayAdv)
            else:
                    poem = poem + " " + token.orth_

    # Os números das sentenças são substituidos por alguma palavra aleatória de
    # determinada array:
    # Números 1 e 2: Substantivos (arrayNoun)
    # Números 3 e 4: Verbos (arrayVerb)
    # Número 5: Adjetivos (arrayAdj)
    # Número 6: Advérbios (arrayAdv)
    # Caso não seja um numero, e sim uma palavra, a palavra será incluida em "poem"

    # 1 e 2 são usados para substantivos e 3 e 4 para verbos, pois segui o modelo
    # do "PoemGen", e ele separa Substantivos concretos(1) de abstratos(2)
    # assim como verbos transitivos(3) de intransitivos(4)
    # Como ainda não sei se é possivel fazer essa separação com a spacy,
    # Apenas mantive o padrão da sentença do "PoemGen" e
    # adaptei o uso do meu banco de palavras.

    print(poem)
