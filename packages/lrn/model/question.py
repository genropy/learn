# encoding: utf-8
from datetime import datetime

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('question', pkey='id', name_long='!![en]Question', name_plural='!![en]Questions',caption_field='question')
        self.sysFields(tbl, draftField=True)
        tbl.column('question',name_long='!![en]Question', validate_notnull=True)
        tbl.column('description', name_long='!![en]Description')
        tbl.column('details', name_long='!![en]Details')
        tbl.column('user_id',size='22', group='_', name_long='!![en]Inserted by'
                    ).relation('adm.user.id', relation_name='myquestions', 
                                mode='foreignkey', onDelete='raise')
        tbl.column('approval_ts', dtype='DH', name_long='!![en]Approval TS')
        tbl.column('approved_by_user_id', size='22', group='_', name_long='!![en]Approved by'
                    ).relation('adm.user.id', 
                                relation_name='approved_questions', 
                                mode='foreignkey', onDelete='raise')
        tbl.column('main_topic_id',size='22', group='_', name_long='!![en]Main topic'
                    ).relation('topic.id', 
                                relation_name='questions', 
                                mode='foreignkey', 
                                onDelete='setnull')
        tbl.column('main_answer_id',size='22', group='_', name_long='!![en]Main answer'
                    ).relation('answer.id', 
                                relation_name='questions', 
                                mode='foreignkey', 
                                onDelete='setnull')
        #tbl.formulaColumn('__protected_by_approval_ts',"""($approval_ts IS NOT NULL AND $approved_by_user_id!=:env_user_id)""",dtype='B')
    
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


        