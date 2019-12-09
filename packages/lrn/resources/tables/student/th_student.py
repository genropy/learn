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
        r.fieldcell('email')

    def th_order(self):
        return 'nickname'

    def th_query(self):
        return dict(column='nickname', op='contains', val='')

class Form(BaseComponent):
    def th_form(self, form):
        bc = form.center.borderContainer() 
        top = bc.borderContainer(region='top',datapath='.record',height='180px')
        top.contentPane(region='right',padding='10px').img(src='^.photo_url',
                crop_height='150px',
                crop_width='150px',
                crop_border='2px dotted silver',
                crop_rounded=6,edit=True,
                placeholder=True,
                upload_folder='site:students/avatars',
                upload_filename='=#FORM.record.nickname')
        fb = top.contentPane(region='center').formbuilder(cols=2,border_spacing='4px',
                            margin='10px')
        fb.field('nickname',readOnly=True)
        fb.br()
        fb.field('name')
        fb.field('surname')
        fb.field('email',width='30em',colspan=2)
        fb.field('full_address',colspan=2,
                width='30em',
                selected_locality='.locality',
                selected_country='.country',
                selected_position='.position',
                tag='geoCoderField')
        fb.field('locality')
        fb.field('country')
        bc.contentPane(region='center')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

class FormStudentPage(Form):
    def th_options(self):
        return dict(showtoolbar=False,autoSave=True)
