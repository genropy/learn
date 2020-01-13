# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('clip',pkey='id',name_long='!![en]Clip',name_plural='!![en]Clips',caption_field='title')
        self.sysFields(tbl)
        tbl.column('title', name_long='!![en]Title')
        tbl.column('video_id', name_long='!![en]Video',batch_assign=True).relation('video.id', 
                                relation_name='clips', 
                                mode='foreignkey', 
                                onDelete='raise')
        tbl.column('topic_id', name_long='!![en]Topic',batch_assign=True).relation('topic.id', 
                                relation_name='clips', 
                                mode='foreignkey', 
                                onDelete='raise')
        tbl.column('time_code', name_long='!![en]Timecode')
        tbl.aliasColumn('video_url', '@video_id.video_url')
        tbl.aliasColumn('video_embedded_url','@video_id.video_embedded_url')
        tbl.formulaColumn('timecode_parameter', """REPLACE(@video_id.@streaming_service.url_timecode_template, '#time_code', $time_code)""")
        tbl.formulaColumn('clip_url', """$video_url||'&'||$timecode_parameter""", name_long='URL')
