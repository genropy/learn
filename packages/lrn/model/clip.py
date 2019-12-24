# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('clip',pkey='id',name_long='!![en]Clip',name_plural='!![en]Clips',caption_field='title')
        self.sysFields(tbl)
        tbl.column('title', name_long='!![en]Title')
        tbl.column('video_id', name_long='!![en]Video').relation('video.id', 
                                relation_name='clips', 
                                mode='foreignkey', 
                                onDelete='raise')
        tbl.column('topic_id', name_long='!![en]Topic').relation('topic.id', 
                                relation_name='clips', 
                                mode='foreignkey', 
                                onDelete='raise')
        tbl.column('time_code', name_long='!![en]Timecode')
        tbl.column('keywords', name_ling='!![en]Keywords')
        tbl.column('url', name_long='!![en]Url')