# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'

    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='main')