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
        self.videosPane(center.borderContainer(title='!![en]Videos', datapath='.videos'))
        self.videosPane2(center.framePane(title='!![en]Videos versione alternativa', datapath='.videos2'))
    
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
                                nodeId='myQuestions',
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
            nodeId='pubQuestions',
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


    def videosPane(self,bc):
        left = bc.borderContainer(region='left', width='40%')
        left.contentPane(region='top', height='40%'
                    ).plainTableHandler(nodeId='video_th', table='lrn.video',
                                        viewResource='ViewMini',
                                        #view_grid_autoSelect=True,
                                        condition__onStart=True)

        left.contentPane(region='center').plainTableHandler(table='lrn.clip',
                                                          nodeId='clip_th',
                                                          view_grid_autoSelect=True,
                                                          condition_video_id='^#video_th.view.grid.selectedId',
                                                          condition='$video_id=:video_id',
                                                          viewResource='ViewFromVideoMini',
                                                          grid_selected_embedded_url='main.videos.curr_embedded_url')
        bc.contentPane(region='center').iframe(height='100%',width='100%',border='0',
                                            #src='^#clip_th.view.grid.selectedId?embedded_url')
                                            src ='^.curr_embedded_url')

    def videosPane2(self, frame):
        bar = frame.top.slotToolbar('10,selettore_video,*', height='20px', datapath='.current', nodeId='params')
        fb = bar.selettore_video.formbuilder(cols=2)
        fb.dbSelect('^.video_id', lbl='Video', 
                                  dbtable='lrn.video', columns='$title,$description',
                                  auxColumns='$title,$streaming_service',
                                  selected_description='.description',
                                  hasDownArrow=True)
        fb.div('^.description', style='font-weight:bold;')
        bc = frame.center.borderContainer(region='center')

        left = bc.contentPane(region='left', width='40%').plainTableHandler(table='lrn.clip',
                                                          view_grid_autoSelect=True,
                                                          condition_video_id='^#params.video_id',
                                                          condition='CASE WHEN :video_id IS NULL THEN TRUE ELSE $video_id=:video_id END',
                                                          condition__onStart=True,
                                                          viewResource='ViewMini',
                                                          grid_selected_embedded_url='#params.embedded_url')
        
        bc.contentPane(region='center').iframe(height='100%',width='100%',border='0',
                                               src ='^.current.embedded_url')



    def mainToolbar(self,pane):
        bar = pane.slotToolbar('2,pageTitle,*,logoutButton,2')
        bar.pageTitle.div('^.current_student_nickname',font_weight='bold')
        bar.logoutButton.button('Logout',action='genro.logout();')