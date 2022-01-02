import json
#import CountryHouseWateringClasses as WC
import Event as EV
import datetime as DT
from StausesAndDefaultSettings import *


class CountryHouseModel:
    iCount = 0
    def __init__(self):
        self.settings = {}
        try:
            with open('config.json') as f:
                loadedSettings = json.load(f)
            #проверить, что все ключи есть, а те, которых нет, добавить с дефолтными значениями
            self.settings = {**loadedSettings, **defaultSettings} #на каком уровне вложенности работает????????????

        except FileNotFoundError:
            self.settings = defaultSettings
            
        
        #--------------------------Internal objects-------------------------------
        self.watering = self.settings["watering"] #один большой объект для отправки во view
        self.zones = self.watering["zones"] #внутренние объекты для упрощения кода
        self.cycles =  self.watering["cycles"] #внутренние объекты для упрощения кода
        
        self.otherControls = self.settings["otherControls"]
        self.contactors = self.otherControls["contactors"]
            
        self.alarmLog = []

        
        #--------------------------------Events---------------------------------

        
        #особытия для внешних обработчиков, здесь список названий всех возможных событий, а уже добавлять их к eventsList будем по запросу в отдельной публичной функции
        self.handledEvents = ["wateringUpdated", "otherControlsUpdated", "alarmLogUpdated", "onQuit"]
        self.eventsList = {}
        
        
        #--------------------------------Hardware---------------------------------
        
        
    #-------------------------------Interface------------------------------------
    def changeWateringCycleTime(self, cycleNumber, hours, minutes):
        try:
            if self.cycles[cycleNumber-1]["status"] != IN_WORK:
                self.cycles[cycleNumber-1]["hours"] = hours
                self.cycles[cycleNumber-1]["minutes"] = minutes
                self.eventsList["wateringUpdated"].trigger(self.watering)
        except:
            pass
    
    def addWateringCycle(self, hours, minutes):
        try:
            durations = [defaultDuration for item in range(len(self.zones))]
            self.cycles.append({"hours":hours,"minutes":minutes, "durations":durations,"status": OFF,"progress":0.0})
            self.eventsList["wateringUpdated"].trigger(self.watering)
        except:
            pass
    
    def changeZoneDuration(self, cycleNumber, zoneNumber, minutes):
        try:
            if self.cycles[cycleNumber-1]["status"] != IN_WORK:
                self.cycles[cycleNumber-1]["durations"][zoneNumber-1] = minutes
                self.eventsList["wateringUpdated"].trigger(self.watering)
        except:
            pass
    
    def manuallyToggleZone(self, zoneNumber):
        pass
    
    def acknowledgeAlarm(self):
        pass
    
    def clearAlarmLog(self):
        pass
    
    def toggleContactor(self, contactorNumber):
        pass
    
    def hwSetDigitalInputState(self, inputNumber):
        pass
    
    def subscribeForEvent(self, event, callback):
        if event in self.handledEvents: #если есть хотя бы один подписчик, тогда добавляем Event в словарь
            self.eventsList[event] = EV.Event()
            self.eventsList[event].addCallback(callback)
            return True
        else:
            return False
    
    def onSecondTick(self):
        self.checkContactors()
        self.checkWatering()
        self.eventsList["otherControlsUpdated"].trigger(self.otherControls)
        self.eventsList["wateringUpdated"].trigger(self.watering)
        self.eventsList["alarmLogUpdated"].trigger(self.alarmLog)
    
    #-------------------------------Internal Functions---------------------------
    
    def checkContactors():
        #for contactor in self.contactors:
        #    if contactor["enabled"] == True:
        #        if contactor["gpioNumber"]
        pass
    
    
    def checkWatering():
        #now = DT.datetime.now()
        pass
    
    def quitProcedure(self):
        #GPIO.cleanup()
        self.eventsList["onQuit"].trigger()   


if __name__ == "__main__":
    ch = CountryHouseModel()
    now = DT.datetime.now().hour
    print(now)