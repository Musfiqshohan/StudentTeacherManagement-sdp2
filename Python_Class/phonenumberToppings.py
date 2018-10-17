from Python_Class.studentDecorator import studentDecorator


class phonenumberToppings(studentDecorator):
    number=0

    def __init__(self, number, componentperson):
        self.number = number
        self.componentperson = componentperson
