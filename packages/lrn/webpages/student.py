# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'

    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='main')
        student_id,nickname = self.db.table('lrn.student'
                                    ).readColumns(columns='$id,$nickname',
                                                  where='$user_id=:uid',
                                                 uid=self.avatar.user_id)
        bc.data('.current_student_id',student_id)
        bc.data('.current_student_nickname',nickname)
        self.mainToolbar(bc.contentPane(region='top'))
        
        center = bc.tabContainer(region='center',margin='2px')
        self.faqPane(center.borderContainer(title='!![en]FAQ',datapath='.faq'))
        self.lessonsPane(center.contentPane(title='!![en]Lessons'))
        self.profilePane(center.contentPane(title='!![en]Profile'))

    
    def profilePane(self,pane):
        pane.thFormHandler(table='lrn.student',
                            datapath='.profile',
                            formResource = 'FormStudentPage',
                            startKey='=main.current_student_id')
        

    def faqPane(self,bc):
        bc.data('.topics',self.db.table('lrn.topic').getHierarchicalData())
        left = bc.contentPane(region='left',width='20%',padding='10px',
                                splitter=True,border_right='1px solid silver')
        left.tree(storepath='.topics',
                    labelAttribute='caption',
                    hideValues=True,
                    selected_pkey='.topic_id',
                    selected_hierarchical_pkey='.hierarchical_pkey',
                    selectedLabelClass='selectedTreeNode')
        center = bc.contentPane(region='center',margin_left='5px',
                            border_left='1px solid silver')
        center.dialogTableHandler(table='lrn.question',
            default_user_id=self.avatar.user_id,
            default_main_topic_id='=main.faq.topic_id',
            delrow=False,
            condition="""CASE WHEN :hpkey IS NULL THEN $main_topic_id IS NULL ELSE 
                        @main_topic_id.hierarchical_pkey LIKE :hpkey || '%%'
                        END
                        """,
            condition_hpkey='^main.faq.hierarchical_pkey')


    def lessonsPane(self,pane):
        pane.div('TO DO...')

    def mainToolbar(self,pane):
        bar = pane.slotToolbar('2,pageTitle,*,logoutButton,2')
        bar.pageTitle.div('^.current_student_nickname',font_weight='bold')
        bar.logoutButton.button('Logout',action='genro.logout();')