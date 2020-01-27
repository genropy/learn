# -*- coding: utf-8 -*-
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    py_requires = 'miocomponent:GestoreAnagrafiche'

    def main(self,root,color='gray',**kwargs):
        #metto dei dati di partenza
        root.data('main.dati_anagrafici', Bag(nome='Anselmo', cognome='Rossi'))

        pane = root.contentPane(datapath='main.dati_anagrafici')
        fb = pane.formbuilder(cols=2, nodeId='miaform')
        fb.textbox('^.nome', lbl='Nome')
        fb.textbox('^.cognome', lbl='Cognome')
        fb.button('Premi', action="alert('Ciao '+ nome +' '+cognome)",
                    nome='=#miaform.nome', 
                    cognome='=#miaform.cognome')
    
    

        