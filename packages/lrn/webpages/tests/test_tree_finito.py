# -*- coding: utf-8 -*-

# includedview_bagstore.py
# Created by Francesco Porcari on 2011-03-23.
# Copyright (c) 2020 Softwell. All rights reserved.
from gnr.core.gnrbag import Bag,BagResolver
from gnr.core.gnrdecorator import public_method

class ResolverGeo(BagResolver):
    classKwargs = {'cacheTime': 300,
                   'regione':None,
                   'provincia':None,
                   'comune_id':None,
                   '_page': None}

    def load(self):
        if self.comune_id:
            print(self.comune_id)
        elif self.provincia:
            return self.elencoComuni()
        elif self.regione:
            return self.elencoProvince()
        else:
            return self.elencoRegioni()
    
    def elencoRegioni(self):
        result = Bag()
        regioni_grouped = self._page.db.table('glbl.regione').query().fetchGrouped('zona')
        for zona,regioni in regioni_grouped.items():
            zonabag = Bag()
            result.addItem(zona,zonabag,nome=zona)
            for r in regioni:
                zonabag.addItem(r['sigla'],ResolverGeo(_page=self._page,regione=r['sigla'],nome=r['nome'],sigla=r['sigla']))
        return result

    
    def elencoProvince(self):
        result = Bag()
        f = self._page.db.table('glbl.provincia').query(
            where='$regione=:r',r=self.regione
        ).fetch()
        for r in f:
            result.addItem(r['sigla'],ResolverGeo(_page=self._page,provincia=r['sigla']),nome=r['nome'],sigla=r['sigla'])
        return result
    
    def elencoComuni(self):
        print(x)

    
    def resolverSerialize(self):
        self._initKwargs.pop('_page')
        return BagResolver.resolverSerialize(self)

class GnrCustomWebPage(object):
    py_requires="""gnrcomponents/testhandler:TestHandlerFull,
                gnrcomponents/framegrid:FrameGrid"""
    
    def test_01_tree_res(self,pane):
        """
        tree resolver
        """
        pane.tree(storepath='.geodata',labelAttribute='nome',hideValues=True)
        geodata = Bag()
        geodata.addItem('italia',ResolverGeo(_page=self),nome='Italia')
        pane.data('.geodata',geodata)
