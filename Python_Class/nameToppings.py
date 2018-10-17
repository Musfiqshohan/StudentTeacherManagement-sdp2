from Python_Class.studentDecorator import studentDecorator


class nameToppings(studentDecorator):
    name=""

    def __init__(self, name, componentperson):
        self.name = name
        self.componentperson = componentperson;
