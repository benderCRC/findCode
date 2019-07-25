#!/usr/bin/env python
#Tool to find which file contains specific code
#By Shawn Bender 2019

import os 

while(True):
    
    text = raw_input()

    if(text == ""):
        exit()

    cmd = 'grep --with-filename ' + "'" + text +"'" + ' *'

    os.system(cmd)


