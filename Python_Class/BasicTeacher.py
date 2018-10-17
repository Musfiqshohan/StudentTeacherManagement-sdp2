from Python_Class.ComponentPerson import ComponentPerson


class BasicTeacher(ComponentPerson):
    def __init__(self):
        ComponentPerson.__init__(self)

        self.role = "Teacher"
