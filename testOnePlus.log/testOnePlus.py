# -*- encoding=utf8 -*-
__author__ = "gouchang"

from airtest.core.api import *

auto_setup(__file__)

keyevent("POWER")

swipe(Template(r"tpl1536809069232.png", record_pos=(-0.003, 1.017), resolution=(1080.0, 2280.0)), vector=[0, -0.6])
touch(Template(r"tpl1536809073595.png", record_pos=(-0.006, 0.643), resolution=(1080.0, 2280.0)))
touch(Template(r"tpl1536809082045.png", record_pos=(0.373, -0.312), resolution=(1080.0, 2280.0)))

wait(Template(r"tpl1536822489038.png", record_pos=(0.43, 0.179), resolution=(2280, 1080)))

#exists(Template(r"tpl1536822489038.png", record_pos=(0.43, 0.179), resolution=(2280, 1080)))


keyevent("HOME")

touch(Template(r"tpl1536822721821.png", record_pos=(-0.201, 0.983), resolution=(1080, 2280)))

swipe(Template(r"tpl1536822776675.png", record_pos=(-0.381, -0.696), resolution=(1080, 2280)), vector=[0.5, 0],duration=0.05)

keyevent("POWER")
