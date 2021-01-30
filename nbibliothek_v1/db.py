from nbibliothek_v1.models import *
import sqlite3


class Abstract_DB:
    def __init__(self, db_url):
        self._db_url = db_url

    def begin_transaction(self):
        pass

    def commit(self):
        pass

    def _MemberstoDTO(self, rows):
        pass

    def _bookstoDTO(self, rows):
        pass

    def _booktoDTO(self, rows):
        pass

    def get_members_by_nim(self, nim):
        pass

    def get_book_by_isbn(self, isbn):
        pass

    def pinjam_buku_by_isbn(self, isbn):
        pass

    def kembalikan_buku_by_isbn(self, nim, isbn):
        pass

    def _DTOforChart(self, rows):
        pass

    def get_fav_books_for_chart(self):
        pass

    def _SuggestiontoDTO(self, row):
        pass

    def get_suggestions(self, word):
        pass

    def init(self):
        pass


class NbibliothekDB(Abstract_DB):
    def __init__(self, db_url):
        self._db_url = db_url
        self._conn = self._create_connection()

    def _create_connection(self):
        return sqlite3.connect(self._db_url)

    def begin_transaction(self):
        pass

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()

    def _MemberstoDTO(self, row):
        dto = None

        for prop in row:
            dto = MemberDTO(prop[0], prop[1])

        return dto

    def get_members_by_nim(self, nim):
        get_nim_query = """
        SELECT * 
          FROM members
         WHERE nim=?;"""

        cursor = self._conn.cursor()
        ex = cursor.execute(get_nim_query, (nim,))
        row = ex.fetchall()

        return self._MemberstoDTO(row)

    def _BooktoDTO(self, row):
        dto = None

        for prop in row:
            dto = BooksDTO(prop[0], prop[1], prop[2],
                           prop[3], prop[4], prop[5], prop[6])

        return dto

    def _BookstoDTO(self, rows):
        dtos = []

        for row in rows:
            dtos.append(BooksDTO(row[0], row[1], row[2],
                                 row[3], row[4], row[5], row[6]))

        return dtos

    def get_book_by_isbn(self, isbn):
        get_book_by_isbn_query = """
        SELECT *
          FROM books
         WHERE isbn=?;"""

        cursor = self._conn.cursor()
        ex = cursor.execute(get_book_by_isbn_query, (isbn,))
        row = ex.fetchall()

        return self._BooktoDTO(row)

    def kembalikan_buku_by_isbn(self, nim, isbn):
        kembalikan_query = """
        UPDATE borrows
           SET tgl_returned  = (date('now','localtime'))
         WHERE nim=? and isbn=?;
        """
        update_availability_query = """
        update books
           set availability = availability + 1
         WHERE isbn=?; """

        cursor = self._conn.cursor()
        cursor.execute(kembalikan_query, (nim, isbn,))
        cursor.execute(update_availability_query, (isbn,))

    def _BorrowstoDTO(self, rows):
        dtos = []

        for row in rows:
            dtos.append(BorrowsDTO(row[0], row[1],
                                   row[2], row[3], row[4], row[5]))

        return dtos

    def get_current_borrows_by_nim(self, nim):
        check_current_borrows = """
        SELECT nim, borrows.isbn, books.title, borrows.tgl_pinjam, borrows.tgl_return, borrows.tgl_returned
        FROM borrows
        INNER JOIN books on books.isbn = borrows.isbn
        WHERE tgl_returned is NULL AND
        nim=?;
        """
        cursor = self._conn.cursor()
        ex = cursor.execute(check_current_borrows, (nim,))
        rows = ex.fetchall()

        return self._BorrowstoDTO(rows)

    def pinjam_buku_by_isbn(self, nim, isbn):

        pinjam = """
        INSERT into borrows(nim,isbn)
        VALUES (?,?);
        """
        update_availability = """        
        UPDATE books
           SET availability = availability - 1
         WHERE isbn=? AND availability > 0;"""

        cursor = self._conn.cursor()
        cursor.execute(pinjam, (nim, isbn,))
        cursor.execute(update_availability, (isbn,))

    def _DTOforChart(self, rows):
        dtos = []

        for row in rows:
            dtos.append(ChartsDTO(row[0], row[1], row[2]))

        return dtos

    def get_fav_books_for_chart(self):
        get_fav_books_1_month_query = """
        SELECT borrows.isbn, books.title, count(*)
          FROM borrows
         INNER JOIN books on books.isbn = borrows.isbn
         WHERE strftime('%m', tgl_pinjam) = strftime('%m','now') 
         GROUP BY borrows.isbn
         ORDER BY count(*) DESC
         LIMIT 5; """
        cursor = self._conn.cursor()
        ex = cursor.execute(get_fav_books_1_month_query)
        row = ex.fetchall()

        return self._DTOforChart(row)

    def get_fav_books_for_dummy(self):
        query = """
        SELECT * 
          FROM books
         WHERE isbn in (
        SELECT isbn
          FROM borrows 
         WHERE strftime('%m', tgl_pinjam) = strftime('%m','now') 
         group by isbn
         order by count(*) DESC
         limit 5);
        """
        cursor = self._conn.cursor()
        ex = cursor.execute(query)
        row = ex.fetchall()

        return self._BookstoDTO(row)

    def _SuggestionBooktoDTO(self, rows):
        dtos = []

        for row in rows:
            dtos.append(SuggestionBookDTO(row[0], row[1]))

        return dtos

    def get_suggestion_book(self, word):
        suggestion_query = """
        SELECT title, isbn
          FROM books
         WHERE title like ?
            OR isbn like ?
            OR author like ?
         ORDER by title;
        """
        isi = f"%{word}%"
        cursor = self._conn.cursor()
        ex = cursor.execute(suggestion_query, (isi, isi, isi,))
        row = ex.fetchall()

        return self._SuggestionBooktoDTO(row)

    def _SuggestionMembertoDTO(self, rows):
        dtos = []

        for row in rows:
            dtos.append(SuggestionMemberDTO(row[0], row[1]))

        return dtos

    def get_suggestion_members(self, word):
        suggestion_query = """
        SELECT name, nim
          FROM members
         WHERE name like ?
            OR nim like ?
         ORDER by name;
        """
        isi = f"%{word}%"
        cursor = self._conn.cursor()
        ex = cursor.execute(suggestion_query, (isi, isi,))
        row = ex.fetchall()

        return self._SuggestionMembertoDTO(row)

    def init(self):
        drop_books_table = """
        DROP TABLE IF EXISTS books;
        """
        self._conn.cursor().execute(drop_books_table)

        drop_members_table = """
        DROP TABLE IF EXISTS members;
        """
        self._conn.cursor().execute(drop_members_table)

        drop_ongoing_borrows_table = """
        DROP TABLE IF EXISTS borrows;
        """

        self._conn.cursor().execute(drop_ongoing_borrows_table)

        foreign_keys_on = """
        PRAGMA foreign_keys = ON;"""

        self._conn.cursor().execute(foreign_keys_on)

        create_books_table = """CREATE table books(
    isbn int UNIQUE NOT NULL check(length(isbn) = 13),
    title varchar(255) NOT NULL,
    author varchar(255) NOT NULL,
    publisher varchar(255) NOT NULL,
    classification int NOT NULL check(length(classification) <= 3),
    availability int NOT NULL,
    quantity int NOT NULL
);"""

        self._conn.cursor().execute(create_books_table)

        create_members_table = """
        CREATE table members(
           nim INTEGER PRIMARY KEY UNIQUE NOT NULL check(length(nim) = 10),
          name varchar(255) NOT NULL
);"""

        self._conn.cursor().execute(create_members_table)

        create_borrows_table = f"""
        
CREATE table borrows(
   nim int NOT NULL,
  isbn int NOT NULL,
   tgl_pinjam date default (date('now','localtime')),
   tgl_return date default (date('now','localtime','+7 day')),
   tgl_returned date,
   FOREIGN KEY(nim) REFERENCES members(nim),
   FOREIGN KEY(isbn) REFERENCES books(isbn)    
);"""

        self._conn.cursor().execute(create_borrows_table)

        initiate_books = """
        INSERT into books VALUES(
            1234567890001,
            "Filsafat Cinta",
            "Doni Sulaeman",
            "Dunia Biru Publishing",
            100,
            5,
            5
        );
        
        INSERT into books VALUES(
            1234567890002,
            "Menjelajah Pikiran",
            "Sumanto Adiprakoso",
            "Membaca Surga Publishing",
            100,
            5,
            5
        );

        INSERT into books VALUES(
            1234567890003,
            "Mengenal Agama Kristen",
            "Agung Prakoso",
            "Jogja Publishing",
            200,
            5,
            5
        );

        INSERT into books VALUES(
            1234567890004,
            "Kebijakan Buddha",
            "Lie Xung Yuk",
            "Dharma Publishing",
            200,
            5,
            5
        );

        INSERT into books VALUES(
            1234567890005,
            "Struktur Sosial Moderen",
            "Sunggar Silaen",
            "Artikular Publishing",
            300,
            5,
            5
        );

        INSERT into books VALUES(
            1234567890006,
            "Masyarakat Kota",
            "Doni Kuto",
            "Kompas Gramedia",
            300,
            5,
            5
        );


        INSERT into books VALUES(
            1234567890007,
            "Kamus Bahasa Isyarat",
            "Koni Silaban",
            "Mojokerto Citra Terbit",
            400,
            5,
            5
        );

        INSERT into books VALUES(
            1234567890008,
            "Kamus Bahasa Jerman",
            "Joko Purbowi",
            "Artikular Publishing",
            400,
            5,
            5
        );

        INSERT into books VALUES(
            1234567890009,
            "Konsep Toksikologi",
            "Lita Suryano",
            "Universitas Indonesia Publishing",
            500,
            5,
            5
        );

        INSERT into books VALUES(
            1234567890010,
            "Biology Is Fun",
            "John Monrow",
            "Harvard University Press",
            500,
            5,
            5
        );

        INSERT into books VALUES(
            1234567890011,
            "Biology Is Fun",
            "John Monrow",
            "Yale University Press",
            500,
            5,
            5
        );

    INSERT into books VALUES(
                1234567890012,
                "Sejarah Indonesia",
                "Tono Sugandhi",
                "Kompas Penerbit",
                900,
                5,
                5
            );

    INSERT into books VALUES(
                1234567890013,
                "American History",
                "Mary McCain",
                "Young Publishing",
                900,
                5,
                5
            );

    INSERT into books VALUES(
                1234567890014,
                "Sejarah Indonesia",
                "Tono Sugandhi",
                "Kompas Penerbit",
                900,
                5,
                5
            );
    
    INSERT into books VALUES(
                1234567890015,
                "Sejarah Tanah Jawa",
                "Tono Sugandhi",
                "Kompas Penerbit",
                900,
                5,
                5
            );

    INSERT into books VALUES(
                1234567890016,
                "War History",
                "John Caucas",
                "Morning Star Publishing",
                900,
                5,
                5
            );

    INSERT into books VALUES(
                1234567890017,
                "Zaman Megalitikum",
                "Marni Sumarno",
                "Kompas Penerbit",
                900,
                5,
                5
            );

    INSERT into books VALUES(
                1234567890018,
                "Sejarah Kelam Indonesia",
                "Marni Sumarno",
                "Kompas Penerbit",
                900,
                5,
                5
            );
    
    INSERT into books VALUES(
                1234567890019,
                "Tanah Abang : Sejarah Para Jawara",
                "Marni Sumarno",
                "Kompas Penerbit",
                900,
                5,
                5
            );

    INSERT into books VALUES(
                1234567890020,
                "Pendudukan Jepang",
                "Marni Sumarno",
                "Kompas Penerbit",
                900,
                5,
                5
            );

    INSERT into books VALUES(
                1234567890021,
                "Pendudukan Belanda",
                "Marni Sumarno",
                "Kompas Penerbit",
                900,
                5,
                5
            );
"""

        self._conn.cursor().executescript(initiate_books)

        initiate_members = """
        INSERT into members VALUES(
            1234567890,
            "Samuel Kosasih"
            
        );

        INSERT into members VALUES(
            1234567891,
            "Jason Miraz"
            
        );

        INSERT into members VALUES(
            1234567892,
            "Munarman"
            
        );

        INSERT into members VALUES(
            1234567893,
            "Sutono Badri"
        );

        INSERT into members VALUES(
            1234567894,
            "Badia Sungko"
        );

        INSERT into members VALUES(
            1234567895,
            "Nanang Sugiono"
            
        );

        INSERT into members VALUES(
            1234567896,
            "Jani Sugoko"
            
        );

        INSERT into members VALUES(
            1234567897,
            "Sandrian Sukamtie"
            
        );

        INSERT into members VALUES(
            1234567898,
            "Pardito Siahaan"
            
        );

        INSERT into members VALUES(
            1234567899,
            "Samiun Basri"
            
        );

        INSERT into members VALUES(
            1234567811,
            "Gerald Young"
            
        );

        INSERT into members VALUES(
            1234567812,
            "Elenoar Young"
            
        );

        INSERT into members VALUES(
            1234567813,
            "Nick Young"
            
        );

        INSERT into members VALUES(
            1234567814,
            "Rachel Chung"
            
        );

        INSERT into members VALUES(
            1234567815,
            "Rachel Ying"
            
        );

        INSERT into members VALUES(
            1234567816,
            "Rana Del Roy"
            
        );

        INSERT into members VALUES(
            1234567817,
            "Warsito Adira"
            
        );

        INSERT into members VALUES(
            1234567818,
            "Jean McLouvre"
            
        );

        INSERT into members VALUES(
            1234567819,
            "Mary McMonne"
            
        );

        INSERT into members VALUES(
            1234567820,
            "Suganda Mulyo"
            
        );
        
"""

        self._conn.cursor().executescript(initiate_members)

    def init_borrows_dummy(self):
        self.pinjam_buku_by_isbn("1234567890", "1234567890001")
        self.pinjam_buku_by_isbn("1234567891", "1234567890001")
        self.pinjam_buku_by_isbn("1234567892", "1234567890001")
        self.pinjam_buku_by_isbn("1234567893", "1234567890001")
        self.pinjam_buku_by_isbn("1234567894", "1234567890001")
        self.pinjam_buku_by_isbn("1234567890", "1234567890002")
        self.pinjam_buku_by_isbn("1234567891", "1234567890002")
        self.pinjam_buku_by_isbn("1234567892", "1234567890002")
        self.pinjam_buku_by_isbn("1234567893", "1234567890002")
        self.pinjam_buku_by_isbn("1234567890", "1234567890003")
        self.pinjam_buku_by_isbn("1234567891", "1234567890003")
        self.pinjam_buku_by_isbn("1234567895", "1234567890004")
        self.pinjam_buku_by_isbn("1234567896", "1234567890004")
        self.pinjam_buku_by_isbn("1234567897", "1234567890004")
        self.pinjam_buku_by_isbn("1234567895", "1234567890005")
        self.pinjam_buku_by_isbn("1234567896", "1234567890005")
        self.pinjam_buku_by_isbn("1234567897", "1234567890006")
        self.pinjam_buku_by_isbn("1234567897", "1234567890007")
        self.pinjam_buku_by_isbn("1234567897", "1234567890008")
