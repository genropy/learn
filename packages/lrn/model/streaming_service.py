# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('streaming_service', pkey='code', name_long='!![en]Code', name_plural='!![en]Streaming services', caption_field='code',lookup=True)
        tbl.column('code',size=':10',name_long='!![en]Code')
        tbl.column('host_url', name_long='Host url')
        tbl.column('url_video_template')
        tbl.column('url_timecode_template')