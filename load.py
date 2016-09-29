import pickle
from fab import bob

unpickled=pickle.load(open('save.p', 'rb'))
print(type(bob) is type(unpickled))