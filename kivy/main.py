from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
#from pygments.lexers import HtmlLexer

from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class MyApp (App):
    def build(self):
        width= '380'
        height= '280'
        #return CodeInput(Lexer = HtmlLexer())

        Config.set('graphics', 'resizable', '0');
        Config.set('graphics', 'width', '380');
        Config.set('graphics', 'height', '280');

        s = Scatter()
        f1 = FloatLayout(size = (300, 300))
        s.add_widget(f1)
        f1.add_widget(Button(text = '!!!',
                      font_size = 30,
                      on_press = self.btn_press,
                      background_color = [0.1, 0.9, 0.5, 1],
                      background_normal = '',
                      size_hint = (.5, .25),
                      pos = (int(height)/2 - int(height)/8,
                             int(width) / 2 - int(width)/8)
                      ));
        return s#f1

    def btn_press(self, instance):
        print('Buton is pressed!')
        instance.text = 'Hello User!'
        #instance.exit

if __name__ == '__main__':
    MyApp().run()