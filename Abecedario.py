# Programa que monta uma sentença com base na restrição "Abecedário"

# Importação da biblioteca e ferramentas necessárias
import spacy
from spacy.en import English

#Criação do "parser"
nlp = English()

# O arquivo "abc.txt" já foi criado manualmente na pasta de projetos
# O arquivo contém um trecho de um artigo que fala sobre a técnica de NLP
# conhecida como "Stemmer"
# Basicamente, o programa abre o arquivo e o "tokeniza"
with open("/projetos/abc.txt") as file:
    parsedData = nlp(file.read())

sentence = ""

# E a mágica do "Abecedario" acontece :)
# "i" controla a letra, prefix é a primeira letra do token e orth é a palavra
for i in range(97, 123):
    for token in parsedData:
        if(token.prefix_ == chr(i)):
           sentence = sentence + token.orth_ + " "
           break

print(sentence)

# Futuras implementações: Contruir frase que faça sentido e em forma de poema.

sentencePattern = "DET NOUN ADJ VERB, PRON NOUN VERB"
parsedPattern = nlp(sentencePattern)

sentence = ""

for i in range(97, 123):
    for token in parsedPattern:
        tok = token.orth_
        for token in parsedData:
            if(token.prefix_ == chr(i) and token.pos_ == tok):
                sentence = sentence + token.orth_ + " "
                break
        break

print(sentence)
