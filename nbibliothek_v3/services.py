from nbibliothek_v2.services import NbibliothekService_v2
from googletrans import *
import os
import json


class LangManager_v2:

    def __init__(self, lang):
        self._lang = lang
        self._lang_path = os.getcwd()+fr'\nbibliothek_v1\configs\id.json'
        with open(self._lang_path) as config_file:
            self._data = json.load(config_file)
        self._translator = Translator()

    def translate(self, word):
        translated = self._translator.translate(word, dest=self._lang)
        return translated.text

    def get_words(self, key):
        kata = self._data[key]
        return self.translate(kata)


class NbibliothekService_v3(NbibliothekService_v2):

    def lang_manager(self):
        return LangManager_v2(self._lang)
