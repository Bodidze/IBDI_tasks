import pickle
from fab import bob

unpickled=pickle.load(open('save.p', 'rb'))
#unpickled=pickle.load(open('awesome_possum.pkl', 'rb'))
print(type(bob) is type(unpickled))