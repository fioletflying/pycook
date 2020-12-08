#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @author   : Feifei
# @IDE      : Pycharm
# @file     : Die.py
# @time     : 2019/6/27 14:45

from random import randint

class Die():
  """表示骰子"""
  def __init__(self,num_sides=6):
    self.num_sides = num_sides


  def roll(self):
    return randint(1,self.num_sides)

