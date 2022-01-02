import tkinter as tk
from tkinter import ttk
import Event as EV
from StausesAndDefaultSettings import *


class WateringZoneWidget(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, borderwidth = 1, relief = "solid", padding = 2)
        
        zone = kwargs["zone"]
        
        self._index = kwargs["index"]

        self._lbl_name = tk.Label(self, text=f'Зона {self._index + 1}')
        #self._lbl_name.grid(column = 0, row = 0)
        self._lbl_name.pack(side = tk.LEFT)
        
        self._typicalFlowrate = tk.StringVar()
        self._typicalFlowrate.set(zone["typicalFlowrate"])
        self._ent_typicalFlowrate = tk.Entry(self, textvariable = self._typicalFlowrate, width = 3)
        #self._ent_typicalFlowrate.grid(column = 1, row = 0)
        self._ent_typicalFlowrate.pack(side = tk.LEFT)
        
        self._status = tk.StringVar()
        self._status.set(statuses[zone["status"]])
        self._lbl_status = tk.Label(self, textvariable = self._status)
        #self._lbl_status.grid(column = 2, row = 0)
        self._lbl_status.pack(side = tk.LEFT)
        
        self._enabled = tk.BooleanVar()
        self._enabled.set(zone["enabled"])
        self._chk_enabled = tk.Checkbutton(self, variable = self._enabled, state = "disabled")
        #self._chk_enabled.grid(column = 3, row = 0)
        self._chk_enabled.pack(side = tk.LEFT)
        
        self._progress = tk.DoubleVar()
        self._progress.set(zone["progress"])
        self._bar_progress = ttk.Progressbar(self, length=100, variable = self._progress)
        #self._bar_progress.grid(column = 4, row = 0)
        self._bar_progress.pack(side = tk.LEFT)
        
        self._btn_manuModeOn = tk.Button(self, text = "Руч.реж.")
        #self._bar_progress.grid(column = 5, row = 0)
        self._btn_manuModeOn.pack(side = tk.LEFT)
        
class WateringCycleWidget(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, borderwidth = 1, relief = "solid", padding = 2)
        
        cycle = kwargs["cycle"]
        
        self._onCycleTimeChange = kwargs["onCycleTimeChange"]
        self._index = kwargs["index"]

        self._lbl_name = tk.Label(self, text=f'Полив {self._index + 1}')
        self._lbl_name.grid(row = 0, columnspan = 3, column = 1)
        

        self._spb_hour = tk.Spinbox(self, from_ = 0, to = 23, width = 2,\
                                    command = lambda: self._onCycleTimeChange(index = self._index, hour = self._spb_hour.get()), \
                                    wrap = True, state = "readonly")
        self._spb_hour.grid(row = 1, column = 0)
        
        self._lbl_timeDivider = tk.Label(self, text=':')
        self._lbl_timeDivider.grid(column = 2, row = 1)
        

        self._spb_minute = tk.Spinbox(self, from_ = 0, to = 59, width = 2,\
                                      command = lambda: self._onCycleTimeChange(index = self._index, minute = self._spb_minute.get()), \
                                      wrap = True, state = "readonly")
        self._spb_minute.grid(row = 1, column = 3)
        
      
        

class WateringWidget(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        
        watering = kwargs["watering"]
        onCycleTimeChange = kwargs["onCycleTimeChange"]
        
        self._zoneWidgets = []
        for index, zone in enumerate(watering["zones"]):
            zoneWidget = WateringZoneWidget(self, zone = zone, index = index)
            zoneWidget.grid(row = index + 1, column = 0, sticky = tk.W)
            self._zoneWidgets.append(zoneWidget)
            
        self._cycleWidgets = []
        for index, cycle in enumerate(watering["cycles"]):
            cycleWidget = WateringCycleWidget(self, cycle = cycle, index = index, onCycleTimeChange = onCycleTimeChange)
            cycleWidget.grid(row = 0, column = index + 1)
            self._cycleWidgets.append(cycleWidget)
        
        
        n = len(watering["cycles"])
        m = len(watering["zones"])
        self._durationEntries = [[0] * m for i in range(n)]
        
        for indexZone, zone in enumerate(watering["zones"]):
            for indexCycle, cycle in enumerate(watering["cycles"]):
                newSpinbox = tk.Spinbox(self, from_ = 0, to = 30, width = 2, wrap = True, state = "readonly")
                self._durationEntries[indexCycle][indexZone]= newSpinbox
                newSpinbox.grid(row = indexZone + 1, column = indexCycle + 1)

class CountryHouseView(tk.Tk):
    def __init__(self, model):
        super().__init__()
        
        self._model = model
        
        self.title("Моя дача")
        self.geometry("800x480")
        #self.resizable(False, False)
        
        
        self._tabctrl_main = ttk.Notebook(self)  
        self._tab_watering = WateringWidget(self._tabctrl_main, watering = model["watering"], onCycleTimeChange = self.onCycleTimeChange)  
        self._tab_otherControls = tk.Frame(self._tabctrl_main)
        
        self._tabctrl_main.add(self._tab_watering, text='Полив')  
        self._tabctrl_main.add(self._tab_otherControls, text='Оборудование')  
        self._tabctrl_main.pack(expand = 1, fill=tk.BOTH) 



        #Часть Alarm Log
        self.frmAlarmLog = tk.LabelFrame(self, padx=5, pady=5,
                                text="Лог аварий и сообщений")
        self.frmAlarmLog.pack(fill=tk.X)
        self.btn = tk.Button(self.frmAlarmLog, text="Acknowledge", height = "5", width = "12")
        self.btn.pack(side = tk.LEFT)
        
        self.check = ttk.Checkbutton(self.frmAlarmLog, text = "Checkb")
        self.check.pack(side = tk.LEFT)
        
        self.bind("<<MyEvent>>", lambda e: self.lbl1.configure(text='yellow'))

    def onCycleTimeChange(self, **kwargs):
        if "hour" in kwargs:
            print(f'Cycle {kwargs["index"]} hour = {kwargs["hour"]}')
        elif "minute" in kwargs:
            print(f'Cycle {kwargs["index"]} minute = {kwargs["minute"]}')
        

if __name__ == "__main__":
    app = CountryHouseView(defaultSettings)
    app.mainloop()
