import json

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

import requests


class LoginLayout(GridLayout):
    def __init__(self, **kwargs):
        super(LoginLayout, self).__init__(**kwargs)
        self.cols = 1
        self.login("Fsdsda")

    def register(self,shit):
        self.clear_widgets()
        self.add_widget(Label(text="Friends +", font_size=40))
        self.name_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Name", self.name_input))
        self.phone_number_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Phone Number", self.phone_number_input))
        self.password_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Password", self.password_input))
        self.add_widget(self.form_sumbit())

    def login(self,shit):
        self.clear_widgets()
        self.add_widget(Label(text="Friends +", font_size=40))
        self.name_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Name", self.name_input))
        self.phone_number_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Phone Number", self.phone_number_input))
        self.password_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Password", self.password_input))
        self.add_widget(self.form_sumbit(False))

    def submit_login(self,shit):
        res = requests.get("https://communityconnect1234-default-rtdb.europe-west1.firebasedatabase.app/Users.json")
        all_users = dict(res.json())
        for key,val in all_users.items():
            val = dict(val)
            if val["name"] == self.name_input.text and val["password"] == self.password_input.text:
                print("Logged in to", self.name_input.text)


    def submit_register(self,shit):
        data = {self.phone_number_input.text: {"name": self.name_input.text,"password":self.password_input.text}}
        res = requests.patch("https://communityconnect1234-default-rtdb.europe-west1.firebasedatabase.app/Users.json",
                             json.dumps(data))
        print(res.content)

    def form_sumbit(self, register=True):
        lay = GridLayout(cols=1)
        if register:
            lay.add_widget(Label())
            reg_btn = Button(text="Register", font_size=30, size_hint=(0.5, 2))
            reg_btn.bind(on_press = self.submit_register)
            lay.add_widget(reg_btn)
            lay.add_widget(Label())
            log_btn = Button(text="already have an account? Log in", font_size=20, size_hint=(0.5, 2))
            log_btn.bind(on_press = self.login)
            lay.add_widget(log_btn)
        else:
            lay.add_widget(Label())
            log_btn = Button(text="Login", font_size=30, size_hint=(0.5, 2))
            log_btn.bind(on_press = self.submit_login)
            lay.add_widget(log_btn)
            lay.add_widget(Label())
            reg_btn = Button(text="new? Sign Up!", font_size=20, size_hint=(0.5, 2))
            reg_btn.bind(on_press = self.register)
            lay.add_widget(reg_btn)
        return lay

    def form_input(self, name, inp):
        lay = GridLayout(cols=1)
        lay.size_hint = (0.5, 1)
        lay.add_widget(Label(text=f"{name}: ", font_size=20, size_hint=(0.5, 1)))
        lay.add_widget(inp)
        return lay

    def sub_to_database(self):
        data = {self.name_input: {"phone": self.phone_number_input.text,
                                  "password": self.password_input.text}}
        print(data)
        return data


class MyApp(App):
    def build(self):
        return LoginLayout()


if __name__ == "__main__":
    app_var = MyApp()
    app_var.run()
