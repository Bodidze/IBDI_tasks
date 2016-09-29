from abc import ABCMeta, abstractmethod
import time
from functools import reduce

class Problem(metaclass = ABCMeta):
    """
    Abstract base class for data flow and collection of
    implemented solvers for its computation, timing and check.
    """

    def __init__(self):
        self.solvers = []


    @abstractmethod
    def inputs(self):
        pass


    @abstractmethod
    def outputs(self):
        pass


    def add_solver(self, obj):
        """
        Serves for adding classes with 'compute' method for
        calculations on data.
        """

        if hasattr(obj,"compute"):
            self.solvers.append(obj)
        else:
            raise NoMethodException("Class does not have 'compute' method")


    def profile_solvers(self):
        """
        Profiles all the available solutions added via add_solver method.
        """

        clsname = self.__class__.__name__
        x1, x2 = self.inputs()
        check = self.outputs()
        loops = 10

        for obj in self.solvers:
            t = 0
            objname = obj.__class__.__name__
            print("Solving '%s' with '%s', input = (%d, %d) "%(clsname, objname, x1, x2))
            #was decided to loop over tuple
            #time module was used for timing for the sake of simplicity

            for i in range(loops):
                start = time.time()
                r1 = obj.compute(x1)
                r2 = obj.compute(x2)
                t+=time.time() - start

                if (r1, r2) != check:
                    print("Result is not correct")
                    break

            print("%d loops took %f seconds on average" %(loops, t/loops))


class SumUpToN(Problem):
    def inputs(self):
        return 100, 1000000
    def outputs(self):
        return 5050, 500000500000


class Naive:
    def compute(self, N):
        return reduce(lambda x, y: x + y, range(1, N + 1))


class ConstTime:
    def compute(self, N):
        return (N + 1) * N / 2


class Wrong:
    def compute(self, N):
        return 100

#p=Problem()
#TypeError: Can't instantiate abstract class..

prob = SumUpToN()
prob.add_solver(Naive())
prob.add_solver(ConstTime())
prob.add_solver(Wrong())
prob.profile_solvers()