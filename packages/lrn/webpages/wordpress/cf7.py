# -*- coding: utf-8 -*-
            
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag
from gnr.utils.awsmanager import AWSManager 
import datetime
import re

class GnrCustomWebPage(object):
    py_requires='gnrcomponents/externalcall:BaseRpc'

    @public_method
    def newSubscriptionFromCF7(self, cf7_token=None, email=None, fullname=None, name=None, description=None, video_link=None, 
                                    html=True, **kwargs):
        is_valid = self.checkToken(cf7_token=cf7_token)
        if not is_valid:
            return
        sub_tbl = self.db.table('lrn.contest_subscription')
        new_subscription = sub_tbl.newrecord(email=email, fullname=fullname, name=name, description=description, video_link=video_link)
        sub_tbl.insert(new_subscription)
        self.db.commit()
    
    @public_method
    def checkToken(self, cf7_token=None):
        wp_service = self.site.getService(service_type='wordpress', service_name='wordpress')
        if wp_service.wp_cf7_token == cf7_token:
            print('Token is valid')
            return True
        else:
            print('Token is NOT valid')
            return False