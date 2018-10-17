# Python 3.4+
from abc import ABC, abstractmethod
from Python_Class.ComponentPerson import ComponentPerson
class Abstract(ComponentPerson,ABC):
    @abstractmethod
    def foo(self):
        pass

# # Python 3.0+
# from abc import ABCMeta, abstractmethod
# class Abstract(metaclass=ABCMeta):
#     @abstractmethod
#     def foo(self):
#         pass
#
# # Python 2
# from abc import ABCMeta, abstractmethod
# class Abstract:
#     __metaclass__ = ABCMeta
#
#     @abstractmethod
#     def foo(self):
#         pass


