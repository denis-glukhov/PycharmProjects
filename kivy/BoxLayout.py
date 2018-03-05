from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        bl= BoxLayout(orientation = 'vertical', spacing = 60, padding = [10, 50, 200, 10])
        bl.add_widget(Button(text = "Button #1"))
        bl.add_widget(Button(text = "Button #2"))
        bl.add_widget(Button(text = "Button #3"))
        bl.add_widget(Button(text = "Button #4"))
        bl.add_widget(Button(text = "Button #5"))
        return bl


if __name__ == '__main__':
    MyApp().run()
