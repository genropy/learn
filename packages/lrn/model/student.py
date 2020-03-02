# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('student', pkey='id', name_long='!![en]Student', 
                    name_plural='!![en]Students',
                    caption_field='name_full',
                    group_card='!![en]Card Info')
        self.sysFields(tbl)
        tbl.column('name', size=':30', name_long='!![en]Name',
                    group='card')
        tbl.column('surname', size=':30', name_long='!![en]Surname',group='card')
        tbl.column('nickname', size=':20', 
                    name_long='!![en]Nickname', 
                    name_short='!![en]Nick')        
        tbl.column('email', name_long='Email',group='card')
        
        tbl.column('country', name_long='!![en]Country',group='card')

        tbl.column('position', name_long='!![en]Geocode')
        tbl.column('locality', name_long='!![en]Locality')
        tbl.column('full_address', name_long='!![en]Full address')

        tbl.column('photo_url',dtype='P', name_long='!![en]Photo')

        tbl.column('user_id',size='22', group='_', name_long='!![en]User',unique=True
                    ).relation('adm.user.id',one_one=True, 
                         relation_name='student', 
                         mode='foreignkey', onDelete='raise')


        tbl.formulaColumn('name_full',"$name || ' ' || $surname")
    
    def createStudent(self,user_record):
        if self.checkDuplicate(user_id=user_record['id']):
            #existing student with the same user_id
            return
        newstudent = self.newrecord(
            name = user_record['firstname'],
            surname = user_record['lastname'],
            email = user_record['email'],
            nickname = user_record['username'],
            user_id = user_record['id'],
        )
        self.insert(newstudent)
