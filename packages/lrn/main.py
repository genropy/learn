#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='lrn package',
                    sqlschema='lrn',sqlprefix=True,
                    name_short='Lrn', name_long='Lrn', 
                    name_full='Lrn')
                    
    def config_db(self, pkg):
        pass

    def custom_type_money(self):
        return dict(dtype='N',format='#,###.00')

    def custom_type_percent(self):
        return dict(dtype='N',format='##.00')

        
class Table(GnrDboTable):
    def lrn_whoIAm(self):
        return self.fullname

class WebPage(object):
    def learnDiv(self,pane):
        pane.div('Io sono la pagina di learn')