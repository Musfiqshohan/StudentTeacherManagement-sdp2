from Python_Class.studentDecorator import studentDecorator


class studentidtoppings(studentDecorator):
    id=0
    def __init__(self, id, componentperson):
        self.id = id
        self.componentperson = componentperson;
