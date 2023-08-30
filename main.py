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

class NavBar(GridLayout):
    def __init__(self, **kwargs):
        self.height = 100
        super(NavBar, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Button(text = "Billboard"))
        self.add_widget(Button(text="SOS!"))

class Map(MapView):
    def __init__(self):
        super().__init__()
        self.zoom = 15
        self.lon = 34.8
        self.lat = 32.1
        marker = MapMarkerPopup(lat=32.2, lon=34.7)
        self.add_widget(marker)


class AppLayout(GridLayout):
    def __init__(self, **kwargs):
        super(AppLayout,self).__init__(**kwargs)
        self.cols = 1
        self.current_view = Map()
        self.add_widget(self.current_view)
        self.add_widget(NavBar(size_hint=(1, 0.1)))

class MyApp(App):
    def build(self):
        return AppLayout()

if __name__ == "__main__":
    app_var = MyApp()
    app_var.run()