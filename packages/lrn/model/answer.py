# encoding: utf-8
from datetime import datetime

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('answer', pkey='id', name_long='!![en]Answer', 
                        name_plural='!![en]Answers',
                        caption_field='answer', draftField=True)
        self.sysFields(tbl, draftField=True)
        tbl.column('question_id',size='22', group='_', name_long='!![en]Question'
                    ).relation('question.id', relation_name='answers',
                                    mode='foreignkey', 
                                    onDelete='cascade')
        tbl.column('answer', name_long='!![en]Answer')
        tbl.column('approved_by_user_id', size='22', group='_', name_long='!![en]Approved by'
                    ).relation('adm.user.id', 
                                relation_name='approved_answers', 
                                mode='foreignkey', onDelete='raise')
        tbl.column('approval_ts', dtype='DH', name_long='!![en]Approval TS')
        tbl.column('user_id',size='22', group='_', name_long='!![en]User'
                    ).relation('adm.user.id', relation_name='myanswers', 
                                mode='foreignkey', onDelete='raise')

    def defaultValues(self):
        user_id = self.db.currentEnv.get('user_id')
        #Se l'utente ha i giusti requisiti le sue domande e le sue risposte non nascono com ebozza
        if 'admin' in self.db.currentEnv['userTags']: #posso pensare ad una condizione migliore e più sofisticata
            return dict( __is_draft = False,
                         approval_ts = datetime.now(),
                         approved_by_user_id = user_id,
                         user_id=user_id)

        return dict(__is_draft=True, user_id = user_id)

    def trigger_onUpdating(self, record, old_record):
        #Quando un record passa da bozza ad approvato metto utente approvatore e timestamp di approvazione
        if old_record['__is_draft'] and not record['__is_draft']:
            record['approval_ts']  = datetime.now()
            record['approved_by_user_id'] = self.db.currentEnv.get('user_id')