#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    auto = root.branch("!![en]Learn")
    auto.thpage("!![en]Student", table="lrn.student")

