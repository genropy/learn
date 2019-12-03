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
        pane = form.record 
        fb = pane.formbuilder(cols=1,border_spacing='4px',
                            margin='10px')
        fb.field('nickname')
        fb.field('name')
        fb.field('surname')
        fb.field('email',width='30em')
        fb.field('full_address',
                width='50em',
                selected_locality='.locality',
                selected_country='.country',
                selected_position='.position',
                tag='geoCoderField')
        fb.field('locality')
        fb.field('country')
        fb.field('position')

        fb.img(src='^.photo_url',
                crop_height='100px',
                crop_width='100px',
                margin='5px',
                crop_border='2px dotted silver',
                crop_rounded=6,edit=True,
                placeholder=True,
                upload_folder='site:students/avatars',
                upload_filename='=#FORM.record.nickname')
        


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
