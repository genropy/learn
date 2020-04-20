# -*- coding: utf-8 -*-

# includedview_bagstore.py
# Created by Francesco Porcari on 2011-03-23.
# Copyright (c) 2011 Softwell. All rights reserved.
from gnr.core.gnrbag import Bag
from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    py_requires="""gnrcomponents/testhandler:TestHandlerFull,
                gnrcomponents/framegrid:FrameGrid"""

    def test_0_quickgrid(self,pane):
        bc = pane.borderContainer(height='300px')
        bc.contentPane(region='top',height='50px').button('Load',fire='.load')
        bottom = bc.contentPane(region='bottom',height='300px')
        pane.dataRpc('feed',self.getMyData,_fired='^.load')
        grid = bc.contentPane(region='center'
                            ).quickGrid(value='^feed',
                                        selected_link='.selectedLink')
        grid.column('title',width='20em',name='Titolo')
        grid.column('pubDate',width='10em',name='Data')
        grid.column('link',width='10em',name='Link')
        bottom.iframe(src='^.selectedLink',height='100%',width='100%',border=0)



    def test_1_quickgridEdit(self,pane):
        bc = pane.borderContainer(height='300px',width='400px')
        grid = bc.contentPane(region='center').quickGrid(value='^lista_spesa')
        grid.tools('addrow,delrow,export')
        grid.column('articolo',width='20em',name='Articolo',edit=True)
        grid.column('quantita',width='5em',name='Qt',edit=True,dtype='L')


    def struct_spesa(self,struct):
        r = struct.view().rows()
        r.cell('articolo',width='20em',name='Articolo',edit=True)
        r.cell('quantita',width='5em',name='Qt',edit=True,totalize=True,dtype='L')

    def test_2_baggrid(self,pane):
        frame = pane.bagGrid(title='La mia lista',storepath='lista_spesa',
                            struct=self.struct_spesa,
                            datapath='.vistaspesa',
                            height='400px',width='400px',
                            border='1px solid silver',
                            addrow='auto',delrow='auto')
        
    def test_3_tree(self,pane):
        pane.tree(storepath='lista_spesa')

    def struct_feed(self,struct):
        r = struct.view().rows()
        r.cell('title',width='20em',name='Titolo')
        r.cell('pubDate',width='10em',name='Data')
        r.cell('link',width='10em',name='Link')

    def test_4_baggrid_feed(self,pane):
        frame = pane.bagGrid(title='Le mie notizie',storepath='feed',
                            struct=self.struct_feed,
                            datapath='.vistafeed',
                            height='400px',width='600px',
                            border='1px solid silver',
                            addrow=False,delrow=False)
        bar = frame.top.bar.replaceSlots('#','#,*,loadfeed,2')
        bar.loadfeed.button('Load',fire='.load')
        bar.dataRpc('feed',self.getMyData,_fired='^.load')
        rightbar = frame.right.slotBar('2,treebox,2',width='200px')
        box = rightbar.treebox.div(height='100%')
        box.tree(storepath='feed')

    @public_method
    def getMyData(self):
        feed = Bag('https://www.ansa.it/sito/ansait_rss.xml')
        result = Bag()
        for i,n in enumerate(feed['rss.channel']):
            if n.label=='item':
                result.addItem(f'r_{i}',n.value)
        return result
        
    def test_5_tree_feed(self,pane):
        pane.tree(storepath='feed')