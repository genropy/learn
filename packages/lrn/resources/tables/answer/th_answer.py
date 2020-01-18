#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('date_insert')
        r.fieldcell('date_approval')
        r.fieldcell('user_id')
        r.fieldcell('question_id')
        r.fieldcell('answer_text')
        #r.fieldcell('html_description')

    def th_order(self):
        return 'date_insert'

    def th_query(self):
        return dict(column='question_id', op='contains', val='')


class ViewFromQuestion(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('id', hidden=True)
        r.fieldcell('date_insert',  width='9em')
        r.fieldcell('date_approval',  width='9em')
        r.fieldcell('user_id', width='10em')
        r.fieldcell('answer_text', width='30em')

        r.checkboxcolumn('main', name='Main',
                        checkedField='id',
                          checkedId='#FORM.record.main_answer_id',
                          radioButton=True, width='3em')

    def th_order(self):
        return 'date_insert'
        
class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer(datapath='.record')
        fb = bc.contentPane(region='top').formbuilder(cols=2, border_spacing='4px')
        fb.field('question_id')
        #fb.field('description',width='40em')
        bc.contentPane(region='center').simpleTextArea(value='^.description',editor=True)


    def th_options(self):
        return dict(dialog_parentRatio=.8,modal=True)
