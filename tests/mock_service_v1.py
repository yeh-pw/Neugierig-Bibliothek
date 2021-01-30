from nbibliothek_v1.services import NbibliothekService


class MockService(NbibliothekService):

    def notify_return_observer(self, title):
        for observer in self._returnobservers:
            if observer.title == title:
                bb = self.lang_manager().get_words("bukuberjudul")
                sdp = self.lang_manager().get_words("sudahdapatdipinjam")
                return(
                    f"[EMAIL] {bb} '{observer.title}' {sdp} ({observer.borrowed}/{observer.quantity})")
    "[EMAIL] "
    def notify_search(self, title):

        for observer in self._searchobservers:
            if observer.title == title:
                observer.add_times()
                if observer.times > 6:
                    return(
                        f"""[EMAIL] {self.lang_manager().get_words("pesan_obs1")} {title} {self.lang_manager().get_words("pesan_obs2")} 5x""")


