from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import yt_dlp
import webbrowser

class MediaFinderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.query_input = TextInput(hint_text='क्या खोजना है?', multiline=False)
        self.btn = Button(text='Play / Search', on_press=self.find_media)
        self.result = Label(text='परिणाम यहाँ दिखेगा...')
        self.layout.add_widget(self.query_input)
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.result)
        return self.layout

    def find_media(self, instance):
        query = self.query_input.text
        ydl_opts = {'default_search': 'ytsearch1'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            video_url = info['entries'][0]['webpage_url']
            webbrowser.open(video_url)

if __name__ == '__main__':
    MediaFinderApp().run()
