# -*- coding: utf-8 -*-

# includedview_bagstore.py
# Created by Francesco Porcari on 2011-03-23.

from gnr.core.gnrdecorator import public_method

"Test HTML DIV"

class GnrCustomWebPage(object):
    py_requires="gnrcomponents/testhandler:TestHandlerFull,gnrcomponents/source_viewer/source_viewer:SourceViewer" 

    def test_0_connessione(self,pane):
        """Connessione ad eventi"""
        pane.data('.messaggio','Hello world')
        pane.data('.background','green')
        pane.div('^.messaggio',font_size='20px',height='200px',width='400px',rounded=12,
                    text_align='center',color='navy',
                    background='^.background',
                    connect_onclick="this.setRelativeData('.messaggio','Mi hai cliccato');",
                    connect_onmouseenter='this.updAttributes({font_size:"40px"})',
                    connect_onmouseout='this.updAttributes({font_size:"20px"})'
                    )


    def test_1_button(self,pane):
        pane.button('Debugger',
                        action="genro.bp(true)",
                        nome='Luigi')
        pane.button('Set nome',
                        action="SET .messaggio = nome;",
                        nome='Luigi')
        pane.div('^.messaggio',lbl='Messaggio')


    def test_2_button(self,pane):
        fb = pane.formbuilder()
        fb.textbox(value='^.nome',lbl='Nome')
        fb.textbox(value='^.cognome',lbl='Cognome')

        fb.button('Azione',
                        action="SET .messaggio = cognome+' '+nome;",
                        cognome='=.cognome',nome='=.nome')
        fb.div('^.messaggio',lbl='Messaggio')

    def test_3_button(self,pane):
        fb = pane.formbuilder()
        fb.textbox(value='^.nome',lbl='Nome')
        fb.textbox(value='^.cognome',lbl='Cognome')

        fb.button('Azione',
                        action="""SET .messaggio = GET .cognome+' '+GET .nome;"""
                        #this.setRelativeData('.messaggio',this.getRelativeData('.cognome')+' '+this.getRelativeData('.nome'))
                        )
        fb.div('^.messaggio',lbl='Messaggio')


    def test_4_button(self,pane):
        fb = pane.formbuilder()

        fb.button('Azione',
                    ask=dict(title='Dammi le info',
                            fields=[dict(name='nome',lbl='Nome'),
                                    dict(name='cognome',lbl='Cognome'),
                                    dict(name='sesso',lbl='Sesso',tag='filteringSelect',
                                        values='M:Maschio,F:Femmina')]),
                        action="""SET .messaggio = cognome +' '+ nome + ' - '+sesso;""")
        fb.div('^.messaggio',lbl='Messaggio')

    def test_5_button(self,pane):
        fb = pane.formbuilder()
        box = fb.div(height='40px',width='40px',background='red')
        fb.button('Cambia colore',
                    action='box.updAttributes({background:"green"})',
                    box=box)


    def test_6_datacontroller(self,pane):
        fb = pane.formbuilder()
        fb.numberTextBox(value='^.base',lbl='Base',default=0)
        pane.dataController("""SET .base = currbase + 1;""",
                        _timing=1,currbase='=.base')

    def test_7_dataFormula(self,pane):
        fb = pane.formbuilder()
        fb.numberTextBox(value='^.base',lbl='Base',default=0)
        fb.numberTextBox(value='^.altezza',lbl='Altezza',default=0)
        fb.filteringSelect(value='^.poligono',lbl='Poligono',
                values='q:Quadrato,t:Triangolo',default='t')
        fb.div('^.area')
        pane.dataFormula('.area',"""poligono=='t'? base*altezza/2 : base*altezza;""",
                        base='^.base',
                        altezza='^.altezza',
                        poligono='^.poligono')
        
    
    def test_8_datacontroller(self,pane):
        fb = pane.formbuilder()
        fb.numberTextBox(value='^.base',lbl='Base',default=0)
        fb.numberTextBox(value='^.altezza',lbl='Altezza',default=0)
        fb.div('^.area',lbl='Area')
        fb.div('^.perimetro',lbl='Perimetro')
        pane.dataController("""SET .area = base * altezza;
                            SET .perimetro = (base+altezza)*2;""",
                        base='^.base',altezza='^.altezza')
        