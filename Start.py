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
        super(LoginLayout, self).__init__(**kwargs)
        self.cols = 1
        self.login()

    def register(self):
        self.clear_widgets()
        self.add_widget(Label(text="Friends +", font_size=40))
        first_name_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("First Name", first_name_input))
        last_name_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Last Name", last_name_input))
        user_name_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Password", user_name_input))
        phone_number_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Email", phone_number_input))
        password_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Password", password_input))
        self.add_widget(self.form_sumbit())

    def login(self):
        self.clear_widgets()
        self.add_widget(Label(text="Friends +", font_size=40))
        self.name_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Name", self.name_input))
        self.email_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Email", self.email_input))
        self.phone_number_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Phone Number", self.phone_number_input))
        self.password_input = TextInput(text="", font_size=20, )
        self.add_widget(self.form_input("Password", self.password_input))
        self.add_widget(self.form_sumbit())

    def form_sumbit(self, register=True):
        lay = GridLayout(cols=1)
        if register:
            lay.add_widget(Label())
            lay.add_widget(Button(text="Register", font_size=30, size_hint=(0.5, 2)))
            lay.add_widget(Label())
            lay.add_widget(Button(text="already have an account? Log in", font_size=20, size_hint=(0.5, 2)))
        else:
            lay.add_widget(Button(text="Register", font_size=30, size_hint=(0.5, 1)))
            lay.add_widget(Button(text="Login", font_size=30))
        return lay

    def form_input(self, name, inp):
        lay = GridLayout(cols=1)
        lay.size_hint = (0.5, 1)
        lay.add_widget(Label(text=f"{name}: ", font_size=20, size_hint=(0.5, 1)))
        lay.add_widget(inp)
        return lay

    def sub_to_database(self):
        data = {self.email_input.text: {"name": self.name_input.text,
                                        "email": self.email_input.text,
                                        "password": self.password_input.text}}
        print(data)
        return data


class MyApp(App):
    def build(self):
        return LoginLayout()


if __name__ == "__main__":
    app_var = MyApp()
    app_var.run()
