from xml.dom import minidom

xmldoc = minidom.parse("Names.xml")

dic = xmldoc.getElementsByTagName("dic")[0]
entrys = dic.getElementsByTagName("entry")

x = []
i=0
for entry in entrys:
    #print(entry.getElementsByTagName("orth")[0].firstChild.data)
    try:
        a = entry.getElementsByTagName("orth")[0].firstChild.data
    except:
        a = "Não possui orth"
    try:
        b = entry.getElementsByTagName("def")[0].firstChild.data
    except:
        b = "Não possui def"
    x.extend([[a],[b]])
    print ("Palavra:",x[i],"Definição:",x[i])
    i+=1
    #x.extend([[entry.getElementsByTagName("orth")[0].firstChild.data],[entry.getElementsByTagName("def")[0].firstChild.data]])
