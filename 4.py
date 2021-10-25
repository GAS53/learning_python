class Car():
    count_cars = 0

    def __init__(self, color, name, speed, is_police=False):
        Car.count_cars += 1
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'car {self.name} go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(f'car {self.name} turn {direction}')

    def show_speed(self):
        print(f'car {self.name} have speed now {speed}')

    def show_count_cars(self):
        print(Car.count_cars)


class TownCar(Car):
    def __init__(self, color, name, speed, is_police=False):
        super().__init__(color, name, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('excess speed!!!!!  ', end='')
        print(f'speed now {self.speed}')


class SportCar(Car):
    def __init__(self, color, name, speed, is_police=False):
        super().__init__(color, name, speed, is_police)


class WorkCar(Car):
    def __init__(self, color, name, speed, is_police=False):
        super().__init__(color, name, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('excess speed!!!!!')
        print(f'speed now {self.speed}')


class PoliceCar(Car):
    def __init__(self, color, name, speed):
        super().__init__(color, name, speed, is_police=True)


sport = SportCar('red', 'bugatti', speed=150)
town = TownCar('grey', 'lada', speed=90)
work = WorkCar('green', 'man', speed=70)
police = PoliceCar('white', 'ford', speed=120)
sport.go()
town.show_speed()
print(police.is_police)


town.show_count_cars()
