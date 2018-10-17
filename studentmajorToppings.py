from Python_Class.studentDecorator import studentDecorator


class studentmajorToppings(studentDecorator):
    major= ""

    def __init__(self, major, componentperson):
        self.major = major
        self.componentperson = componentperson;





