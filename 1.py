from time import sleep


class TrafficLight():
    def __init__(self):
        self.__color = 'red'

    def running(self):
        '''run TrafficLight and printin color'''
        print('start running')
        print(self.__color)
        sleep(7)
        self.new_color()
        print(self.__color)
        sleep(2)
        self.new_color()
        print(self.__color)
        sleep(5)
        print('stop running')

    def new_color(self):
        '''check and set color'''
        if self.__color == 'red':
            self.__color = 'yellow'
        elif self.__color == 'yellow':
            self.__color = 'green'
        elif self.__color == 'green':
            self.__color = 'red'
        else:
            raise ValueError('color error')


t = TrafficLight()
t.running()
