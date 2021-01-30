from tests.mock_service_v3 import MockService_v3

import re

mem_db = ":memory:"

# Testing 3 languages as examples

# TEST GERMANY
# 5X SEARCH
def test_send_email_success_2thcall_de():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("de")
    no_judul = "Test Judul"
    mock_service.register_search_observer(no_judul)
    call1 = mock_service.notify_search(no_judul)
    call2 = mock_service.notify_search(no_judul)
    call3 = mock_service.notify_search(no_judul)
    call4 = mock_service.notify_search(no_judul)
    call5 = mock_service.notify_search(no_judul)
    call6 = mock_service.notify_search(no_judul)
    assert call2 != """[EMAIL] Bibliothekar, Buch mit dem Titel Test Judul wurde von Menschen mehr als gesucht 5x"""


def test_send_email_success_5thcall_de():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("de")
    no_judul = "Test Judul"
    mock_service.register_search_observer(no_judul)
    call1 = mock_service.notify_search(no_judul)
    call2 = mock_service.notify_search(no_judul)
    call3 = mock_service.notify_search(no_judul)
    call4 = mock_service.notify_search(no_judul)
    call5 = mock_service.notify_search(no_judul)
    call6 = mock_service.notify_search(no_judul)
    assert call5 != """[EMAIL] Bibliothekar, Buch mit dem Titel Test Judul wurde von Menschen mehr als gesucht 5x"""


def test_send_email_success_6thcall_de():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("de")
    judul = "Test Judul"
    mock_service.register_search_observer(judul)
    call1 = mock_service.notify_search(judul)
    call2 = mock_service.notify_search(judul)
    call3 = mock_service.notify_search(judul)
    call4 = mock_service.notify_search(judul)
    call5 = mock_service.notify_search(judul)
    call6 = mock_service.notify_search(judul)
    assert call6 == """[EMAIL] Bibliothekar, Buch mit dem Titel Test Judul wurde von Menschen mehr als gesucht 5x"""


def test_send_email_success_7thcall_de():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("de")
    no_judul = "Test Judul"
    mock_service.register_search_observer(no_judul)
    call1 = mock_service.notify_search(no_judul)
    call2 = mock_service.notify_search(no_judul)
    call3 = mock_service.notify_search(no_judul)
    call4 = mock_service.notify_search(no_judul)
    call5 = mock_service.notify_search(no_judul)
    call6 = mock_service.notify_search(no_judul)
    call7 = mock_service.notify_search(no_judul)
    assert call7 == """[EMAIL] Bibliothekar, Buch mit dem Titel Test Judul wurde von Menschen mehr als gesucht 5x"""

    # RETURN BOOK GERMANY
def test_send_email_return_book_de():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("de")
    nim_peminjam1 = "1234567890"
    dipinjam_entry = "Masyarakat Kota (1234567890006)"
    re_dipinjam_entry = re.search(r"\(([A-Za-z0-9_]+)\)", dipinjam_entry)
    isbn_dipinjam = re_dipinjam_entry[1]
    mock_service.pinjam_buku_by_isbn(nim_peminjam1, isbn_dipinjam)
    mock_service.kembalikan_buku_by_isbn(
        nim_peminjam1, isbn_dipinjam)
    book = mock_service.get_book_by_isbn(isbn_dipinjam)
    jumlah_dipinjam = book.quantity - book.availability
    mock_service.register_return_observer(
        dipinjam_entry, jumlah_dipinjam, book.quantity)
    call = mock_service.notify_return_observer(dipinjam_entry)
    assert call == """[EMAIL] Buch mit dem Titel 'Masyarakat Kota (1234567890006)' kann bereits ausgeliehen werden (0/5)"""


def test_send_email_return_book2_de():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("de")
    nim_peminjam1 = "1234567890"
    nim_peminjam2 = "1234567891"
    nim_peminjam3 = "1234567892"
    dipinjam_entry = "Masyarakat Kota (1234567890006)"
    re_dipinjam_entry = re.search(r"\(([A-Za-z0-9_]+)\)", dipinjam_entry)
    isbn_dipinjam = re_dipinjam_entry[1]
    mock_service.pinjam_buku_by_isbn(nim_peminjam1, isbn_dipinjam)
    mock_service.pinjam_buku_by_isbn(nim_peminjam2, isbn_dipinjam)
    mock_service.pinjam_buku_by_isbn(nim_peminjam3, isbn_dipinjam)
    mock_service.kembalikan_buku_by_isbn(
        nim_peminjam1, isbn_dipinjam)
    book = mock_service.get_book_by_isbn(isbn_dipinjam)
    jumlah_dipinjam = book.quantity - book.availability
    mock_service.register_return_observer(
        dipinjam_entry, jumlah_dipinjam, book.quantity)
    call = mock_service.notify_return_observer(dipinjam_entry)
    assert call == """[EMAIL] Buch mit dem Titel 'Masyarakat Kota (1234567890006)' kann bereits ausgeliehen werden (2/5)"""

# Test Arabic

def test_send_email_success_2thcall_ar():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("ar")
    no_judul = "Test Judul"
    mock_service.register_search_observer(no_judul)
    call1 = mock_service.notify_search(no_judul)
    call2 = mock_service.notify_search(no_judul)
    call3 = mock_service.notify_search(no_judul)
    call4 = mock_service.notify_search(no_judul)
    call5 = mock_service.notify_search(no_judul)
    call6 = mock_service.notify_search(no_judul)
    assert call2 != """[EMAIL] امين المكتبة كتاب بعنوان Test Judul تم البحث عنها بواسطة أشخاص أكثر من 5x"""



def test_send_email_success_5thcall_ar():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("ar")
    no_judul = "Test Judul"
    mock_service.register_search_observer(no_judul)
    call1 = mock_service.notify_search(no_judul)
    call2 = mock_service.notify_search(no_judul)
    call3 = mock_service.notify_search(no_judul)
    call4 = mock_service.notify_search(no_judul)
    call5 = mock_service.notify_search(no_judul)
    call6 = mock_service.notify_search(no_judul)
    assert call5 != """[EMAIL] امين المكتبة كتاب بعنوان Test Judul تم البحث عنها بواسطة أشخاص أكثر من 5x"""



def test_send_email_success_6thcall_ar():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("ar")
    judul = "Test Judul"
    mock_service.register_search_observer(judul)
    call1 = mock_service.notify_search(judul)
    call2 = mock_service.notify_search(judul)
    call3 = mock_service.notify_search(judul)
    call4 = mock_service.notify_search(judul)
    call5 = mock_service.notify_search(judul)
    call6 = mock_service.notify_search(judul)
    assert call6 == """[EMAIL] امين المكتبة كتاب بعنوان Test Judul تم البحث عنها بواسطة أشخاص أكثر من 5x"""


def test_send_email_success_7thcall_ar():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("ar")
    no_judul = "Test Judul"
    mock_service.register_search_observer(no_judul)
    call1 = mock_service.notify_search(no_judul)
    call2 = mock_service.notify_search(no_judul)
    call3 = mock_service.notify_search(no_judul)
    call4 = mock_service.notify_search(no_judul)
    call5 = mock_service.notify_search(no_judul)
    call6 = mock_service.notify_search(no_judul)
    call7 = mock_service.notify_search(no_judul)
    assert call7 == """[EMAIL] امين المكتبة كتاب بعنوان Test Judul تم البحث عنها بواسطة أشخاص أكثر من 5x"""




    # RETURN BOOK ARABIC
def test_send_email_return_book_ar():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("ar")
    nim_peminjam1 = "1234567890"
    dipinjam_entry = "Masyarakat Kota (1234567890006)"
    re_dipinjam_entry = re.search(r"\(([A-Za-z0-9_]+)\)", dipinjam_entry)
    isbn_dipinjam = re_dipinjam_entry[1]
    mock_service.pinjam_buku_by_isbn(nim_peminjam1, isbn_dipinjam)
    mock_service.kembalikan_buku_by_isbn(
        nim_peminjam1, isbn_dipinjam)
    book = mock_service.get_book_by_isbn(isbn_dipinjam)
    jumlah_dipinjam = book.quantity - book.availability
    mock_service.register_return_observer(
        dipinjam_entry, jumlah_dipinjam, book.quantity)
    call = mock_service.notify_return_observer(dipinjam_entry)
    assert call == """[EMAIL] كتاب بعنوان 'Masyarakat Kota (1234567890006)' يمكن بالفعل استعارتها (0/5)"""

def test_send_email_return_book2():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("ar")
    nim_peminjam1 = "1234567890"
    nim_peminjam2 = "1234567891"
    nim_peminjam3 = "1234567892"
    dipinjam_entry = "Masyarakat Kota (1234567890006)"
    re_dipinjam_entry = re.search(r"\(([A-Za-z0-9_]+)\)", dipinjam_entry)
    isbn_dipinjam = re_dipinjam_entry[1]
    mock_service.pinjam_buku_by_isbn(nim_peminjam1, isbn_dipinjam)
    mock_service.pinjam_buku_by_isbn(nim_peminjam2, isbn_dipinjam)
    mock_service.pinjam_buku_by_isbn(nim_peminjam3, isbn_dipinjam)
    mock_service.kembalikan_buku_by_isbn(
        nim_peminjam1, isbn_dipinjam)
    book = mock_service.get_book_by_isbn(isbn_dipinjam)
    jumlah_dipinjam = book.quantity - book.availability
    mock_service.register_return_observer(
        dipinjam_entry, jumlah_dipinjam, book.quantity)
    call = mock_service.notify_return_observer(dipinjam_entry)
    assert call == """[EMAIL] كتاب بعنوان 'Masyarakat Kota (1234567890006)' يمكن بالفعل استعارتها (2/5)"""

# Test Chinnese Mainland
# 5X SEARCH
def test_send_email_success_2thcall_zh_cn():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("zh-cn")
    no_judul = "Test Judul"
    mock_service.register_search_observer(no_judul)
    call1 = mock_service.notify_search(no_judul)
    call2 = mock_service.notify_search(no_judul)
    call3 = mock_service.notify_search(no_judul)
    call4 = mock_service.notify_search(no_judul)
    call5 = mock_service.notify_search(no_judul)
    call6 = mock_service.notify_search(no_judul)
    assert call2 != """[EMAIL] 图书管理员，书名为 Test Judul 被人们搜索的次数超过 5x"""


def test_send_email_success_5thcall_zh_cn():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("zh-cn")
    no_judul = "Test Judul"
    mock_service.register_search_observer(no_judul)
    call1 = mock_service.notify_search(no_judul)
    call2 = mock_service.notify_search(no_judul)
    call3 = mock_service.notify_search(no_judul)
    call4 = mock_service.notify_search(no_judul)
    call5 = mock_service.notify_search(no_judul)
    call6 = mock_service.notify_search(no_judul)
    assert call5 != """[EMAIL] 图书管理员，书名为 Test Judul 被人们搜索的次数超过 5x"""


def test_send_email_success_6thcall_zh_cn():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("zh-cn")
    judul = "Test Judul"
    mock_service.register_search_observer(judul)
    call1 = mock_service.notify_search(judul)
    call2 = mock_service.notify_search(judul)
    call3 = mock_service.notify_search(judul)
    call4 = mock_service.notify_search(judul)
    call5 = mock_service.notify_search(judul)
    call6 = mock_service.notify_search(judul)
    assert call6 == """[EMAIL] 图书管理员，书名为 Test Judul 被人们搜索的次数超过 5x"""


def test_send_email_success_7thcall_zh_cn():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("zh-cn")
    no_judul = "Test Judul"
    mock_service.register_search_observer(no_judul)
    call1 = mock_service.notify_search(no_judul)
    call2 = mock_service.notify_search(no_judul)
    call3 = mock_service.notify_search(no_judul)
    call4 = mock_service.notify_search(no_judul)
    call5 = mock_service.notify_search(no_judul)
    call6 = mock_service.notify_search(no_judul)
    call7 = mock_service.notify_search(no_judul)
    assert call7 == """[EMAIL] 图书管理员，书名为 Test Judul 被人们搜索的次数超过 5x"""

  # RETURN BOOK
def test_send_email_return_book_zh_cn():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("zh-cn")
    nim_peminjam1 = "1234567890"
    dipinjam_entry = "Masyarakat Kota (1234567890006)"
    re_dipinjam_entry = re.search(r"\(([A-Za-z0-9_]+)\)", dipinjam_entry)
    isbn_dipinjam = re_dipinjam_entry[1]
    mock_service.pinjam_buku_by_isbn(nim_peminjam1, isbn_dipinjam)
    mock_service.kembalikan_buku_by_isbn(
        nim_peminjam1, isbn_dipinjam)
    book = mock_service.get_book_by_isbn(isbn_dipinjam)
    jumlah_dipinjam = book.quantity - book.availability
    mock_service.register_return_observer(
        dipinjam_entry, jumlah_dipinjam, book.quantity)
    call = mock_service.notify_return_observer(dipinjam_entry)
    assert call == """[EMAIL] 书名 'Masyarakat Kota (1234567890006)' 可以借了 (0/5)"""


def test_send_email_return_book2_zh_cn():
    mock_service = MockService_v3(mem_db)
    mock_service.init_db()
    mock_service.change_lang("zh-cn")
    nim_peminjam1 = "1234567890"
    nim_peminjam2 = "1234567891"
    nim_peminjam3 = "1234567892"
    dipinjam_entry = "Masyarakat Kota (1234567890006)"
    re_dipinjam_entry = re.search(r"\(([A-Za-z0-9_]+)\)", dipinjam_entry)
    isbn_dipinjam = re_dipinjam_entry[1]
    mock_service.pinjam_buku_by_isbn(nim_peminjam1, isbn_dipinjam)
    mock_service.pinjam_buku_by_isbn(nim_peminjam2, isbn_dipinjam)
    mock_service.pinjam_buku_by_isbn(nim_peminjam3, isbn_dipinjam)
    mock_service.kembalikan_buku_by_isbn(
        nim_peminjam1, isbn_dipinjam)
    book = mock_service.get_book_by_isbn(isbn_dipinjam)
    jumlah_dipinjam = book.quantity - book.availability
    mock_service.register_return_observer(
        dipinjam_entry, jumlah_dipinjam, book.quantity)
    call = mock_service.notify_return_observer(dipinjam_entry)
    assert call == """[EMAIL] 书名 'Masyarakat Kota (1234567890006)' 可以借了 (2/5)"""


