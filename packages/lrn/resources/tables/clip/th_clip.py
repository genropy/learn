#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('title', edit=True, width='20em')
        r.fieldcell('video_id')
        r.fieldcell('topic_id', edit=True, width='20em')
        r.fieldcell('time_code', edit=True, width='6em')
        r.fieldcell('keywords', edit=dict(tag='simpleTextArea', height='70px'), width='20em')
        r.fieldcell('clip_url', cell_format='autolink', width='20em')


    def th_order(self):
        return 'title'

    def th_query(self):
        return dict(column='title', op='contains', val='')

    def th_queryBySample(self):
        return dict(fields=[dict(field='keywords',lbl='!![en]Keywords',width='16em'),
                            dict(field='title',lbl='!![en]Title',width='12em'),
                            dict(field='@topic_id.description', lbl='Topic',width='14em')],
                    cols=3, 
                    isDefault=True)


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.div(width='580px', margin_right='20px').formbuilder(cols=2, border_spacing='4px', 
                                                                    fld_width='100%', colswidth='auto')
        fb.field('title' , colspan=2)
        fb.field('video_id',)
        fb.field('time_code', width='5em')
        fb.field('topic_id', colspan=2, tag='hdbselect')
        fb.field('keywords' , colspan=2, tag='simpleTextArea', height='60px')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
