from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.lang import Builder


class LoginLayout(GridLayout):
    def __init__(self, **kwargs):
        super(LoginLayout,self).__init__(**kwargs)
        self.cols = 1
        self.login()

    def register(self):
        self.clear_widgets()
        self.add_widget(Label(text = "Friends +", font_size = 40))
        name_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Name", name_input))
        email_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Email", email_input))
        password_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Password", password_input))
        self.add_widget(self.form_sumbit())
    def login(self):
        self.clear_widgets()
        self.add_widget(Label(text = "Friends +", font_size = 40))
        name_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Name", name_input))
        email_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Email", email_input))
        password_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Password", password_input))
        self.add_widget(self.form_sumbit(False))

    def form_sumbit(self,register = True):
        lay = GridLayout(cols = 2)
        if register:
            lay.add_widget(Button(text="Register", font_size=30))
            lay.add_widget(Button(text="Login",font_size = 30,size_hint = (0.5,1)))
        else:
            lay.add_widget(Button(text="Register", font_size=30,size_hint = (0.5,1)))
            lay.add_widget(Button(text="Login",font_size = 30))
        return lay



    def form_input(self, name, inp):
        lay = GridLayout(cols = 2)
        lay.size_hint = (0.5,1)
        lay.add_widget(Label(text = f"{name}: ",font_size=20,size_hint= (0.5,1)))
        lay.add_widget(inp)
        return lay




class MyApp(App):
    def build(self):
        return LoginLayout()

if __name__ == "__main__":
    app_var = MyApp()
    app_var.run()
