class TV:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def show(self):
        print(f'{self.channel}, {self.volume}, {self.on}')
    
    def setChannel(self, channel):
        self.channel = channel

    def getChannel(self):
        return f'{self.channel}'

t = TV(9, 10, True)
t.show()
t.setChannel(11)
print(t.getChannel())