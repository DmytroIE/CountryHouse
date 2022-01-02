statuses = { 0: "Выключен", 1: "В ожидании", 2: "В работе", 3: "Неисправность"}
OFF = 0
PENDING = 1
IN_WORK = 2
FAULTY = 3

defaultDuration = 10

defaultSettings = {"watering":{"zones":[{"typicalFlowrate":1.2,"gpioNumber":13,"enabled":False,"status": OFF,"progress":0.0,"manuModeOn":False, "manuallyOn":False},\
                                        {"typicalFlowrate":1.2,"gpioNumber":14,"enabled":False,"status": OFF,"progress":0.0,"manuModeOn":False, "manuallyOn":False},\
                                        {"typicalFlowrate":1.2,"gpioNumber":15,"enabled":False,"status": OFF,"progress":0.0,"manuModeOn":False, "manuallyOn":False},\
                                        {"typicalFlowrate":1.2,"gpioNumber":16,"enabled":False,"status": FAULTY,"progress":0.0,"manuModeOn":False, "manuallyOn":False},\
                                        {"typicalFlowrate":1.2,"gpioNumber":17,"enabled":False,"status": OFF,"progress":0.0,"manuModeOn":False, "manuallyOn":False}],\
                               "cycles":[{"hour":6,"minute":0, "durations":[10,10,10,10,10],"status": OFF,"progress":0.0},\
                                         {"hour":20,"minute":0, "durations":[15,15,15,15,15],"status": OFF,"progress":0.0}], \
                               "flowmeter":{"flowrate":0.0,"gpioNumber":9,"freqWeight":0.2083333},\
                               },
                   "otherControls":{"contactors":[{"enabled":False, "feedback":False, "gpioNumber":5},\
                                              {"enabled":False, "feedback":False, "gpioNumber":6},\
                                              {"enabled":False, "feedback":False, "gpioNumber":7}]},
                   }

if __name__ == "__main__":
    print(statuses[defaultSettings["watering"]["zones"][0]["status"]])