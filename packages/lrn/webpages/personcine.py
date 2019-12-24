# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    py_requires = 'miocomponent:GestoreAnagrafiche'

    def main(self,root,persone=None,**kwargs):
        if not persone:
            root.div('Mancano personcine')
            return
        for persona in persone.split(','):
            root.anagraficaCompleta(persona=persona)
