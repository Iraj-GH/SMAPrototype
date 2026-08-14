from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from datetime import datetime


class MyApp(App):
    def build(self):
        layout = FloatLayout()
        Label1 = Label(text='Class 10 A',font_size=35, size_hint=(0.4,0.4), pos_hint={'center_x': 0.1, 'center_y': 0.9})
        self.Label2 = Label(text='',font_size=35, size_hint=(0.5,0.5), pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.Label3 = Label(text='',font_size=15, size_hint=(0.5,0.5), pos_hint={'center_x': 0.5, 'center_y': 0.86})
        self.update_time()
        Clock.schedule_interval(self.update_time, 1)
        layout.add_widget(Label1)
        layout.add_widget(self.Label2)
        layout.add_widget(self.Label3)
        return layout    

    def update_time(self, *args):
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d %b %Y")
        self.Label3.text = current_date
        self.Label2.text = current_time

if __name__ == '__main__':
    MyApp().run()  
