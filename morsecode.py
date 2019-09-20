# -*- coding: utf-8 -*-
"""
Morse
Created on Sun Aug  4 00:51:41 2019

@author: Chase
"""
import time
import winsound
Dictionary = {'a': '.-', 'b':'-...', 'c':'-.-.', 'd':'-..','e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j': '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o':'---', 'p':'.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..', '.':'.-.-.-', ',':'--..--', '?':'..--..'}
def new_code():
    user_in = input('Text to convert: ')
    result = ''
    for i in user_in.lower():
        if i == ' ':
            result = result + '  '
        else:
                result = result + Dictionary[i] + ' '
    print(result)
    music_in = input('Do you want to hear it?(y/n) ')
    if music_in == 'y':
       WPM_in = input('Enter desired WPM: ')
       tpw = 60 / int(WPM_in)
       tpc = tpw / 4.5
       tpmc = tpc / 3.5517241379
       interval = tpmc * 1000
       for i in result:
           if(i == ' '):
               time.sleep((interval*1.5) / 1000)
           elif(i == '-'):
               winsound.Beep(1000, int(interval))
           else:
               winsound.Beep(1000, int(interval/2))
while 1:
    new_code()
