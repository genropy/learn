#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='lrn package',sqlschema='lrn',sqlprefix=True,
                    name_short='Lrn', name_long='Lrn', name_full='Lrn')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
