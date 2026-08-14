from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.button import Button 
from kivy.clock import Clock 
from datetime import datetime 
from kivy.core.window import Window 
from kivy.graphics import Color, RoundedRectangle
 
class MyApp(App): 
    def build(self): 
        layout = FloatLayout() 
        Window.clearcolor = (64/255, 96/255, 119/255, 1) 
        with layout.canvas.before:
            Color(89/255, 120/255, 148/255, 1)
            self.box = RoundedRectangle(pos=(140, 857), size=(1770, 120), radius=[20])
            Color(45/255, 80/255, 110/255, 1)
            self.box2 = RoundedRectangle(pos=(11, 10), size=(120, 967), radius=[20])
            Color(64/255, 96/255, 119/255, 1)
            self.box3 = RoundedRectangle(pos=(1450, 867), size=(425, 100), radius=[20])        
            Color(177/255, 199/255, 220/255, 1)
            self.box4 = RoundedRectangle(pos=(1450, 862), size=(110, 110), radius=[20])
            Color(177/255, 199/255, 220/255, 1)          
            self.box6 = RoundedRectangle(pos=(145, 590), size=(870, 250), radius=[20])
            Color(177/255, 199/255, 220/255, 1)
            self.box7 = RoundedRectangle(pos=(1040, 590), size=(870, 250), radius=[20])
            Color(177/255, 199/255, 220/255, 1)
            self.box8 = RoundedRectangle(pos=(140, 10), size=(1770, 50), radius=[20])
            Color(98/255, 126/255, 150/255, 1)
            self.box = RoundedRectangle(pos=(140, 75), size=(1770, 500), radius=[20])
        Label1 = Label(text='Class 10 A',font_size=55, size_hint=(0.9,0.4), pos_hint={'center_x': 0.2, 'center_y': 0.93}) 
        self.Label2 = Label(text='',font_size=55, size_hint=(0.5,0.5), pos_hint={'center_x': 0.535, 'center_y': 0.94}) 
        self.Label3 = Label(text='',font_size=25, size_hint=(0.5,0.5), pos_hint={'center_x': 0.535, 'center_y': 0.89}) 
        self.Label4 = Label(text='Mark Your Attendance',font_size=30, size_hint=(0.5,0.5), pos_hint={'center_x': 0.895, 'center_y': 0.95})
        self.Label5 = Label(text='Scan Your Code',font_size=15, size_hint=(0.5,0.5), pos_hint={'center_x': 0.845, 'center_y': 0.92})
        self.Label6 = Label(text='To Mark Yourselves as Present',font_size=15, size_hint=(0.5,0.5), pos_hint={'center_x': 0.872, 'center_y': 0.90})
        Button1 = Button(text='', pos_hint={'center_x': 0.7845, 'center_y': 0.926}, size_hint=(0.055, 0.105), background_color=(177/255, 199/255, 220/255, 0.3))

        self.update_time() 
        Clock.schedule_interval(self.update_time, 1) 
        layout.add_widget(Label1) 
        layout.add_widget(self.Label2) 
        layout.add_widget(self.Label3) 
        layout.add_widget(self.Label4)
        layout.add_widget(self.Label5)
        layout.add_widget(self.Label6)
        layout.add_widget(Button1)
        return layout     
 
    def update_time(self, *args): 
        current_time = datetime.now().strftime("%H:%M") 
        current_date = datetime.now().strftime("%d %b %Y") 
        self.Label3.text = current_date 
        self.Label2.text = current_time 
 
if __name__ == '__main__': 
    MyApp().run()
