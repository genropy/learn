#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('user_id')
        r.fieldcell('approval_ts')
        r.fieldcell('question_id')
        r.fieldcell('answer')
        #r.fieldcell('html_description')

    def th_order(self):
        return '__ins_ts'

    def th_query(self):
        return dict(column='question_id', op='contains', val='')


class ViewFromQuestion(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('id', hidden=True)
        r.fieldcell('__ins_ts', dtype='D',  width='9em')
        r.fieldcell('approval_ts',  width='9em')
        r.fieldcell('user_id', width='10em')
        r.fieldcell('answer', width='30em')

        r.checkboxcolumn('main', name='Main',
                        checkedField='id',
                          checkedId='#FORM.record.main_answer_id',
                          radioButton=True, width='3em')

    def th_order(self):
        return '__ins_ts'
        
class Form(BaseComponent):
    py_requires = 'gnrcomponents/attachmanager/attachmanager:AttachManager'

    def th_form(self, form):
        bc = form.center.borderContainer()
        bc.contentPane(region='left',padding='2px', width='50%').simpleTextArea(height='390px', datapath='.record')
        bc.contentPane(region='center').attachmentMultiButtonFrame()


    def th_options(self):
        return dict(dialog_parentRatio=.9, modal=True)
