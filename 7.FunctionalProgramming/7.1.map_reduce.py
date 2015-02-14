__author__ = 'yangbingxi'


class ClassOne(object):
    def num_to_str(self):
        return map(str, [1, 2, 3 ,4 ,5])

    def add(self, x, y):
        return x + y

    def fn(self, x, y):
        return x * 10 + y

    def char2num(self, s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


    def str2int(self, s):
        def fn(x, y):
            return x * 10 + y

        def char2num(s):
            return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

        return reduce(fn, map(char2num, '13579'))

    def run(self):
        print self.num_to_str()
        print reduce(self.add, [1, 3, 5 ,7, 9])
        print reduce(self.fn, [1, 3, 5 ,7, 9])
        print reduce(self.fn, map(self.char2num, '13579'))
        print self.str2int('13579')



obj = ClassOne()
obj.run()
