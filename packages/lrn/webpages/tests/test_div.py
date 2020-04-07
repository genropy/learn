# -*- coding: utf-8 -*-

# includedview_bagstore.py
# Created by Francesco Porcari on 2011-03-23.

from gnr.core.gnrdecorator import public_method

"Test HTML DIV"

class GnrCustomWebPage(object):
    py_requires="gnrcomponents/testhandler:TestHandlerFull,gnrcomponents/source_viewer/source_viewer:SourceViewer" 

    def test_0_helloworld(self,pane):
        "Hello world test"
        pane.data('.mytext','Hello world')
        pane.div('^.mytext',font_size='15px')

    def test_1_helloworld_dynamic(self,pane):
        "Hello world dynamic"
        pane.textbox(value='^.mytext')
        pane.div('^.mytext',font_size='15px')

    def test_2_helloworld_dynamic(self,pane):
        "Hello world font-size dynamic"
        fb = pane.formbuilder()
        fb.textbox(value='^.mytext',lbl='Content')
        fb.textbox(value='^.font_size',lbl='Font size')
        fb.div('^.mytext',font_size='^.font_size')