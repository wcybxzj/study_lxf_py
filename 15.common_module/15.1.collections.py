# -*- coding: utf-8 -*-
__author__ = 'yangbingxi'


from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

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

        #注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
        od = OrderedDict()
        od['z'] = 11
        od['y'] = 22
        od['x'] = 33
        print od

    def Counter(self):
        c = Counter()
        for ch in 'programming':
            c[ch] = c[ch]+1
        print c

    def run(self):
            self.namedtuple()
            self.deque()
            self.defaultdict()
            self.OrderedDict()
            self.Counter()

obj = mycollections()
obj.run()
print '============================='


class LastUpdatedOrderedDict(OrderedDict):
    '''FIFO'''
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)

obj = LastUpdatedOrderedDict(10)
obj['name'] = 'ybx'
obj['sex'] = 'male'
obj['age'] = 29
print obj