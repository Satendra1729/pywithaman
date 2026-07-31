import logging
from day3_logging import logging_setup

class Car :
    number_of_wheels = 4

    @staticmethod
    def test(): 
        print("this is a static method")

    def __init__(self,brand ,model, price): 
        logging.info("Car object is created!!")
        print("called __init__")
        self.brand = brand
        self.model = model
        self.price = price

        self.speed = 0

    def run(self,speed): 
        "this is run of Car"
        self.speed = speed
        print(f"{self.brand} {self.model} is running at {speed}")


    def __call__(self,test): 
        print(test)

    def __str__(self): 
        s =  f"brand : {self.brand}\n"
        s += f"model : {self.model}\n"
        s += f"price : {self.price}\n"
        s += f"speed : {self.speed}\n"
        return s 

    def __repr__(self): 
        return "this __rpel__"


if __name__ == "__main__":
    logging_setup()
    car = Car("maruti","800", 123465)
    print(f"number of wheel in a car {Car.number_of_wheels}")

    Car.test()
    car.test()
    car.run(10)

    car("test")
    car_as_string = str(car)
    print(car_as_string)
    print(Car.run.__doc__)

