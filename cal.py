import sys
import subprocess
import calendar
import random
from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.metrics import dp


class CalendarCell(Label):
    def __init__(self, bg_color=(0.09, 0.16, 0.27, 1), text_color=(1, 1, 1, 1), border_color=(0.14, 0.23, 0.36, 1), radius=0, **kwargs):
        super().__init__(**kwargs)
        self.color = text_color
        self.bold = True
        self.halign = 'center'
        self.valign = 'middle'
        self.radius = radius

        with self.canvas.before:
            Color(*bg_color)
            self.background = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[(radius, radius)] * 4
            )
            Color(*border_color)
            self.border = Line(rounded_rectangle=(self.x, self.y, self.width, self.height, radius), width=1)

        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.background.pos = self.pos
        self.background.size = self.size
        self.border.rounded_rectangle = (self.x, self.y, self.width, self.height, self.radius)
        self.text_size = self.size


class CalendarWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=0, padding=dp(2), **kwargs)
        self.year = datetime.now().year
        self.month = datetime.now().month

        with self.canvas.before:
            Color(0.04, 0.07, 0.11, 1)
            self.outer_background = RoundedRectangle(pos=self.pos, size=self.size, radius=[(dp(18), dp(18))])
            Color(0.14, 0.23, 0.36, 1)
            self.outer_border = Line(rounded_rectangle=(self.x, self.y, self.width, self.height, dp(18)), width=2)

        self.bind(pos=self.update_border, size=self.update_border)
        self.show_calendar()

    def update_border(self, *args):
        self.outer_background.pos = self.pos
        self.outer_background.size = self.size
        self.outer_border.rounded_rectangle = (self.x, self.y, self.width, self.height, dp(18))

    def go_to_test(self, instance):
        subprocess.Popen([sys.executable, 'test.py'])
        App.get_running_app().stop()

    def show_calendar(self):
        self.clear_widgets()

        title_bar = FloatLayout(size_hint_y=None, height=65)

        title = CalendarCell(
            text=f'{calendar.month_name[self.month]} {self.year}',
            font_size=32,
            bg_color=(0.25, 0.02, 0.05, 1),
            text_color=(1, 0.9, 0.9, 1),
            border_color=(0.4, 0.05, 0.1, 1),
            radius=dp(14),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        title_bar.add_widget(title)

        back_button = Button(
            text='<--',
            font_size=18,
            bold=True,
            color=(1, 0.8, 0.8, 1),
            background_normal='',
            background_color=(0.25, 0.02, 0.05, 1),
            size_hint=(None, None),
            size=(dp(80), dp(45)),
            pos_hint={'x': 0.015, 'center_y': 0.5}
        )
        back_button.bind(on_press=self.go_to_test)
        title_bar.add_widget(back_button)

        self.add_widget(title_bar)

        grid = GridLayout(cols=7, rows=7, spacing=dp(2), padding=dp(2))
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        for day in weekdays:
            grid.add_widget(CalendarCell(
                text=day,
                font_size=19,
                bg_color=(0.06, 0.12, 0.20, 1),
                text_color=(0.6, 0.75, 0.9, 1),
                border_color=(0.14, 0.23, 0.36, 1),
                radius=dp(4)
            ))

        month = calendar.monthcalendar(self.year, self.month)
        num_days = calendar.monthrange(self.year, self.month)[1]
        
        green_count = random.randint(2, 5)
        green_days = set(random.sample(range(1, num_days + 1), green_count))

        while len(month) < 6:
            month.append([0] * 7)

        for week in month:
            for weekday, day in enumerate(week):
                if day == 0:
                    bg = (0.02, 0.04, 0.08, 1)
                    txt_color = (0.2, 0.3, 0.4, 1)
                    grid.add_widget(CalendarCell(text='', font_size=24, bg_color=bg, text_color=txt_color, border_color=(0.06, 0.1, 0.16, 1), radius=dp(4)))
                elif day in green_days:
                    bg = (0.01, 0.18, 0.06, 1)
                    grid.add_widget(CalendarCell(text=str(day), font_size=27, bg_color=bg, text_color=(0.8, 1, 0.8, 1), border_color=(0.02, 0.3, 0.1, 1), radius=dp(4)))
                elif weekday >= 5:
                    bg = (0.22, 0.01, 0.03, 1)
                    grid.add_widget(CalendarCell(text=str(day), font_size=27, bg_color=bg, text_color=(1, 0.85, 0.85, 1), border_color=(0.35, 0.03, 0.06, 1), radius=dp(4)))
                else:
                    grid.add_widget(CalendarCell(text=str(day), font_size=27, bg_color=(0.09, 0.16, 0.27, 1), text_color=(0.95, 0.97, 1, 1), border_color=(0.14, 0.23, 0.36, 1), radius=dp(4)))

        self.add_widget(grid)


class CalendarApp(App):
    def build(self):
        return CalendarWidget()


if __name__ == '__main__':
    CalendarApp().run()
