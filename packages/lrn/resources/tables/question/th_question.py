#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('subject',width='20em')
        r.fieldcell('description',width='40em')

    def th_order(self):
        return 'subject'

    def th_query(self):
        return dict(column='subject', op='contains', val='')



class Form(BaseComponent):
    py_requires = 'gnrcomponents/attachmanager/attachmanager:AttachManager'
    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record')
        fb = top.formbuilder(cols=1, border_spacing='4px')
        fb.field('subject',width='40em')
        fb.field('main_topic_id',width='40em')
        fb.field('description',tag='simpleTextArea',
                    heigth='60px',width='40em')
        tc = bc.tabContainer(region='center',margin='2px')
        tab1 = tc.contentPane(title='!![en]Html Description')
        tab1.simpleTextArea(value='^.record.html_description',editor=True)
        tab2 = tc.contentPane(title='!![en]Answers')
        tab2.dialogTableHandler(relation='@answers')
        tab3 = tc.contentPane(title='!![en]Attachments').attachmentMultiButtonFrame()


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
