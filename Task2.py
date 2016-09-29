import pickle
import sys

class Meta(type):

    def __new__(mcls, name, bases, attrs):
        cls = type.__new__(mcls, name, bases, attrs)
        setattr(sys.modules[__name__], name, cls)   # class added to module namespace so that pickle.dumps is able to find them
        return cls


def person_with_pet(pet):
    name = 'PersonWith%s' % pet.capitalize()
    return Meta(name, (), {'pet': pet})


#cat_cls = person_with_pet('cat')
#bob = cat_cls()

#pickld = pickle.dumps(bob)
#unpickld = pickle.loads(pickld)

#print(type(bob) is type(unpickld))