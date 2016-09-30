import copyreg
import sys
import pickle
import dill

class Meta(type):

    def __new__(mcls, name, bases, attrs):
        cls = type.__new__(mcls, name, bases, attrs)
        setattr(sys.modules[__name__], name, cls)   # class added to module namespace so that pickle.dumps is able to find them
        return cls

    def __reduce__(self):
        return (person_with_pet(), (self.pet, ),)


def person_with_pet(pet):
    name = 'PersonWith%s' % str(pet).capitalize()
    return Meta(name, (), {'pet': pet})



#copyreg.pickle(Meta, person_with_pet)

a=person_with_pet('cat')
bob=a()

pickld=pickle.dumps(bob)
unpickld=pickle.loads(pickld)

#__getstate__ should return a picklable object (such as a tuple) with enough information to reconstruct the instance.

#__setstate__ should expect to receive the same object, and use it to reconfigure the instance.