import os
import json
from nbibliothek_v1.db import NbibliothekDB
from nbibliothek_v1.ui import NbibliothekUI
from datetime import *


class Search_Book_Observer:
    def __init__(self, title, times=1):
        self._title = title
        self._times = times

    @property
    def title(self):
        return self._title

    @property
    def times(self):
        return self._times

    def add_times(self):
        self._times += 1


class Return_Observer:

    def __init__(self, title, borrowed, quantity):
        self._title = title
        self._borrowed = borrowed
        self._quantity = quantity

    @property
    def title(self):
        return self._title

    @property
    def borrowed(self):
        return self._borrowed

    @property
    def quantity(self):
        return self._quantity


class AbstractServices:

    def __init__(self, db_url, lang):
        self._db_url = db_url
        self._lang = lang
        self._ui = None
        self._searchobservers = set()
        self._returnobservers = set()

    def register_search_observer(self, title):
        pass

    def notify_search(self, title):
        pass

    def lang_manager(self):
        pass

    def unregister_search_observer(self, title):
        pass

    def get_book_by_title(self, title):
        pass

    def get_member_by_nim(self, nim):
        pass

    def get_current_borrows_by_nim(self, nim):
        pass

    def if_max_quota_borrows(self, nim):
        pass

    def pinjam_buku_by_title(self, nim, title):
        pass

    def kembalikan_buku_by_title(self, nim, title):
        pass

    def get_fav_books_for_chart(self):
        pass

    def get_fav_books(self):
        pass

    def change_lang(self, bahasa):
        pass

    def run_ui(self):
        pass

    def init_db(self):
        pass


class LangManager:
    def __init__(self, lang):
        self._lang_path = os.getcwd()+fr'\nbibliothek_v1\configs\{lang}.json'
        with open(self._lang_path) as config_file:
            self._data = json.load(config_file)

    def get_words(self, key):
        return self._data[key]


class NbibliothekService(AbstractServices):

    def __init__(self, db_url, lang="id"):
        self._db = NbibliothekDB(db_url)
        self._lang = lang
        self._ui = None  # Declared when run
        self._searchobservers = set()
        self._returnobservers = set()

    def lang_manager(self):
        return LangManager("id")

    def register_return_observer(self, title, borrowed, quantity):
        self._returnobservers.add(
            Return_Observer(title, borrowed, quantity))

    def notify_return_observer(self, title):
        for observer in self._returnobservers:
            if observer.title == title:
                bb = self.lang_manager().get_words("bukuberjudul")
                sdp = self.lang_manager().get_words("sudahdapatdipinjam")
                print(
                    f"[EMAIL] {bb} '{observer.title}' {sdp} ({observer.borrowed}/{observer.quantity})")
        self._returnobservers.clear()

    def register_search_observer(self, title):
        for observer in self._searchobservers:
            if observer.title == title:
                return True

        self._searchobservers.add(Search_Book_Observer(title))

    def notify_search(self, title):

        for observer in self._searchobservers:
            if observer.title == title:
                observer.add_times()
                if observer.times > 6:
                    print(
                        f"""[EMAIL] {self.lang_manager().get_words("pesan_obs1")} {title} {self.lang_manager().get_words("pesan_obs2")} 5x""")

    def unregister_search_observer(self, title):
        # Mencabut observer apabila buku telah ditambahkan, karena belum ada fitur tambah buku maka fungsi ini sementara tidak melakukan apapun
        pass

    def unregister_return_observer(self, title):
        # Mencabut observer apabila buku telah ditambahkan, karena belum ada fitur tambah buku maka fungsi ini sementara tidak melakukan apapun
        pass

    def get_book_by_isbn(self, isbn):
        book = self._db.get_book_by_isbn(isbn)
        return book

    def get_member_by_nim(self, nim):
        member = self._db.get_members_by_nim(nim)
        return member

    def get_current_borrows_by_nim(self, nim):
        current_borrows = self._db.get_current_borrows_by_nim(nim)
        return current_borrows

    def if_already_borrows_x_books(self, nim, isbn):
        current_borrows = self.get_current_borrows_by_nim(nim)

        for x in current_borrows:
            if x.isbn == isbn:
                return True
        return False

    def if_max_quota_borrows(self, nim):
        current_borrows = self.get_current_borrows_by_nim(nim)
        if len(current_borrows) == 3:
            return True
        else:
            return False

    def pinjam_buku_by_isbn(self, nim, isbn):
        self._db.begin_transaction()
        self._db.pinjam_buku_by_isbn(nim, isbn)
        self._db.commit()

    def kembalikan_buku_by_isbn(self, nim, isbn):
        self._db.begin_transaction()
        self._db.kembalikan_buku_by_isbn(nim, isbn)
        self._db.commit()

    def get_fav_books_for_chart(self):
        fav_books = self._db.get_fav_books_for_chart()
        return fav_books

    def get_fav_books_for_dummy(self):
        lang = self.lang_manager()
        print(
            f"5 {lang.get_words('dummy')} {datetime.today().strftime('%m-%Y')}")
        print("")
        a = self._db.get_fav_books_for_dummy()
        for x in a:
            print(
                f"{lang.get_words('judul')}{' '*(10-len(lang.get_words('judul')))}: {x.title}")
            print(
                f"{lang.get_words('pengarang')}{' '*(10-len(lang.get_words('pengarang')))}: {x.author}")
            print(
                f"{lang.get_words('isbn')}{' '*(10-len(lang.get_words('isbn')))}: {x.isbn}")
            print("")

    def get_suggest_member(self, key):
        suggests = self._db.get_suggestion_members(key)
        return suggests

    def get_suggest_book(self, key):
        suggests = self._db.get_suggestion_book(key)
        return suggests

    def change_lang(self, bahasa):
        self._lang = bahasa

    def run_ui(self):
        self._ui = NbibliothekUI(self)
        self._ui.mainloop()

    def init_db(self):
        self._db.init()

    def init_borrows_db_dummy(self):
        self._db.init_borrows_dummy()
