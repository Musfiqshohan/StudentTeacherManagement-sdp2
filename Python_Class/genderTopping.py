from Python_Class.studentDecorator import studentDecorator


class genderToppings(studentDecorator):
    gender=""

    def __init__(self, gender, componentperson):
        self.gender = gender
        self.componentperson = componentperson;
