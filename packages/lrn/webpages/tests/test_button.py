# -*- coding: utf-8 -*-

# includedview_bagstore.py
# Created by Francesco Porcari on 2011-03-23.
# Copyright (c) 2011 Softwell. All rights reserved.

from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    py_requires="gnrcomponents/testhandler:TestHandlerFull,gnrcomponents/source_viewer/source_viewer:SourceViewer"

    def test_0_simplebutton(self,pane):
        "Simple button alert"
        pane.button('Hello',action='alert("Hello world")')
        pane.textbox(value='^.pippero',lbl='pippero')
    
    def test_1_buttonSet(self,pane):
        "Simple button che setta"
        pane.textbox('^.value',lbl='My value')
        pane.button('Set value',action='SET .myvalue=v',v='=.value')
        pane.div('^.myvalue')
    
    def test_2_buttonAsk(self,pane):
        pane.button('Set value',action='SET .myvalue=myvalue',
                    ask=dict(title='Which one',fields=[dict(name='myvalue',lbl='My value')]))
        pane.div('^.myvalue')