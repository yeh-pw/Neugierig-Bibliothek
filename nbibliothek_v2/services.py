from nbibliothek_v1.services import NbibliothekService, LangManager

class NbibliothekService_v2(NbibliothekService):

    def lang_manager(self):
        return LangManager(self._lang)