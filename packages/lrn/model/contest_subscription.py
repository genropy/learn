# encoding: utf-8
from datetime import datetime

class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('contest_subscription',pkey='id',name_long='!![en]Contest subscription',
                                name_plural='!![en]Contest subscriptions',caption_field='email')
        self.sysFields(tbl)
        tbl.column('date', dtype='D', name_long='Date', name_short='Date')
        tbl.column('email', name_long='!![en]email')
        tbl.column('fullname', name_long='!![en]Full name')
        tbl.column('video_link', name_long='Video link', name_short='Video')
        tbl.column('name', name_long='Project name', name_short='Name') 
        tbl.column('description', name_long='Project description', name_short='Description')

    def defaultValues(self):
        date = self.db.workdate or datetime.today()
        return dict(date = date)