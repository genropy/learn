# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('video', pkey='id', name_long='!![en]Video', name_plural='!![en]Videos',caption_field='title')
        self.sysFields(tbl)
        tbl.column('title',size=':60',name_long='!![en]Title')
        tbl.column('description', name_long='!![en]Description')
        tbl.column('streaming_service', name_long='!![en]Streaming service').relation('streaming_service.code',
                                                                                      relation_name='videos',
                                                                                      onDelete='raise')
        tbl.column('main_topic_id',size='22', group='_', name_long='!![en]Main topic'
                    ).relation('topic.id', 
                                relation_name='videos', 
                                mode='foreignkey', 
                                onDelete='raise')
        tbl.column('external_id', name_long='!![en]External id', variant_url=True)
        tbl.aliasColumn('host_url', '@streaming_service.host_url')
        tbl.formulaColumn('video_parameter', """REPLACE(@streaming_service.url_video_template, '#external_id', $external_id)""")
        tbl.formulaColumn('video_url', """$host_url||$video_parameter""", name_long='URL')
