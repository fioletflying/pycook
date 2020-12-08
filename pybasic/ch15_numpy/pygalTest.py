#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @author   : Feifei
# @IDE      : Pycharm
# @file     : pygalTest.py
# @time     : 2019/6/27 14:41


from Die import Die
import  pygal


die = Die()


results = []

for roll_num in range(1000):
  result = die.roll()
  results.append(result)

print(results)


frequencies = []

for value in range(1,die.num_sides+1):
  frequency = results.count(value)
  frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()

hist.title="test"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "frequency of result"

hist.add('D6',frequencies)
hist.render_to_file('die_visul.svg')




