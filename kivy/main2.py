from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):
        bl= GridLayout(rows = 7, cols =7, padding= [30], spacing = 30)
        for row in range (9):
            bl.add_widget(Button(text=("Button #"+str(row+1))))
        return bl


if __name__ == '__main__':
    MyApp().run()
