text= input ("ievadi tekstu: ")
def reverseSentence(text):
  sar1=text.split(";")
  if len(sar1)>2:
    sar1.reverse()
    text = ""
    for elements in sar1:
      text += elements +";"
    print (text)
  else:
    text = "parak iss teikums"
    print (text)
  return text
reverseSentence(text)

