# -*- coding: utf-8 -*-

# includedview_bagstore.py
# Created by Francesco Porcari on 2011-03-23.
# Copyright (c) 2020 Softwell. All rights reserved.
from gnr.core.gnrbag import Bag,BagResolver
from gnr.core.gnrdecorator import public_method

class MeteoResolver(BagResolver):
    apikey='a7c8196b04859197631a803fe3369b3f'
    url="http://api.openweathermap.org/data/2.5/weather?appid=%(apikey)s&q=%(city)s&mode=xml&units=metric"

    def load(self):
        meteo = Bag(self.url%dict(apikey=self.apikey,city=self.city))['current']
        return f"{meteo['weather?value']}, temperature:{meteo['temperature?value']}"

class ResolverGeo(BagResolver):
    classKwargs = {'cacheTime': 300,
                   'regione':None,
                   'provincia':None,
                   '_page': None}

    def load(self):
        if self.regione:
            return self.elencoProvince()
        elif self.provincia:
            return self.elencoComuni()
        else:
            return self.elencoRegioni()

    def elencoComuni(self):
        result = Bag()
        f = self._page.db.table('glbl.comune').query(where='$sigla_provincia=:p',
                                                p=self.provincia).fetch()
        for r in f:
            content = Bag(dict(r))
            content.addItem('meteo',MeteoResolver(city=r['denominazione']),name='Meteo')
            result.addItem(r['id'],content,
                        nome=r['denominazione'],comune_id=r['id'])
        return result

    def elencoProvince(self):
        result = Bag()
        f = self._page.db.table('glbl.provincia').query(where='$regione=:r',r=self.regione).fetch()
        for r in f:
            content = ResolverGeo(_page=self._page,provincia=r['sigla'])
            result.addItem(r['sigla'],content,
                        nome=r['nome'],sigla=r['sigla'])
        return result
    
    def elencoRegioni(self):
        result = Bag()
        regioni_grouped = self._page.db.table('glbl.regione').query().fetchGrouped('zona')
        for zona,regioni in regioni_grouped.items():
            zonabag = Bag()
            result.addItem(zona,zonabag,nome=zona)
            for r in regioni:
                content = ResolverGeo(_page=self._page,regione=r['sigla'])
                zonabag.addItem(r['sigla'],content,nome=r['nome'],sigla=r['sigla'])
        return result


    
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
        pane.tree(storepath='.geodata',labelAttribute='nome')#hideValues=True
        geodata = Bag()
        geodata.addItem('italia',ResolverGeo(_page=self),nome='Italia')
        pane.data('.geodata',geodata)
