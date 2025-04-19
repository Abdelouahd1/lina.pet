from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.scrollview import ScrollView

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)
        layout.add_widget(Image(source='assets/images/splash.png'))
        layout.add_widget(Button(text='Enter', size_hint_y=0.2,
                                 on_press=lambda x: self.manager.current = 'menu'))
        self.add_widget(layout)

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)
        layout.add_widget(Label(text='Welcome to LinaPet!', font_size=32))
        layout.add_widget(Button(text='Story', size_hint_y=0.2,
                                 on_press=lambda x: self.manager.current = 'story'))
        layout.add_widget(Button(text='Play', size_hint_y=0.2,
                                 on_press=lambda x: self.manager.current = 'game'))
        self.add_widget(layout)

class StoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)
        scroll = ScrollView()
        story_text = Label(
            text="Lina was a sweet cat I loved deeply.\nOne day, she disappeared without a trace...\nSo I made this game to keep her memory alive.",
            size_hint_y=None,
            font_size=18,
        )
        story_text.bind(texture_size=lambda instance, value: setattr(story_text, 'height', value[1]))
        scroll.add_widget(story_text)
        layout.add_widget(scroll)
        layout.add_widget(Button(text='Back to Menu', size_hint_y=0.2,
                                 on_press=lambda x: self.manager.current = 'menu'))
        self.add_widget(layout)

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.image = Image(source='assets/images/lina.png')
        self.layout.add_widget(self.image)

        button_layout = BoxLayout(size_hint_y=0.3, spacing=10)
        actions = ['happy', 'sad', 'eat', 'sleep']
        for act in actions:
            button = Button(text=act.capitalize())
            button.bind(on_press=lambda x, name=act: self.play_sound(name))
            button_layout.add_widget(button)

        self.layout.add_widget(button_layout)
        self.add_widget(self.layout)

    def play_sound(self, sound_name):
        sound = SoundLoader.load(f"assets/sounds/{sound_name}.mp3")
        if sound:
            sound.play()

class LinaPetApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(StoryScreen(name='story'))
        sm.add_widget(GameScreen(name='game'))
        return sm

if __name__ == '__main__':
    LinaPetApp().run()
