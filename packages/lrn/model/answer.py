# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('answer', pkey='id', name_long='!![en]Answer', 
                        name_plural='!![en]Answers',
                        caption_field='answer_text')
        self.sysFields(tbl)
        tbl.column('question_id',size='22', group='_', name_long='!![en]Question'
                    ).relation('question.id', relation_name='answers',
                                    mode='foreignkey', 
                                    onDelete='cascade')
        tbl.column('answer_text', name_long='!![en]Answer text')
        tbl.column('date_insert', dtype='D', name_long='!![en]Insert date')
        tbl.column('date_approval', dtype='D', name_long='!![en]Approval date')
        tbl.column('user_id',size='22', group='_', name_long='!![en]User'
                    ).relation('adm.user.id', relation_name='myanswers', 
                                mode='foreignkey', onDelete='raise')

        #tbl.column('html_description', name_long='!![en]Html Description')

    def defaultValues(self):
        return dict(date_insert=self.db.workdate, user_id=self.db.currentEnv.get('user_id'))


        