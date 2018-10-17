from Python_Class.studentDecorator import studentDecorator


class passwordToppings(studentDecorator):
    password = ""

    def __init__(self, password, componentperson):
        self.password = password
        self.componentperson = componentperson;








