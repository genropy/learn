# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('answer', pkey='id', name_long='!![en]Answer', 
                        name_plural='!![en]Answers',
                        caption_field='description')
        self.sysFields(tbl)
        tbl.column('question_id',size='22', group='_', name_long='!![en]Question'
                    ).relation('question.id', relation_name='answers',
                                    mode='foreignkey', 
                                    onDelete='cascade')
        tbl.column('description', name_long='!![en]Description')
        tbl.column('html_description', name_long='!![en]Html Description')