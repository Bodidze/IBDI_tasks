import pickle
from Task2 import person_with_pet

cat_cls = person_with_pet('cat')
bob = cat_cls()
pickld = pickle.dumps(bob)
pickle.dump(pickld, open('save.p', 'wb'))
