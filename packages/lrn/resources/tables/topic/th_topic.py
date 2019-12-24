#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('description')

    def th_order(self):
        return 'description'

    def th_query(self):
        return dict(column='description', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record')
        fb = top.formbuilder(cols=2, border_spacing='4px')
        fb.field('description')
        centerTc = bc.tabContainer(region='center', margin_left='6px')
        self.questionsTab(centerTc.contentPane(title='!![en]Questions'), form=form)
        self.videosTab(centerTc.contentPane(title='!![en]Videos'), form=form)
        self.clipsTab(centerTc.contentPane(title='!![en]Clips'), form=form)


    
    def questionsTab(self, pane, form):
        th = pane.dialogTableHandler(relation='@questions')
        form.htree.relatedTableHandler(th,inherited=True)

    def videosTab(self, pane, form):
        th = pane.dialogTableHandler(relation='@videos')
        form.htree.relatedTableHandler(th,inherited=True)

    def clipsTab(self, pane, form):
        th = pane.dialogTableHandler(relation='@clips')
        form.htree.relatedTableHandler(th,inherited=True)

    def th_options(self):
        return dict(dialog_height='500px', 
                    dialog_width='650px',
                    hierarchical=True)
