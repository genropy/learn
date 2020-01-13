# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('topic_alias',pkey='id',name_long='!![en]Topic alias',
                      name_plural='!![en]Topic alias')
        self.sysFields(tbl)
        tbl.column('topic_id',size='22', group='_', name_long='Topic'
                    ).relation('topic.id', relation_name='aliases', mode='foreignkey', onDelete='raise')
        tbl.column('question_id',size='22',group='_',name_long='!![en]Question').relation('question.id', 
                                        mode='foreignkey', onDelete='cascade',
                                        relation_name='questions_alias')

        tbl.column('video_id',size='22',group='_',name_long='!![en]Video').relation('video.id', 
                                        mode='foreignkey', onDelete='cascade',
                                        relation_name='video_alias')
        
        tbl.column('clip_id',size='22',group='_',name_long='!![en]Clip').relation('clip.id', 
                                        mode='foreignkey', onDelete='cascade',
                                        relation_name='clip_alias')