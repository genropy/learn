# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('video', pkey='id', name_long='!![en]Video', name_plural='!![en]Videos',caption_field='title')
        self.sysFields(tbl)
        tbl.column('title',size=':60',name_long='!![en]Title')
        tbl.column('description', name_long='!![en]Description')
        tbl.column('streaming_service', name_long='!![en]Streaming service')
        tbl.column('main_topic_id',size='22', group='_', name_long='!![en]Main topic'
                    ).relation('topic.id', 
                                relation_name='videos', 
                                mode='foreignkey', 
                                onDelete='raise')
        tbl.column('url', name_long='!![en]Url')