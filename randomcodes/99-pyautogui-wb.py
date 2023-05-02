import string
#
#-------------------------------------------------------------------
#
import pyautogui
from typing import Dict
import sys
import pygame
pyautogui.alert('This is an alert box.')
DBox1 = pyautogui.confirm('Shall I proceed?')
DBox2 = pyautogui.confirm('Enter Options:',buttons=['A', 'B', 'C'])
DBox3 = pyautogui.prompt('What is your name?')
DBox4 = pyautogui.password('Enter Password(text will be hidden)')
print ('Here are my response:', DBox1, DBox2, DBox3, DBox4)
pyautogui.alert('Here are my response:', DBox1, DBox2, DBox3, DBox4)
pyautogui.alert('Here are my response:')
pyautogui.alert(DBox1, DBox2, DBox3, DBox4)
ScreenWidth, ScreenHeight = pyautogui.size()
CMouseX, CMouseY = pyautogui.position()
pyautogui.alert(text=(CMouseX, CMouseY), title='Mouse Position')
print ('Mouse Position', CMouseX, CMouseY)
#
#-------------------------------------------------------------------
#