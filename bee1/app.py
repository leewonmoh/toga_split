
import toga
from toga.style import Pack
from toga.style.pack import *
from eliza import Eliza 
import os
import random

class Bee1(toga.App):
    def startup(self):
        #alternative icon embedding
        #path=os.path.dirname(os.path.abspath(__file__))
        #brutus_icon=os.path.join(path,"icons","brutus.icns")
        #Eliza module
        self.partner=Eliza()

        self.chat=toga.DetailedList(
            data=[
                {
                    'icon':toga.Icon('icons/brutus.icns'),

                    'title': 'Bot',
                    'subtitle': 'Hello. How are you feeling today?'
                }
            ]
            ,style=Pack(flex=1))

        self.text_input=toga.TextInput(style=Pack(flex=1))
        
        send_button=toga.Button('Send',style=Pack(padding_left=5),on_press=self.handle_input)

        input_box=toga.Box(
            children=[self.text_input, send_button],
            style=Pack(direction=ROW, alignment=CENTER, padding=5)
        )
#alignment='CENTER',
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)

        # Create a main content box
        #main_box = toga.Box()

        # Add the content on the main window
        self.main_window.content = toga.Box(
            children=[self.chat,input_box],
            style=Pack(direction=COLUMN)
        )

        # Show the main window
        self.main_window.show()

    def handle_input(self,widget,**kwargs):
        input_text=self.text_input.value
        self.chat.data.append(
            icon=toga.Icon('icons/cricket-72.png'),
            title='User',
            subtitle=input_text
        )
        self.text_input.value=''
        self.chat.scroll_to_bottom()

        yield random.random()*2        
        response=self.partner.respond(input_text)
        self.chat.data.append(
            icon=toga.Icon('icons/brutus.icns'),
            title='Bot',
            subtitle=response
        )

def main():
    return Bee1('bee1', 'org.beeware.bee1')

