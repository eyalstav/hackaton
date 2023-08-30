import json
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

class Map(MapView):
    def __init__(self):
        super().__init__()
        self.zoom = 15
        self.get_current_location()
        res = requests.get("https://communityconnect1234-default-rtdb.europe-west1.firebasedatabase.app/Help.json")
        data = dict(res.json())
        print(data)
        for key, val in data.items():
            print(val)
            val = dict(val)
            des = val['description']
            lat = val["location"]["lat"]
            lon = val["location"]["lon"]
            marker = MapMarkerPopup(lat=lat, lon=lon)
            marker.add_widget(Button(text=des))
            self.add_widget(marker)

    def get_current_location(self):
        from kivy.utils import platform
        if platform == "android" or platform == "ios":
            from plyer import gps
            gps.configure(on_location = self.update_position,on_status=self.auth_gps)
        if platform == "win":
            import geocoder
            g = geocoder.ip('me')
            self.lat, self.lon = g.latlng

    def auth_gps(self, status):
        if status == "provider-enabled":
            pass
        else: pass
    def update_position(self,*args,**kwargs):
        self.lat = kwargs["lat"]
        self.lon = kwargs["lon"]

class SOS_Form(GridLayout):
    def __init__(self, **kwargs):
            super(SOS_Form, self).__init__(**kwargs)
            self.cols = 1
            self.form()

    def form(self):
        self.clear_widgets()
        self.add_widget(Label(text = "SOS!", font_size = 40))
        self.des_input = TextInput(text="Description", font_size=20)
        self.add_widget(self.form_input("Description", self.des_input))
        self.add_widget(Button(text="Get Help!").bind(on_press = self.submit()))
    def form_input(self, name, inp):
        lay = GridLayout(cols = 2)
        lay.size_hint = (0.5,1)
        lay.add_widget(Label(text = f"{name}: ",font_size=20,size_hint= (0.5,1)))
        lay.add_widget(inp)
        return lay

    def submit(self):
        import geocoder
        g = geocoder.ip('me')
        self.lat, self.lon = g.latlng

        data = {"eyal44321@kjghkhgmail.com": {"description": self.des_input.text, "location": {"lat": self.lat, "lon": self.lon}}}
        print(data)
        res = requests.patch("https://communityconnect1234-default-rtdb.europe-west1.firebasedatabase.app/Help.json",
                             json.dumps(data))
        print(res.content)

