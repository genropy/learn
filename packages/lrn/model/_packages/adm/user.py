# encoding: utf-8

class Table(object):

    def trigger_onUpdating(self,record,old_record=None):
        if old_record['status'] != 'conf' and record['status'] == 'conf':
            group_code = self.db.table('adm.group').sysRecord('STUDENT')['code']
            record['group_code'] = group_code
            self.db.table('lrn.student').createStudent(record)
