__author__ = 'yangbingxi'


from collections import namedtuple, deque, defaultdict, OrderedDict

class mycollections(object):

    def namedtuple(self):
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(1, 2)
        print p.x
        print p.y
        print isinstance(p, Point)
        print isinstance(p, tuple)

    def deque(self):
        mylsit = ['a', 'b', 'c']
        q = deque(mylsit)
        q.append('x')
        q.appendleft('y')
        print q

    def defaultdict(self):
        dd = defaultdict(lambda: 'N/A')
        print dd['not_exists_key']

    def OrderedDict(self):
        mylist = [('a', 1), ('b', 2), ('c', 3)]
        print dict(mylist)
        print OrderedDict(mylist)



    def run(self):
        self.namedtuple()
        self.deque()
        self.defaultdict()
        self.OrderedDict()





obj = mycollections()
obj.run()

