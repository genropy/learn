#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('question_id')
        r.fieldcell('description')
        r.fieldcell('html_description')

    def th_order(self):
        return 'question_id'

    def th_query(self):
        return dict(column='question_id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer(datapath='.record')
        fb = bc.contentPane(region='top').formbuilder(cols=2, border_spacing='4px')
        fb.field('question_id')
        fb.field('description',width='40em')
        bc.contentPane(region='center').simpleTextArea(value='^.html_description',editor=True)


    def th_options(self):
        return dict(dialog_parentRatio=.8,modal=True)
