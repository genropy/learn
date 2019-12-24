# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    py_requires = 'miocomponent:GestoreAnagrafiche'

    def main(self,root,color='gray',**kwargs):
        root.div('Hello',color=color)
    
    

        