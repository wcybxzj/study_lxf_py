__author__ = 'yangbingxi'


from collections import namedtuple

class mycollections(object):
    def namedtuple(self):
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(1, 2)
        print p.x
        print p.y

    def run(self):
        self.namedtuple()


obj = mycollections()
obj.run()

