__author__ = "Ngenge Senior"
__date__  = "July 31 2016"

from  kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
class LoginScreen(GridLayout):
    def __init__(self,**kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text = "User Name:"))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)
        self.add_widget(Label(text = "Email Address"))
        self.email = TextInput(multiline = False)
        self.add_widget(self.email)
        self.add_widget(Label(text = "Password"))
        self.password = TextInput(multiline = False,password = True)
        self.add_widget(self.password)
        self.add_widget(Label(text = "Comments" ))
        self.comments = TextInput(multiline = True)
        self.add_widget(self.comments)
class TestScreenApp(App):
    def build(self):
        title = "Login Screen"
        icon = "sun.gif"
        return LoginScreen()
if __name__ == '__main__':
    TestScreenApp().run()
