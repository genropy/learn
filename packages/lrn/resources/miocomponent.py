from gnr.web.gnrbaseclasses import BaseComponent
from gnr.web.gnrwebstruct import struct_method
from gnr.core.gnrdecorator import public_method

class GestoreAnagrafiche(BaseComponent):
    @struct_method
    def ga_anagraficaRidotta(self,pane,datapath=None):
        box = pane.div(padding='10px',margin='10px',
                    border='2px solid silver',rounded=10,
                    datapath=datapath)
        fb = box.formbuilder()
        fb.textbox(value='^.nome',lbl='Nome')
        fb.textbox(value='^.cognome',lbl='Cognome')
        fb.textbox(value='^.indirizzo',lbl='Indirizzo')
        fb.dbCombobox(value='^.citta',lbl='Città',
                        dbtable='glbl.localita')
        fb.dateTextbox(value='^.data_nascita',lbl='Data di nascita')
        return fb

    def _anagraficaTelefoni(self,fb):
        fb.textbox(value='^.telefono',lbl='Telefono')
        fb.textbox(value='^.cellulare',lbl='Cellulare')

    @struct_method
    def ga_anagraficaCompleta(self,pane,persona=None):
        pane.div(persona)
        box = pane.div(datapath=persona)
        fb = box.anagraficaRidotta(datapath='.dati_anagrafici')
        self._anagraficaTelefoni(fb)
        box.button('Salva',fire='.salva')
        box.dataRpc(None,self.salvaAnagraficaCompleta,
                    _fired='^.salva',persona=persona,
                    dati_anagrafici='=.dati_anagrafici',
                    _onResult='alert("Salvataggio "+result)')
        return fb
    
    @public_method
    def salvaAnagraficaCompleta(self,dati_anagrafici=None,
                                persona=None,**kwargs):
        sn = self.site.storageNode('site:personcine',f'{persona}.xml')
        with sn.local_path() as lp:
            dati_anagrafici.toXml(lp)
        return 'Ok'