#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nickname')
        r.fieldcell('name')
        r.fieldcell('surname')
        r.fieldcell('provincia')
        r.fieldcell('comune_id')
        r.fieldcell('email')

    def th_order(self):
        return 'nickname'

    def th_query(self):
        return dict(column='nickname', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record 
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('nickname')
        fb.field('name')
        fb.field('surname')
        fb.field('provincia',hasDownArrow=False)
        #fb.dbSelect(value='^.provincia',dbtable='glbl.provincia',lbl='Provincia',hasDownArrow=False)
        fb.field('comune_id',condition='$sigla_provincia=:pr',
                    condition_pr='=.provincia')
        fb.field('email')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
