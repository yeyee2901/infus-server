#Push botton
from guizero import App,Text,PushButton

#text=Text(app,text="Timbangan Infus Digital", font='arial', size=16, color='blue')

def say_hello():
    text.value = "Hello World"
    
#    text=Text(app,text="I clicked it")

app = App()
text = Text(app)
button=PushButton(app,command=say_hello)
app.display()
