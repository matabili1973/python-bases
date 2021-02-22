from time import sleep
from itertools import cycle

class TrafficLight:
    __color = [
        ['Red', 7],
        ['Yellow', 2],
        ['Green', 8],
        ['Yellow', 2]
        ]

    def running(self):
        self.color = TrafficLight.__color
        counter = 0
        for itor in cycle(self.color):
            if counter > 20:
                break
            print(itor[0])
            sleep(itor[1])
            counter += 1

my_light = TrafficLight()
my_light.running()
