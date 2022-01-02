class Event:
    def __init__(self):
        self.callbacks = []
        
    def addCallback(self, callback):
        self.callbacks.append(callback)
    
    def trigger(self, *args):
        for c in self.callbacks:
            c(*args)