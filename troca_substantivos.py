# Programa de Teste: Substituindo substantivos utilizando spaCy
# Autor: Pablo

# Descrição: Utilizando dois arquivos, é realizada a troca dos substantivos
# do primeiro pelos substantivos do segundo, seguindo o exemplo do artigo
# em que os substantivos foram substituidos pelos de outro texto.
# O programa ainda precisa ser lapidado, e no momento utilza a biblioteca
# spaCy para analisar quais palavras são substantivos, para realizar a troca.


# Importando bibliotecas necessárias e criando o analisador

import spacy
from spacy.en import English
nlp = English()
print("English: OK")

# Criando o arquivo que será editado:

file = open("/projetos/new.txt","w")
file.write("Hello world. This is my testing text. Well, I'll be using this document to try some Oulipo restrictions games")
file.close()

# Lendo o arquivo e armazenando-o em uma string:

file = open("/projetos/new.txt","r")
unparsedText = str(file.read())
file.close()

# Criando arquivo para ser realizada a troca de substantivos

file = open("/projetos/new2.txt","w")
file.write("Some new NOUNS: mouse, horse, wall, table, shark and book")
file.close()

# Lendo o arquivo e armazenando-o em uma string:

file = open("/projetos/new2.txt","r")
unparsedData = str(file.read())
file.close()

# Criando dados analisados:

parsedData = nlp(unparsedText)
parsedData2 = nlp(unparsedData)

# Criando uma lista de substantivos a partir do segundo arquivo

nouns = []

for token in parsedData2:
	if(token.pos_ == "NOUN"):
		nouns.append(token.orth_)

# Aplicando substantivos do segundo arquivo no primeiro:

newSentence = " "
j = 0
for token in parsedData:
	if(token.pos_ != "NOUN"):
		newSentence = newSentence + " " + token.orth_
	else:
		for i in range (0, 6):
			newSentence = newSentence + " " + nouns[j]
			j = j + 1
			break

# Comparando as sentenças:

print(parsedData)
print(parsedData2)
print(newSentence)

# Salvando o texto em um arquivo:

file = open("/projetos/final.txt","w")
file.write(newSentence)
file.close()
