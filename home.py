from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.button import Button 
from kivy.clock import Clock 
from datetime import datetime, date
from kivy.core.window import Window 
from kivy.graphics import Color, RoundedRectangle,Ellipse, Rectangle
 
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

        Label7 = Label(text='Currently',font_size=40, size_hint=(0.5,0.5), pos_hint={'center_x': 0.173, 'center_y': 0.787}, color=(20/255, 45/255, 70/255, 1))

        Label8 = Label(text='Todays Substitutions',font_size=40, size_hint=(0.5,0.5), pos_hint={'center_x': 0.703, 'center_y': 0.787}, color=(20/255, 45/255, 70/255, 1))

        Label9 = Label(text='Todays Routine',font_size=40, size_hint=(0.5,0.5), pos_hint={'center_x': 0.213, 'center_y': 0.505})

        Label10 = Label(text='Discipline is the bridge between goals and achievements',font_size=30, size_hint=(0.5,0.5), pos_hint={'center_x': 0.34, 'center_y': 0.033}, color=(20/255, 45/255, 70/255, 1))

        Button1 = Button(text='', pos_hint={'center_x': 0.7845, 'center_y': 0.926}, size_hint=(0.055, 0.105), background_color=(177/255, 199/255, 220/255, 0.9), background_normal="bar-code.png", background_down="bar-code.png")

        Button2 = Button(text='', pos_hint={'center_x': 0.3033, 'center_y': 0.7245}, size_hint=(0.45, 0.25), background_color=(177/255, 199/255, 220/255, 0.1))

        Button3 = Button(text='', pos_hint={'center_x': 0.767, 'center_y': 0.7245}, size_hint=(0.45, 0.25), background_color=(177/255, 199/255, 220/255, 0.1))

        Button4 = Button(text='', pos_hint={'center_x': 0.037, 'center_y': 0.8}, size_hint=(0.055, 0.105), background_color=(177/255, 199/255, 220/255, 0.9), background_normal="Notification.png", background_down="Notification.png")

        Button5 = Button(text='', pos_hint={'center_x': 0.037, 'center_y': 0.55}, size_hint=(0.055, 0.105), background_color=(177/255, 199/255, 220/255, 0.9), background_normal="home.png", background_down="home.png")

        Button6 = Button(text='', pos_hint={'center_x': 0.037, 'center_y': 0.44}, size_hint=(0.055, 0.105), background_color=(177/255, 199/255, 220/255, 0.9), background_normal="white-calendar.png", background_down="white-calendar.png")

        Button7 = Button(text='', pos_hint={'center_x': 0.037, 'center_y': 0.33}, size_hint=(0.055, 0.105), background_color=(177/255, 199/255, 220/255, 0.9), background_normal="people.png", background_down="people.png")

        Button8 = Button(text='', pos_hint={'center_x': 0.037, 'center_y': 0.22}, size_hint=(0.055, 0.105), background_color=(177/255, 199/255, 220/255, 0.9), background_normal="settings.png", background_down="settings.png")

        Button9 = Button(text='', pos_hint={'center_x': 0.5325, 'center_y': 0.328}, size_hint=(0.92, 0.5), background_color=(177/255, 199/255, 220/255, 0.1))

        Button10 = Button(text='', pos_hint={'center_x': 0.113, 'center_y': 0.787}, size_hint=(0.055, 0.105), background_color=(177/255, 199/255, 220/255, 0.9), background_normal="Blue-Person.png", background_down="Blue-Person.png")

        Button11 = Button(text='', pos_hint={'center_x': 0.573, 'center_y': 0.787}, size_hint=(0.055, 0.105), background_color=(177/255, 199/255, 220/255, 0.9), background_normal="Sub.png", background_down="Sub.png")

        Button12 = Button(text='', pos_hint={'center_x': 0.113, 'center_y': 0.505}, size_hint=(0.055, 0.105), background_color=(177/255, 199/255, 220/255, 0.9), background_normal="Blue-Calendar.png", background_down="Blue-Calendar.png")

        self.update_time() 
        Clock.schedule_interval(self.update_time, 1) 
        layout.add_widget(Label1) 
        layout.add_widget(self.Label2) 
        layout.add_widget(self.Label3) 
        layout.add_widget(self.Label4)
        layout.add_widget(self.Label5)
        layout.add_widget(self.Label6)
        layout.add_widget(Label7)
        layout.add_widget(Label8)
        layout.add_widget(Label9)
        layout.add_widget(Label10)
        layout.add_widget(Button1)
        layout.add_widget(Button2)
        layout.add_widget(Button3)
        layout.add_widget(Button4)
        layout.add_widget(Button5)
        layout.add_widget(Button6)
        layout.add_widget(Button7)
        layout.add_widget(Button8)
        layout.add_widget(Button9)
        layout.add_widget(Button10)
        layout.add_widget(Button11)
        layout.add_widget(Button12)
        return layout     
 
    def update_time(self, *args): 
        current_time = datetime.now().strftime("%H:%M") 
        current_date = datetime.now().strftime("%a, %d %b %Y") 
        self.Label3.text = current_date 
        self.Label2.text = current_time 
 
if __name__ == '__main__': 
    MyApp().run()
