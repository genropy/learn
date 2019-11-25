# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('topic', pkey='id', name_long='!![en]Topic', 
                        name_plural='!![en]Topics',
                        caption_field='description')
        self.sysFields(tbl,hierarchical='description',
                        counter=True) #hierarchical_description
        tbl.column('description', size=':40', name_long='!![en]Description')
