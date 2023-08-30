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
        self.add_widget(SOS_Form())
        #self.add_widget(Map())
        self.add_widget(NavBar(size_hint=(1, 0.1)))

class MyApp(App):
    def build(self):
        return AppLayout()

if __name__ == "__main__":
    app_var = MyApp()
    app_var.run()