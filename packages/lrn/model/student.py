# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('student', pkey='id', name_long='!![en]Student', 
                    name_plural='!![en]Students',
                    caption_field='name_full')
        self.sysFields(tbl)
        tbl.column('name', size=':30', name_long='!![en]Name')
        tbl.column('surname', size=':30', name_long='!![en]Surname')
        tbl.column('nickname', size=':20', 
                    name_long='!![en]Nickname', 
                    name_short='!![en]Nick')        
        tbl.column('email', name_long='Email')
        tbl.formulaColumn('name_full',"$name || ' ' || $surname")