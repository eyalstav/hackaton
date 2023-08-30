import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.lang import Builder
import json

from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.textfield import MDTextField
import requests


class WindowManager(ScreenManager):
    pass
class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass

class SearchTextInput(MDTextField):

    def on_text(self, instance, value):
        self.get_issues_from_db_by_value(value)

    def get_issues_from_db_by_value(self, value):
        option_list = get_issues_text_from_db()
        app = MDApp.get_running_app()
        option_list = list(set(option_list + value[:value.rfind(' ')].split(' ')))
        val = value[value.rfind(' ') + 1:]
        if not val:
            return
        try:
            app.option_data = []
            for i in range(len(option_list)):
                word = [word for word in option_list if word.startswith(val)][0][len(val):]
                if not word:
                    return
                if self.text + word in option_list:
                    if self.text + word not in app.option_data:
                        popped_suggest = option_list.pop(option_list.index(str(self.text + word)))
                        app.option_data.append(popped_suggest)
                app.update_data(app.option_data)

        except IndexError:

            pass


def get_issues_text_from_db():
    res = requests.get(
        'https://communityconnect1234-default-rtdb.europe-west1.firebasedatabase.app/Billboard.json')
    billboard_db_data = res.json()
    option_list = ""
    if billboard_db_data is not None:
        for dictionary in billboard_db_data:
            option_list += dictionary
            option_list += ","
        option_list = option_list.split(',')
    return option_list

class Search_Select_Option(OneLineAvatarIconListItem):
    def show_issue(self):
        pass
        # show issue screen

import requests
from SOS import *

logged_in = False
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
                global logged_in
                logged_in = True
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


class AppLayout(GridLayout):
    def __init__(self, **kwargs):
        super(AppLayout,self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(LoginLayout())





        self.add_widget(self.nav_bar())

    def change_map(self,shit):
        if logged_in:
            print("hioo")
            self.clear_widgets()
            self.add_widget(Map())
            self.add_widget(self.nav_bar())

    def change_sos(self,shit):
        if logged_in:
            print(shit)
            self.clear_widgets()
            self.add_widget(SOS_Form())
            self.add_widget(self.nav_bar())
    def change_billboard(self,shit):
        if logged_in:
            self.clear_widgets()
            self.add_widget(Builder.load_file("project.kv"))
            self.add_widget(self.nav_bar())


    def nav_bar(self):
        lay = GridLayout(cols = 3,size_hint=(1,0.2))
        self.sos_btn = Button(text="BillBoard")
        self.sos_btn.bind(on_press = self.change_billboard)
        lay.add_widget(self.sos_btn)
        self.bill_btn = Button(text="Map",size_hint = (0.7,1))
        self.bill_btn.bind(on_press = self.change_map)
        lay.add_widget(self.bill_btn)
        self.sos_btn = Button(text="SOS!")
        self.sos_btn.bind(on_press = self.change_sos)
        lay.add_widget(self.sos_btn)
        return lay

class MainApp(GridLayout):
    def __init__(self, **kwargs):
        super(MainApp,self).__init__(**kwargs)
        app = AppLayout()
        self.add_widget(app)
        self.clear_widgets()
        self.add_widget(AppLayout())

class MyApp(MDApp):
    def build(self):
        return AppLayout()

    rv_data = ListProperty()

    def reset_data_to_default(self):
        self.rv_data = [{'text': item} for item in get_issues_text_from_db()]

    def update_data(self, rv_data_list):
        self.rv_data = [{'text': item} for item in rv_data_list]
        print(self.rv_data, 'update')

    def erase(self):
        self.reset_data_to_default()

    def search(self):
        pass

    def insert_issue_to_db(self, topic, description):
        if len(topic) > 1 and description != "":
            print(topic + "," + description)
            # patch db
            res = requests.patch(
                'https://communityconnect1234-default-rtdb.europe-west1.firebasedatabase.app/Billboard.json',
                data=json.dumps({topic: {'description': description}}))
        pass


if __name__ == "__main__":
    app_var = MyApp()
    app_var.run()