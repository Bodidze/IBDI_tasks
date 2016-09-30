from multiprocessing import Process, Queue
import pickle
from Task2 import person_with_pet
import dill

def pet_reader(q):
    msg = q.get()
    while not msg == 'STOP':
        with open(msg, 'rb') as f:
            obj = pickle.load(f)
        print(type(obj))
        msg = q.get()
    print('STOPPING!')

if __name__ == '__main__':
    # forking a separate process
    q = Queue()
    p = Process(target=pet_reader, args=(q,))
    p.start()

    # creating and dumping in this process
    pos_cls = person_with_pet('possum')
    awesome_possum = pos_cls()
    with open('awesome_possum.pkl', 'wb') as f:
        pickle.dump(awesome_possum, f)

    # sending the data to the other process (file name in this case, but can be
    # a dump string as well
    q.put('awesome_possum.pkl')

    # exiting gracefully
    q.put('STOP')  # just in case unpickling worked
    p.join()
