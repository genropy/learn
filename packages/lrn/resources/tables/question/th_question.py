#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method,metadata

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('question',width='20em')
        r.fieldcell('description',width='40em')
        r.fieldcell('user_id',width='10em')
        r.fieldcell('__ins_ts', dtype='D', name='!![en]Date',width='8em')

    def th_order(self):
        return '__ins_ts'

    def th_query(self):
        return dict(column='question', op='contains', val='', runOnStart=True)

class ViewStatus(View):
    
    def th_top_custom(self,top):
        top.slotToolbar('*,sections@status,*', childname='upper', _position='<bar')
    
    @metadata(isMain=True)
    def th_sections_status(self):
        return [ dict(caption='!![en]All', includeDraft=True),
                 dict(caption='!![en]To approve', condition='$__is_draft IS TRUE', includeDraft=True),
                 dict(caption='!![en]Approved')]

class ViewReview(View):
    
    def th_top_custom(self,top):
        top.slotToolbar('*,sections@workflow,*', childname='upper', _position='<bar')
    
    @metadata(isMain=True)
    def th_sections_workflow(self):
        return [
            dict(caption='!![en]All', includeDraft=True),
            dict(caption='!![en]To approve', condition='$__is_draft IS TRUE', includeDraft=True),
            dict(caption='!![en]No topic', condition='$main_topic_id IS NULL'),
            dict(caption='!![en]No main answer', condition='$main_answer_id IS NULL')]

class Form(BaseComponent):
    py_requires = 'gnrcomponents/attachmanager/attachmanager:AttachManager'

    def th_form(self, form):
        bc = form.center.borderContainer()
        self.questionForm(bc.contentPane(region='top',datapath='.record'))
        self.questionTabs(bc.tabContainer(region='center',margin='2px'))
        
    def questionTabs(self, tc):
        tc.contentPane(title='!![en]Details', datapath='.record', region='center').ckeditor(value='^.details')
        tc.contentPane(title='!![en]Attachments').attachmentMultiButtonFrame()
        tc.contentPane(title='!![en]Answers').dialogTableHandler(relation='@answers', viewResource='ViewFromQuestion')

    def questionForm(self, pane):
        fb = pane.formbuilder(cols=1, border_spacing='4px')
        fb.field('question', width='40em')
        fb.field('description', width='40em', tag='simpleTextArea', height='50px')
        fb.field('main_topic_id',width='40em', readOnly=True)

    def th_options(self):
        return dict(dialog_windowRatio=.8)

class FormMyQuestion(Form):

    def questionTabs(self, tc):
        tc.contentPane(title='!![en]Details', datapath='.record', region='center').ckeditor(value='^.details')
        tc.contentPane(title='!![en]Attachments').attachmentMultiButtonFrame()
        tc.contentPane(title='!![en]Answers').plainTableHandler(relation='@answers', viewResource='ViewFromQuestion')
        
    def th_options(self):
        return dict(modal=True)

class FormStudente(Form):

    def questionTabs(self, tc):
        tc.contentPane(title='!![en]Details', datapath='.record', region='center').ckeditor(value='^.details')
        tc.contentPane(title='!![en]Attachments').attachmentMultiButtonFrame()
        tc.contentPane(title='!![en]Answers').plainTableHandler(relation='@answers', viewResource='ViewFromQuestion')
        pane = tc.contentPane(title='!![en]Answer this question')
        pane.div('WORK IN PROGRESS')

class FormReview(Form):

    def questionForm(self, pane):
        fb = pane.formbuilder(cols=1, border_spacing='4px')
        fb.field('question', width='40em')
        fb.field('description', width='40em', tag='simpleTextArea', height='50px')
        fb.field('main_topic_id', width='40em', tag='hdbselect')
        fb.button('!![en]Approve', 
                    parentForm=True, action="""this.form.setDraft(false);
                                                this.form.save()""",
                                                hidden='^.approval_ts')

class FormNewQuestion(BaseComponent):
    py_requires = 'gnrcomponents/attachmanager/attachmanager:AttachManager'

    def th_form(self, form):
        bc = form.center.borderContainer(datapath='.record')
        top = bc.contentPane(region='top')
        fb = top.formbuilder(cols=1, border_spacing='4px')
        fb.field('question',width='40em')
        fb.field('description', width='40em', tag='simpleTextArea', height='50px')
        tc = bc.tabContainer(region='center')

        tc.contentPane(title='!![en]Details', region='center').ckeditor(value='^.details')
        tc.contentPane(title='!![en]Attachments').attachmentMultiButtonFrame()

    def th_options(self):
        return dict(modal=True)
        
    def th_bottom_custom(self, bottom):
        bar = bottom.slotBar('*,revert_btn,save_btn')
        bar.revert_btn.slotButton('!![en]Reset',action='this.form.publish("reload")',disabled='^.controller.changed?=!#v')
        bar.save_btn.slotButton('!![en]Send', action='this.form.publish("save",{destPkey:"*newrecord*",always:true});')