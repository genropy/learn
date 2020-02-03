# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'

    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='main')
        student_id,nickname = self.db.table('lrn.student'
                                    ).readColumns(columns='$id,$nickname',
                                                  where='$user_id=:uid',
                                                 uid=self.avatar.user_id)
        bc.data('.current_student_id', student_id)
        bc.data('.current_student_nickname', nickname)

        self.mainToolbar(bc.contentPane(region='top'))
        center = bc.tabContainer(region='center',margin='2px')
        self.profilePane(center.contentPane(title='!![en]Profile'))
        self.questionsPane(center.borderContainer(title='!![en]Published questions',datapath='.questions'))
        self.askQuestion(center.contentPane(title='!![en]Ask question'))
        self.myQuestionsPane(center.contentPane(title='!![en]My Questions',
                                                datapath='.my_questions'))
        #self.myAnswersPane(center.borderContainer(title='!![en]My Answers',datapath='.my_answers'))
        self.videosPane(center.contentPane(title='!![en]Videos'))
    
    def profilePane(self,pane):
        pane.thFormHandler(table='lrn.student',
                            datapath='.profile',
                            formResource = 'FormStudentPage',
                            startKey='=main.current_student_id')

    def askQuestion(self, pane):
        pane.thFormHandler(table='lrn.question',
                            datapath='.new_question',
                            formResource = 'FormNewQuestion',
                            startKey='*newrecord*')

    def myQuestionsPane(sel, pane):
        pane.dialogTableHandler(table='lrn.question',
                               condition='$user_id = :env_user_id',
                               condition__onStart=True,
                               formResource='FormMyQuestion',
                               viewResource='ViewStatus',
                               addrow=False)

    def questionsPane(self,bc):
        bc.data('.topics',self.db.table('lrn.topic').getHierarchicalData())
        left = bc.contentPane(region='left',width='20%',padding='10px', splitter=True,border_right='1px solid silver')
        left.tree(storepath='.topics',
                    labelAttribute='caption',
                    hideValues=True,
                    selected_pkey='.topic_id',
                    selected_hierarchical_pkey='.hierarchical_pkey',
                    selectedLabelClass='selectedTreeNode')
        center = bc.contentPane(region='center',margin_left='5px',
                            border_left='1px solid silver')
        center.dialogTableHandler(table='lrn.question',
            default_main_topic_id='=main.questions.topic_id',
            delrow=False,
            addrow=False,
            condition__onStart=True,
            condition="""CASE WHEN :hpkey IS NULL THEN TRUE ELSE 
                        @main_topic_id.hierarchical_pkey LIKE :hpkey || '%%'
                        END
                        AND $approval_ts IS NOT NULL
                        """,
            condition_hpkey='^main.questions.hierarchical_pkey',
            formResource='FormStudente')


    def videosPane(self,pane):
        pane.dialogTableHandler(table='lrn.video', delrow=False, addrow=False, condition__onStart=True)

    def mainToolbar(self,pane):
        bar = pane.slotToolbar('2,pageTitle,*,logoutButton,2')
        bar.pageTitle.div('^.current_student_nickname',font_weight='bold')
        bar.logoutButton.button('Logout',action='genro.logout();')