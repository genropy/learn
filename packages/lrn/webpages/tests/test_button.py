# -*- coding: utf-8 -*-

# includedview_bagstore.py
# Created by Francesco Porcari on 2011-03-23.
# Copyright (c) 2011 Softwell. All rights reserved.

from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    py_requires="gnrcomponents/testhandler:TestHandlerFull"

    def test_0_simplebutton(self,pane):
        "Simple button alert"
        pane.textbox('^.message',lbl='Message')
        pane.button('Hello',action='alert(message)',
                        message='=.message')
    
    def test_1_buttonSet(self,pane):
        "Copy value"
        fb = pane.formbuilder()
        fb.textbox('^.sorgente',lbl='Sorgente')
        fb.button('Copia',action='SET .destinazione = v;',
                    v='=.sorgente')
        fb.textbox('^.destinazione',lbl='Destinazione')
    
    def test_2_buttonAsk(self,pane):
        "Button with ask"
        pane.button('Set value',
                    action="""SET .myvalue = myvalue;
                              SET .mycolor = mycolor;""",
                        ask=dict(title='Which one',
                                fields=[dict(name='myvalue',lbl='My value',
                                            validate_notnull=True),
                                        dict(name='mycolor',lbl='Color',
                                                tag='combobox',
                                                values='orange,green,blue')])
                                )
        pane.div('^.myvalue',color='^.mycolor')