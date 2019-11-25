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
        tbl.column('provincia',size='2', name_long='!![it]Provincia'
                    ).relation('glbl.provincia.sigla', 
                                relation_name='studenti',
                                mode='foreignkey', 
                                onDelete='raise')
        tbl.column('comune_id',size='22', name_long='!![it]Comune'
                    ).relation('glbl.comune.id', 
                                relation_name='studenti',
                                mode='foreignkey', 
                                onDelete='raise')
        tbl.column('photo_url',dtype='P', name_long='Photo')
        tbl.formulaColumn('name_full',"$name || ' ' || $surname")