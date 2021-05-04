#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('date')
        r.fieldcell('email')
        r.fieldcell('fullname')
        r.fieldcell('name')
        r.fieldcell('description')
        r.fieldcell('video_link')

    def th_order(self):
        return 'date'

    def th_query(self):
        return dict(column='fullname', op='contains', val='')

class Form(BaseComponent):
    def th_form(self, form):
        bc = form.center.borderContainer(datapath='.record')
        fb = bc.formbuilder(cols=2, border_spacing='4px', margin='10px')
        fb.field('date',readOnly=True)
        fb.field('email')
        fb.field('fullname')
        fb.field('name')
        fb.simpletextarea('^.description', lbl='Project description', colspan=2,
                                width='100%', height='100px')
        fb.field('video_link', colspan=2)

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')