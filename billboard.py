import json

from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.textfield import MDTextField
import requests


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class Search_Select_Option(OneLineAvatarIconListItem):
    def show_issue(self):
        pass
        # show issue screen


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


class RVTestApp(MDApp):
    rv_data = ListProperty()

    def reset_data_to_default(self):
        self.rv_data = [{'text': item} for item in get_issues_text_from_db()]

    def update_data(self, rv_data_list):
        self.rv_data = [{'text': item} for item in rv_data_list]
        print(self.rv_data, 'update')

    def build(self):
        self.reset_data_to_default()
        return Builder.load_file("project.kv")

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


RVTestApp().run()