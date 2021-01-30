from tests.mock_service_v1 import MockService
import re

mem_db = ":memory:"


# 5X SEARCH
def test_send_email_success_2thcall():
    mock_service = MockService(mem_db)
    mock_service.init_db()
    no_judul = "Test Judul"
    mock_service.register_search_observer(no_judul)
    call1 = mock_service.notify_search(no_judul)
    call2 = mock_service.notify_search(no_judul)
    call3 = mock_service.notify_search(no_judul)
    call4 = mock_service.notify_search(no_judul)
    call5 = mock_service.notify_search(no_judul)
    call6 = mock_service.notify_search(no_judul)
    assert call2 != """[EMAIL] Pustakawan, buku berjudul Test Judul sudah dicari oleh orang lebih dari 5x"""


def test_send_email_success_5thcall():
    mock_service = MockService(mem_db)
    mock_service.init_db()
    no_judul = "Test Judul"
    mock_service.register_search_observer(no_judul)
    call1 = mock_service.notify_search(no_judul)
    call2 = mock_service.notify_search(no_judul)
    call3 = mock_service.notify_search(no_judul)
    call4 = mock_service.notify_search(no_judul)
    call5 = mock_service.notify_search(no_judul)
    call6 = mock_service.notify_search(no_judul)
    assert call5 != """[EMAIL] Pustakawan, buku berjudul Test Judul sudah dicari oleh orang lebih dari 5x"""


def test_send_email_success_6thcall():
    mock_service = MockService(mem_db)
    mock_service.init_db()
    no_judul = "Test Judul"
    mock_service.register_search_observer(no_judul)
    call1 = mock_service.notify_search(no_judul)
    call2 = mock_service.notify_search(no_judul)
    call3 = mock_service.notify_search(no_judul)
    call4 = mock_service.notify_search(no_judul)
    call5 = mock_service.notify_search(no_judul)
    call6 = mock_service.notify_search(no_judul)
    assert call6 == """[EMAIL] Pustakawan, buku berjudul Test Judul sudah dicari oleh orang lebih dari 5x"""


def test_send_email_success_7thcall():
    mock_service = MockService(mem_db)
    mock_service.init_db()
    judul = "Test Judul"
    mock_service.register_search_observer(judul)
    call1 = mock_service.notify_search(judul)
    call2 = mock_service.notify_search(judul)
    call3 = mock_service.notify_search(judul)
    call4 = mock_service.notify_search(judul)
    call5 = mock_service.notify_search(judul)
    call6 = mock_service.notify_search(judul)
    call7 = mock_service.notify_search(judul)
    assert call7 == """[EMAIL] Pustakawan, buku berjudul Test Judul sudah dicari oleh orang lebih dari 5x"""


# # RETURN BOOK
def test_send_email_return_book():
    mock_service = MockService(mem_db)
    mock_service.init_db()
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
    assert call == """[EMAIL] Buku berjudul 'Masyarakat Kota (1234567890006)' sudah dapat dipinjam (0/5)"""


def test_send_email_return_book2():
    mock_service = MockService(mem_db)
    mock_service.init_db()
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
    assert call == """[EMAIL] Buku berjudul 'Masyarakat Kota (1234567890006)' sudah dapat dipinjam (2/5)"""
