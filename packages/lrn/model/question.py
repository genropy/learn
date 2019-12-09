# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('question', pkey='id', name_long='!![en]Question', name_plural='!![en]Questions',caption_field='subject')
        self.sysFields(tbl)
        tbl.column('subject',size=':60',name_long='!![en]Subject')
        tbl.column('description', name_long='!![en]Description')
        tbl.column('html_description', name_long='!![en]Html Description')
        tbl.column('main_topic_id',size='22', group='_', name_long='!![en]Main topic'
                    ).relation('topic.id', 
                                relation_name='questions', 
                                mode='foreignkey', 
                                onDelete='raise')
        tbl.column('user_id',size='22', group='_', name_long='!![en]User'
                    ).relation('adm.user.id', relation_name='myquestions', 
                                mode='foreignkey', onDelete='raise')

        