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
        left = bc.contentPane(region='left',width='30%',splitter=True)
        left.tree(storepath='.topics.root',
                    labelAttribute='caption',
                    hideValues=True,
                    selected_hierarchical_pkey='.hierarchical_pkey',
                    selectedLabelClass='selectedTreeNode')
        center = bc.contentPane(region='center').plainTableHandler(table='lrn.question',
            condition="@main_topic_id.hierarchical_pkey LIKE :hpkey || '%%'",
            condition_hpkey='^main.faq.hierarchical_pkey',
        )


    def lessonsPane(self,pane):
        pass

    def mainToolbar(self,pane):
        bar = pane.slotToolbar('2,pageTitle,*,logoutButton,2')
        bar.pageTitle.div('^.current_student_nickname',font_weight='bold')
        bar.logoutButton.button('Logout',action='genro.logout();')