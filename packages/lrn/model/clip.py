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
        tbl.aliasColumn('other_topics','@clip_alias.@topic_id.description',name_long='!![en]Other topics')
        tbl.formulaColumn('timecode_parameter', """REPLACE(@video_id.@streaming_service.url_timecode_template, '#time_code', $time_code)""")
        tbl.formulaColumn('clip_url', """$video_url||'&'||$timecode_parameter""", name_long='URL')
        tbl.pyColumn('embedded_url', group='_',py_method='formatUrl')

    def formatUrl(self, record, field):
        z = (['0','0','0']+record['time_code'
                ].replace('s','').replace('m',':').replace('h',':').split(':'))[-3:]
        sec = int(z[0])*3600+int(z[1])*60+int(z[2])
        return'{video_embedded_url}?start={sec}'.format(video_embedded_url=record['video_embedded_url'],sec=sec)
