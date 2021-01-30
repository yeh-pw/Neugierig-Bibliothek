class BooksDTO:
    def __init__(self, isbn, title, author, publisher, classification, availability, quantity):
        self._isbn = isbn
        self._title = title
        self._author = author
        self._publisher = publisher
        self._classification = classification
        self._availability = availability
        self._quantity = quantity

    @property
    def isbn(self):
        return self._isbn

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def publisher(self):
        return self._publisher

    @property
    def classification(self):
        return self._classification

    @property
    def availability(self):
        return self._availability

    @property
    def quantity(self):
        return self._quantity


class MemberDTO:
    def __init__(self, nim, name):
        self._nim = nim
        self._name = name

    @property
    def nim(self):
        return self._nim

    @property
    def name(self):
        return self._name


class BorrowsDTO:
    def __init__(self, nim, isbn, title, tgl_pinjam, tgl_return, tgl_returned):
        self._nim = nim
        self._isbn = isbn
        self._title = title
        self._tgl_pinjam = tgl_pinjam
        self._tgl_return = tgl_return
        self._tgl_returned = tgl_returned

    @property
    def nim(self):
        return self._nim

    @property
    def isbn(self):
        return self._isbn

    @property
    def title(self):
        return self._title

    @property
    def tgl_pinjam(self):
        return self._tgl_pinjam

    @property
    def tgl_return(self):
        return self._tgl_return

    @property
    def tgl_returned(self):
        return self._tgl_returned


class ChartsDTO:
    def __init__(self, isbn, title, score):
        self._isbn = isbn
        self._title = title
        self._score = score

    @property
    def isbn(self):
        return self._isbn

    @property
    def title(self):
        return self._title

    @property
    def score(self):
        return self._score


class SuggestionBookDTO:
    def __init__(self, title, isbn):
        self._title = title
        self._isbn = isbn

    @property
    def title(self):
        return self._title

    @property
    def isbn(self):
        return self._isbn

    @property
    def listbox_fill(self):
        return f"{self._title} ({self.isbn})"


class SuggestionMemberDTO:
    def __init__(self, name, nim):
        self._name = name
        self._nim = nim

    @property
    def name(self):
        return self._name

    @property
    def nim(self):
        return self._nim

    @property
    def listbox_fill(self):
        return f"{self._name} ({self.nim})"
