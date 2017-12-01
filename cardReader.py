# -*- coding: utf8 -*-
 
import time
import MFRC522
import RPi.GPIO as GPIO
from threading import Thread

class CardReader(Thread):
    def __init__(self, cardName):
        file = open("./Files/cardIds.txt", "r")
        self.kanjiId = ""
        self.rfidReader = MFRC522.MFRC522()
        
        for line in file:
            for word in line.split():
                if word == cardName:
                    kanjiId = line.split()[1]

    def run(self):
        while True:
            status, tag_type = self.rfidReader.MFRC522_Request(self.rfidReader.PICC_REQIDL)

            if status == self.rfidReader.MI_OK:
                status, uid = self.rfidReader.MFRC522_Anticoll()

                if status == self.rfidReader.MI_OK:
                    uid = ':'.join(['%X' % x for x in uid])
                    if uid == self.kanjiId:
                        return True
                    else:
                        return False
     
            time.sleep(.25)