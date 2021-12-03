from guizero import App, Window, Text, PushButton

def open_window():
    window.show()

def close_window():
    window.hide()

app = App(title="Main Window")

window = Window(app, title = "2nd Window")
#menampilkan kata text pada 2nd window
text = Text(window, text="text")
#2nd window akan disembunyikan terlebih dahulu
window.hide()

#membuat push botton
open_button = PushButton(app, text="Open", command=open_window)
close_button = PushButton(window, text="Close", command=close_window)

app.display()
