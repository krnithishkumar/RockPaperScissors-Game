import random

import kivy
import win32com.client as win


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder

from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
)

from kivy.clock import Clock

from os import listdir

PATH = './kv/'
for kv in listdir(PATH):
    Builder.load_file(PATH + kv)


class HomeScreen(GridLayout):
    count = NumericProperty(0)
    count2 = NumericProperty(0)
    pc = StringProperty(0)
    displaycount1 = ''
    def updateOpp(self, o):
        if o==1:
            self.pc = "Rock"
        elif o==2:
            self.pc = "Paper"
        elif o==3:
            self.pc = "Scissor"
        print(self.pc)
    def rock(self):
        player = 1
        opp = self.generateRandom()
        self.updateOpp(opp)
        #self.pc = "change"
        self.updateScore(player, opp)
        
    def paper(self):
        player = 2
        opp = self.generateRandom()
        self.updateOpp(opp)
        self.updateScore(player, opp)
        
    def scissor(self):
        player = 3
        opp = self.generateRandom()
        self.updateOpp(opp)
        self.updateScore(player, opp)
        
    def generateRandom(self):
        computer = random.choice([1, 2, 3])
        print(computer)
        return computer
    def updateScore(self, p, o):
        if (p==1 and o==3) or (p==2 and o==1) or (p==3 and o==2):
            self.count += 1
        elif (p!=o):
            self.count2 += 1
        
    strcount=str(StringProperty(count))
    displaycount1 = "User Score: "
        
    speaker = win.Dispatch("SAPI.SpVoice")
    speaker.Speak("Welcome to Rock Scissors Game");
    
class MyApp(App):
    title = 'Paper Rock Scissors'
    obj = HomeScreen()
    def build(self):
        return HomeScreen()

if __name__ == '__main__':
    MyApp().run()
