from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput

class MyApp (App):
    def build(self):
        return Button(text = 'Это КНОПКА!!!',
                      font_size = 50,
                      on_press = self.btn_press,
                      background_color = [0.1, 0.9, 0.5, 1],
                      background_normal = ''
                      )
    def btn_press(self, instance):
        print("Кнопка нажата")
        instance.text = 'Hello User!'


if __name__ == '__main__':
    MyApp().run()