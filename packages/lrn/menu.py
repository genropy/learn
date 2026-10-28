#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    learn = root.branch("!![en]Learn")
    learn.thpage("!![en]Students", table="lrn.student")
    learn.thpage("!![en]Topics", table="lrn.topic")
    learn.thpage("!![en]Videos", table="lrn.video")
    learn.thpage("!![en]Clips", table="lrn.clip")
    learn.thpage("!![en]Contest Subscriptions", table="lrn.contest_subscription")
    learn.thpage("!![en]Review Questions", table="lrn.question", viewResource='ViewReview', formResource='FormReview')
    learn.webpage("!![en]My Page",filepath="/lrn/student" )
    learn.lookups('Lookup tables',lookup_manager='lrn')
    learn.branch("!![en]Local tests", dir="tests",pkg='lrn')

