#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('date_approval',width='8em')
        r.fieldcell('date_insert',  name='!![en]Date',width='8em')
        r.fieldcell('subject',width='20em')
        r.fieldcell('description',width='40em')

    def th_order(self):
        return 'subject'

    def th_query(self):
        return dict(column='subject', op='contains', val='')

class ViewTeacher(BaseComponent):
    
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('user_id',width='10em')
        r.fieldcell('date_insert', name='!![en]Date',width='8em')
        r.fieldcell('date_approval',width='8em')
        r.fieldcell('subject',width='20em')
        r.fieldcell('description',width='40em')

    def th_order(self):
        return 'date_insert'
    
    def th_top_custom(self,top):
        top.slotToolbar('*,sections@workflow,*', childname='upper', _position='<bar')
    
    def th_sections_workflow(self):
        return [
            dict(caption='!![en]All'),
            dict(caption='!![en]To Approve', condition='$date_approval IS NULL'),
            dict(caption='!![en]No Topic ',condition='$main_topic_id IS NULL'),
            dict(caption='!![en]No Main Answer ',condition='$main_answer_id IS NULL')]


class Form(BaseComponent):
    py_requires = 'gnrcomponents/attachmanager/attachmanager:AttachManager'
    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record')
        fb = top.formbuilder(cols=1, border_spacing='4px')
        fb.field('subject', width='40em')
        fb.field('main_topic_id',width='40em')
        tc = bc.tabContainer(region='center',margin='2px')
        tab1 = tc.contentPane(title='!![en]Description', datapath='.record')
        tab1.contentPane(title='!![en]Description', region='center').ckeditor(value='^.description')
        tab2 = tc.contentPane(title='!![en]Answers')
        tab2.dialogTableHandler(relation='@answers', viewResource='ViewFromQuestion')
        tab3 = tc.contentPane(title='!![en]Attachments').attachmentMultiButtonFrame()

    def th_options(self):
        return dict(dialog_windowRatio=.8)

class FormNewQuestion(BaseComponent):
    py_requires = 'gnrcomponents/attachmanager/attachmanager:AttachManager'

    def th_form(self, form):
        bc = form.center.borderContainer(datapath='.record')
        top = bc.contentPane(region='top')
        fb = top.formbuilder(cols=1, border_spacing='4px')
        fb.field('subject',width='40em', tag='simpleTextArea', height='50px')
        tc = bc.tabContainer(region='center')

        tc.contentPane(title='!![en]Description', region='center').ckeditor(value='^.description')
        tc.contentPane(title='!![en]Attachments').attachmentMultiButtonFrame()

    def th_options(self):
        return dict(modal=True)
        
    def th_bottom_custom(self, bottom):
        bar = bottom.slotBar('*,revert_btn,save_btn')
        bar.revert_btn.slotButton('!![en]Reset',action='this.form.publish("reload")',disabled='^.controller.changed?=!#v')
        bar.save_btn.slotButton('!![en]Send', action='this.form.publish("save",{destPkey:"*newrecord*",always:true});')