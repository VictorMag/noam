from xml.dom import minidom

xmldoc = minidom.parse("Names.xml")
dic = xmldoc.getElementsByTagName("dic")[0]
entrys = dic.getElementsByTagName("entry")

x = []
def StartList():
    for entry in entrys:
        x.append (entry.getElementsByTagName("orth")[0].firstChild.data)
    return x
def getListName():
    for entry in entrys:
        print (entry.getElementsByTagName("orth")[0].firstChild.data)
        x.append (entry.getElementsByTagName("orth")[0].firstChild.data)
    return x
    
def getCompName():
    x = input("entre com um dado \n")
    for entry in entrys:
        a=entry.getElementsByTagName("orth")[0].firstChild.data
        if x == a:
            print (x,"É igual a:", a,"sucesse")
        else:
            print (x,"É diferente de:",a,"fail")
def NMaisSete():
    getListName()
    nome = input("Entre com o nome para o jogo de N+7: \n")
    for y in range(0,len(x)):
        if nome == x[y]:
            print ("Nome escolhido:",x[y],"Setimo nome:",x[(y+7)%len(x)])

def getListDef():
    for entry in entrys:
       print (entry.getElementsByTagName("orth")[0].firstChild.data)
       try:
            print (entry.getElementsByTagName("def")[0].firstChild.data)
       except:
            print ("Não possui definição /n")
def getDic():
    i=0
    for entry in entrys:
        # print(entry.getElementsByTagName("orth")[0].firstChild.data)
        try:
            a = entry.getElementsByTagName("orth")[0].firstChild.data
        except:
            a = "Não possui orth"
        try:
            b = entry.getElementsByTagName("def")[0].firstChild.data
        except:
            b = "Não possui def"
        try:
            c = entry.getElementsByTagName("etym")[0].firstChild.data
        except:
            c = "Não possui origem definida"
        x.extend([[a], [b], [c]])
        print ("Palavra:",a)
        print("Origem:",c)
        print("Definição:",b)

        #print("Palavra:", x[0], "Definição:", x[i],"\n")
        i+=1
        #x.extend([[entry.getElementsByTagName("orth")[0].firstChild.data],[entry.getElementsByTagName("def")[0].firstChild.data]])
def getListEtym():
    for entry in entrys:
        try:
            a = entry.getElementsByTagName("etym")[0].firstChild.data
        except:
            a = "Não possui origem definida"
        print(a)

def NMaisA(n):
    print(n)
    getListName()
    nome = input("Entre com o nome para o jogo de N+Alguma Coisa: \n")
    for y in range(0,len(x)):
        if nome == x[y]:
            print ("Nome escolhido:",x[y],n,"º","nome:",x[(y+n)%len(x)])

NMaisA(10)