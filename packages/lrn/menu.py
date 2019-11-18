#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    auto = root.branch(u"auto")
    auto.thpage(u"!!Student", table="lrn.student")

