# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'
import json
d = dict(name='Bob', age=20, score=88)

json_d = json.dumps(d)
print json_d

str_d = json.loads(json_d)
print str_d
