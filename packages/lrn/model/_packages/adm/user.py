# encoding: utf-8

class Table(object):

    def trigger_onUpdated(self,record,
                          old_record=None):
        if old_record['status'] == 'wait' \
            and record['status'] == 'conf':
            tblstudent = self.db.table('lrn.student')
            newstudent = tblstudent.newrecord(
                name = record['firstname'],
                surname = record['lastname'],
                email = record['email'],
                nickname = record['username'],
                user_id = record['id']
            )
            tblstudent.insert(newstudent)
