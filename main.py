import time
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


from SOS import *

class NavBar(GridLayout):
    def __init__(self, **kwargs):
        self.height = 100
        super(NavBar, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Button(text = "Billboard"))
        self.add_widget(Button(text="SOS!"))


class AppLayout(GridLayout):
    def __init__(self, **kwargs):
        super(AppLayout,self).__init__(**kwargs)
        self.cols = 1
        #self.add_widget(SOS_Form())
        self.add_widget(Map())
        self.add_widget(self.nav_bar())

    def change_map(self,shit):
        print("hioo")
        self.clear_widgets()
        self.add_widget(Map())
        self.add_widget(self.nav_bar())

    def change_sos(self,shit):
        print(shit)
        self.clear_widgets()
        self.add_widget(SOS_Form())
        self.add_widget(self.nav_bar())
    def change_billboard(self,shit):
        pass


    def nav_bar(self):
        lay = GridLayout(cols = 3,size_hint=(1,0.2))
        self.sos_btn = Button(text="BillBoard")
        self.sos_btn.bind(on_press = self.change_sos)
        lay.add_widget(self.sos_btn)
        self.bill_btn = Button(text="Map",size_hint = (0.7,1))
        self.bill_btn.bind(on_press = self.change_map)
        lay.add_widget(self.bill_btn)
        self.sos_btn = Button(text="SOS!")
        self.sos_btn.bind(on_press = self.change_sos)
        lay.add_widget(self.sos_btn)
        return lay

class MyApp(App):
    def build(self):
        return AppLayout()

if __name__ == "__main__":
    app_var = MyApp()
    app_var.run()