#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    auto = root.branch("!![en]Learn")
    auto.thpage("!![en]Students", table="lrn.student")
    auto.thpage("!![en]Topics", table="lrn.topic")
    auto.thpage("!![en]Questions", table="lrn.question")

