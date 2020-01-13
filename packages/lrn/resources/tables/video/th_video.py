#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('title',width='20em')
        r.fieldcell('description',width='30em')
        r.fieldcell('streaming_service', width='12em')
        r.fieldcell('main_topic_id', width='15em')
        r.fieldcell('external_id', width='8em')
        r.fieldcell('video_url', cell_format='autolink', width='30em')

    def th_order(self):
        return 'title'

    def th_query(self):
        return dict(column='title', op='contains', val='')

    def th_queryBySample(self):
        return dict(fields=[dict(field='title',lbl='!![en]Title',width='12em'),
                            dict(field='@main_topic_id.description', lbl='!![en]Main Topic', width='14em')],
                    cols=2, 
                    isDefault=True)

class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer() 
        top = bc.borderContainer(region='top',datapath='.record',height='150px')

        fb = top.div(margin_right='20px', width='600px').formbuilder(cols=3, border_spacing='4px', width='100%', fld_width='100%', colswidth='auto')
        fb.field('title', colspan=2)
        fb.field('streaming_service')
        fb.field('main_topic_id', colspan=2)
        fb.field('external_id' )
        fb.field('description', colspan=3, tag='simpleTextArea', height='70px')
        
        
        bc.contentPane(region='center').dialogTableHandler(relation='@clips', 
                                    dialog_parentRatio=.9,
                                    viewResource='ViewFromVideo')

    def th_options(self):
        return dict(dialog_height='500px', dialog_width='650px' )
