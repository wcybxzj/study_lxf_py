__author__ = 'yangbingxi'


class ClassOne:
    def lazy_sum(self, *args):
        def sum():
            ax = 0
            for n in args:
                ax = ax +n
            return ax
        return sum

    def closure_bug(self):
        fs = []
        for i in range(1, 4):
            def f():
                return i * i
            fs.append(f)
        return fs

    def closure(self):
        fs = []
        for i in range(1, 4):
            def f(j):
                def g():
                    return j * j
                return g
            fs.append(f(i))
        return fs




    def run(self):
        func = self.lazy_sum(1, 3, 5, 7)
        print func()

        func2 = self.lazy_sum(1, 3, 5, 7)
        print func == func2

        f1, f2, f3 = self.closure_bug()
        print f1(),
        print f2(),
        print f3()

        f1, f2, f3 = self.closure()
        print f1(),
        print f2(),
        print f3()



obj = ClassOne()
obj.run()
