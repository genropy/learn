#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('title', width='20em')
        r.fieldcell('video_id')
        r.fieldcell('topic_id', width='20em', name='!![en]Main topic')
        r.fieldcell('other_topics', width='20em',name='!![en]Other topics')
        r.fieldcell('time_code', width='6em')
        r.fieldcell('clip_url', format_showlinks=True, width='20em')

    def th_order(self):
        return 'title'

    def th_query(self):
        return dict(column='title', op='contains', val='')

    def th_queryBySample(self):
        return dict(fields=[dict(field='title',lbl='!![en]Title',width='12em'),
                            dict(field='@topic_id.description', lbl='Main Topic',width='14em'),
                            dict(field='other_topics',lbl='!![en]Other topics',width='16em')],
                    cols=3, 
                    isDefault=True)

class ViewFromVideo(BaseComponent):
    
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('title', width='20em')
        r.fieldcell('topic_id', width='20em')
        r.fieldcell('other_topics', width='20em',name='!![en]Other topics')
        r.fieldcell('time_code', width='6em')
        r.fieldcell('clip_url', format_showlinks=True, width='20em')

class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer(datapath='.record')
        fb = bc.contentPane(region='top').div(width='580px', margin_right='20px').formbuilder(cols=2, border_spacing='4px', 
                                                                    fld_width='100%', colswidth='auto')
        fb.field('title' , colspan=2)
        fb.field('video_id',)
        fb.field('time_code', width='5em')
        fb.field('topic_id', colspan=2, tag='hdbselect')
        bc.contentPane(region='center').iframe(src='^.clip_embedded_url',
                    height='100%',width='100%',border='0',_virtual_column='$video_embedded_url')
    @public_method
    def th_onLoading(self, record, newrecord, loadingParameters, recInfo):
        if record['video_embedded_url']:
            z = (['0','0','0']+record['time_code'].replace('s','').replace('m',':').replace('h',':').split(':'))[-3:]
            sec = int(z[0])*3600+int(z[1])*60+int(z[2])
            record['clip_embedded_url'] = '{video_embedded_url}?start={sec}'.format(video_embedded_url=record['video_embedded_url'],sec=sec)

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
