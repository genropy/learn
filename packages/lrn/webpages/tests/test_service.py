from gnr.core.gnrdecorator import public_method 

class GnrCustomWebPage(object):
    py_requires="""gnrcomponents/testhandler:TestHandlerFull,
                gnrcomponents/framegrid:FrameGrid,
                services/ftp/pysftp/component:SftpClient"""
    
    def test_1_ftp(self,pane):
        fb = pane.formbuilder()
        fb.dbselect(value='^.service',dbtable='sys.service',condition='$service_type=:f',
                        condition_f='ftp',lbl='Ftp',hasDownArrow=True,
                        selected_service_name='.service_name')
        fb.button('Run',fire='.run')
        fb.dataRpc('.result',self.ftplist,_fired='^.run',service_name='=.service_name')
        fb.div('^.result')

    @public_method
    def ftplist(self,service_name=None):
        myftp = self.getService('ftp',service_name)
        with myftp() as openconnection:
            return '<br/>'.join(openconnection.listdir())

    def test_2_variable_ftp(self, pane):
        fb = pane.formbuilder()
        fb.dbselect(value='^.service',dbtable='sys.service',condition='$service_type=:f',
                        condition_f='ftp',lbl='Ftp',hasDownArrow=True,
                        selected_service_name='.service_name')
        pane.dataRpc('.root.ftp',self.test4getFtpres,service_name='^.service_name')
        pane.tree(storepath='.root',hideValues=True, selectedLabelClass='selectedTreeNode',
                      selected_abs_path='.abs_path',selected_file_ext='.file_ext',
                      checked_abs_path='.checked_abs_path',
                      labelAttribute='nodecaption', autoCollapse=True)

    @public_method
    def test4getFtpres(self,service_name=None):
        return self.getService(service_type='ftp',
                                service_name=service_name).sftpResolver()
        

    def test_3_ftpclient(self, pane):
        bc = pane.borderContainer(height='500px')
        bc.contentPane(region='center').sftpClientLayout('learn',datapath='main')


    def test_4_pdf(self, pane):
        print(x)

