from guizero import App, PushButton

def do_nothing():
    print("Nothing happend")

app = App (title="Keypad Example", width=100, height=90, layout="grid")
button1 = PushButton(app, command=do_nothing, text="1", grid=[0,0])
button2 = PushButton(app, command=do_nothing, text="2", grid=[1,0])
button3 = PushButton(app, command=do_nothing, text="3", grid=[2,0])
button4 = PushButton(app, command=do_nothing, text="4", grid=[0,1])
button5 = PushButton(app, command=do_nothing, text="5", grid=[1,1])
button6 = PushButton(app, command=do_nothing, text="6", grid=[2,1])
app.display()
