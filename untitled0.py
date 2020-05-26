# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:01:31 2020

@author: -
"""

dct ={}
 
dct["市值"]=4522435.94
 
dct['日期']='2020-05-07'

dct['总份额']=1439346.68

dct['市值']/dct['总份额']

# %%
import collections
Grade = collections.namedtuple('grade',('score','weight'))

# %%
class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
       self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total
# %%
class Student:
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade
