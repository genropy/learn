#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    auto = root.branch("!![en]Learn")
    auto.thpage("!![en]Students", table="lrn.student")
    auto.thpage("!![en]Topics", table="lrn.topic")
    auto.thpage("!![en]Questions", table="lrn.question")
    auto.thpage("!![en]Videos", table="lrn.video")
    auto.thpage("!![en]Clips", table="lrn.clip")
    auto.thpage("!![en]Review Questions", table="lrn.question", viewResource='ViewReview', formResource='FormReview')
    auto.webpage("!![en]My Page",filepath="/lrn/student" )
    auto.lookups('Lookup tables',lookup_manager='lrn')

