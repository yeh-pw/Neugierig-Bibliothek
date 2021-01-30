import re
from tkinter import *
from tkinter import ttk
from datetime import *
from functools import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib as plt
from matplotlib.figure import Figure
from numpy.core.fromnumeric import size
plt.use("TkAgg")


class NbibliothekUI:
    def __init__(self, nbibliothek_service):

        self._window = Tk()
        self._nbibliothek_service = nbibliothek_service
        self._languagemanager = self._nbibliothek_service.lang_manager()

        self._window.geometry("750x650")

        self._window.title("Neugierig Bibliothek")
        self._window.resizable(0, 0)
        Label(self._window, text="Neugierig Bibliothek", font="none 12 bold").pack(
            side=TOP, anchor=NW, expand=False)
        Label(self._window, text="IIse. Str No.21",
              font="none 12 bold").pack(side=TOP, anchor=NW)
        Label(self._window, text="Berlin - 12053",
              font="none 12 bold").pack(side=TOP, anchor=NW)
        Label(self._window, text=f"{datetime.today().strftime('%d-%m-%Y')}",
              font="none 12 bold").place(x=650, y=0)
        Label(self._window, bg="gray33").pack(side=TOP, fill="both")

        self._notebooku = ttk.Notebook(self._window)
        self._notebooku.pack(pady=1)

        self._framecari = Frame(self._notebooku, width=750, height=650)

        self._framelaporan = Frame(self._notebooku, width=750, height=650)

        self._initframecari = self._notebooku.add(
            self._framecari, text=self._languagemanager.get_words("label_cari"))

        self._initframelaporan = self._notebooku.add(
            self._framelaporan, text=self._languagemanager.get_words("laporan"))

        self._labelcari = Label(self._framecari, font="none 11 bold", text=self._languagemanager.get_words("label_cari")).place(
            x=4, y=5)
        self._labelcariseparator = Label(
            self._framecari, text=":", font="none 11 bold").place(x=275, y=4)

        # ENTRY CARI JUDUL IS DOWN BELOW DUE MODIFICATION

        self._buttoncari_judul = Button(
            self._framecari, width=15, text=self._languagemanager.get_words("tombol_cari"), command=self.search_book_clicked)
        self._buttoncari_judul.place(x=625, y=5)

        self._statuscarijudul = Label(
            self._framecari, font="none 11 bold")
        self._statuscarijudul.place(x=175, y=35)
        self._statuscarijudul.config(width=47)

        self._baganbuku = Label(
            self._framecari, font="none 11 bold", bg="gray78", text=self._languagemanager.get_words("buku")).place(x=4, y=70)

        self._judulbuku = Label(
            self._framecari, font="none 10", text=self._languagemanager.get_words("judul")).place(x=4, y=105)

        self._judulbukuseparator = Label(self._framecari, text=":",
                                         font="none 11 bold").place(x=275, y=105)

        self._hasiljudul = Label(
            self._framecari, font="none 10")
        self._hasiljudul.place(x=300, y=105)

        self._pengarangbuku = Label(
            self._framecari, font="none 10", text=self._languagemanager.get_words("pengarang")).place(x=4, y=130)

        self._pengarangbukuseparator = Label(
            self._framecari, text=":", font="none 11 bold").place(x=275, y=130)

        self._hasilpengarangbuku = Label(
            self._framecari, font="none 10")

        self._hasilpengarangbuku.place(x=300, y=130)
        self._penerbitbuku = Label(
            self._framecari, font="none 10", text=self._languagemanager.get_words("penerbit")).place(x=4, y=155)

        self._penerbitbukuseparator = Label(self._framecari, text=":",
                                            font="none 11 bold").place(x=275, y=155)

        self._hasilpenerbitbuku = Label(
            self._framecari, font="none 10")
        self._hasilpenerbitbuku.place(x=300, y=155)

        self._hasilpenerbitbukuseparator = Label(self._framecari, text=":",
                                                 font="none 11 bold").place(x=275, y=155)

        self._noklasifikasi = Label(
            self._framecari, font="none 10", text=self._languagemanager.get_words("no_klasifikasi")).place(x=4, y=180)
        self._separtornoklasifikasi = Label(self._framecari, text=":",
                                            font="none 11 bold").place(x=275, y=180)

        self._hasilnoklasifikasi = Label(
            self._framecari, font="none 10")
        self._hasilnoklasifikasi.place(x=300, y=180)

        self._nobarcode = Label(
            self._framecari, font="none 10", text=self._languagemanager.get_words("isbn")).place(x=4, y=205)

        self._separatornobarcode = Label(self._framecari, text=":",
                                         font="none 11 bold").place(x=275, y=205)

        self._hasilnobarcode = Label(
            self._framecari, font="none 10")
        self._hasilnobarcode.place(x=300, y=205)

        self._exemplar = Label(
            self._framecari, font="none 10", text=self._languagemanager.get_words("eksemplar")).place(x=4, y=230)

        self._separatorexemplar = Label(self._framecari, text=":",
                                        font="none 11 bold").place(x=275, y=230)
        self._hasilexemplar = Label(
            self._framecari, font="none 10")
        self._hasilexemplar.place(x=300, y=230)

        # Member section.
        self._labelnimcari = Label(
            self._framecari, font="none 11 bold", text=self._languagemanager.get_words("nim")).place(x=4, y=255)

        # ENTRY NIM IS DOWN BELOW DUE TO MODIFICATION
        self._buttoncarinim = Button(
            self._framecari, width=15, text=self._languagemanager.get_words("tombol_cari"), command=self.search_nim_clicked)
        self._buttoncarinim.place(x=625, y=255)

        self._buttonpinjam = Button(
            self._framecari, width=15, text=self._languagemanager.get_words("tombol_pinjam"), command=self.pinjam_clicked)
        self._buttonpinjam.place(x=625, y=285)

        self._statuscarinim = Label(
            self._framecari, font="none 11 bold")
        self._statuscarinim.config(width=47)
        self._statuscarinim.place(x=175, y=285)

        self._separatorcarinim = Label(self._framecari, text=":",
                                       font="none 11 bold").place(x=275, y=255)

        self._labelmember = Label(
            self._framecari, font="none 11 bold", text=self._languagemanager.get_words("anggota"), bg="gray78").place(x=4, y=310)

        self._namamember = Label(
            self._framecari, font="none 10", text=self._languagemanager.get_words("nama")).place(x=4, y=335)

        self._separatornamamember = Label(self._framecari, text=":",
                                          font="none 11 bold").place(x=275, y=335)
        self._hasilnamamember = Label(
            self._framecari, font="none 10")
        self._hasilnamamember.place(x=300, y=335)

        self._hasilnimcari = Label(
            self._framecari, font="none 10")
        self._hasilnimcari.place(x=300, y=360)

        self._nimcari = Label(
            self._framecari, font="none 10", text=self._languagemanager.get_words("nim")).place(x=4, y=360)

        self._separatornimcari = Label(self._framecari, text=":",
                                       font="none 11 bold").place(x=275, y=360)

        self._tanggalkembali = Label(
            self._framecari, font="none 10", text=self._languagemanager.get_words("tanggal_kembali")).place(x=4, y=385)

        self._separatortanggalkembali = Label(
            self._framecari, font="none 11 bold", text=":").place(x=275, y=385)

        self._hasiltanggalkembali = Label(self._framecari, font="none 10")
        self._hasiltanggalkembali.place(x=300, y=385)

        self._labelpeminjaman = Label(
            self._framecari, font="none 10", text=self._languagemanager.get_words("peminjaman")).place(x=4, y=410)

        self._separatorpeminjaman = Label(
            self._framecari, font="none 11 bold", text=":"
        ).place(x=275, y=410)

        self._hasilpeminjaman = []  # x = 350
        self._buttonpengembalian = []

        self._buttonshowchart = Button(
            self._framelaporan, text=self._languagemanager.get_words("tampilkanchartbukupopuler"), command=self.draw_chart, bg="yellow")
        self._buttonshowchart.pack(side=TOP, fill=X, expand=False)

        self._titles = []
        self._scores = []
        self._legends = []
        self._fig = Figure()
        self._ax = self._fig.add_subplot()
        self._canvas = FigureCanvasTkAgg(
            self._fig, master=self._framelaporan)
        self._canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        self._ax.pie([1], labels=[""])

        # Entry for Searching Book Title(ISBN)
        self._sv_book = StringVar()
        self._sv_book.trace("w", self.suggestions_book)
        self._entrycarijudul = Entry(
            self._framecari, width=50, bg="yellow", textvariable=self._sv_book)
        self._entrycarijudul.place(x=300, y=6)

        # Below is frame for listbox and scrollbar.
        # 1 width of frame != 1 width of listbox.
        # But fortunately frame size can be dynamic.
        self._framesuggest_book = Frame(self._framecari)
        self._suggestlb_searchbook = Listbox(
            self._framesuggest_book, width=50, selectmode=SINGLE)
        self._suggestlb_searchbook.bind(
            '<Double-1>', self.suggestion_to_entry_book)
        self._scrollbarbook = Scrollbar(
            self._framesuggest_book, command=self._suggestlb_searchbook.yview, orient=VERTICAL)
        self._suggestlb_searchbook.config(
            yscrollcommand=self._scrollbarbook.set)

        # Entry for Searching Member Name(NIM)
        self._sv_member = StringVar()
        self._sv_member.trace("w", self.suggestions_member)
        self._entrynim = Entry(
            self._framecari, width=50, bg="yellow", textvariable=self._sv_member)
        self._entrynim.place(x=300, y=255)

        self._framesuggest_member = Frame(self._framecari)
        self._suggestlb_searchmember = Listbox(
            self._framesuggest_member, width=50, selectmode=SINGLE)
        self._suggestlb_searchmember.bind(
            '<Double-1>', self.suggestion_to_entry_member
        )
        self._scrollbarmember = Scrollbar(
            self._framesuggest_member, command=self._suggestlb_searchmember.yview, orient=VERTICAL)
        self._suggestlb_searchmember.config(
            yscrollcommand=self._scrollbarmember.set)

    def suggestion_member_cleaner(self):
        self._suggestlb_searchmember.pack_forget()
        self._scrollbarmember.pack_forget()
        self._framesuggest_member.place_forget()

    def suggestion_to_entry_member(self, *args):
        event = self._suggestlb_searchmember.curselection()
        text = self._suggestlb_searchmember.get(event)
        self._entrynim.delete(0, END)
        self._entrynim.insert(0, text)
        self._suggestlb_searchmember.delete(0, 'end')
        self.suggestion_member_cleaner()

    def suggestions_member(self, *args):
        self._suggestlb_searchmember.delete(0, 'end')
        self.suggestion_member_cleaner()
        val = self._sv_member.get()
        if not val:
            self.suggestion_member_cleaner()
        elif len(self._nbibliothek_service.get_suggest_member(val)) == 0 or val.isspace() == True:
            self.suggestion_member_cleaner()
        else:
            suggests_member = self._nbibliothek_service.get_suggest_member(val)
            len_lb = len(suggests_member)
            for x in suggests_member:
                self._suggestlb_searchmember.insert(END, x.listbox_fill)
            if len_lb > 10:
                len_lb = 10
            else:
                len_lb = len_lb
            self._framesuggest_member.place(x=300, y=272)
            self._suggestlb_searchmember.config(height=len_lb)
            self._suggestlb_searchmember.pack(side=LEFT)
            if len(self._nbibliothek_service.get_suggest_book(val)) > 10:
                self._scrollbarmember.pack(side=RIGHT, fill=Y)

    def suggestion_book_cleaner(self):
        self._suggestlb_searchbook.pack_forget()
        self._scrollbarbook.pack_forget()
        self._framesuggest_book.place_forget()

    def suggestion_to_entry_book(self, *args):
        event = self._suggestlb_searchbook.curselection()
        text = self._suggestlb_searchbook.get(event)
        self._entrycarijudul.delete(0, END)
        self._entrycarijudul.insert(0, text)
        self._suggestlb_searchbook.delete(0, 'end')
        self.suggestion_book_cleaner()

    def suggestions_book(self, *args):
        self._suggestlb_searchbook.delete(0, 'end')
        self.suggestion_book_cleaner()
        val = self._sv_book.get()
        if not val:
            self.suggestion_book_cleaner()
        elif len(self._nbibliothek_service.get_suggest_book(val)) == 0 or val.isspace() == True:
            self.suggestion_book_cleaner()
        else:
            suggests_books = self._nbibliothek_service.get_suggest_book(val)
            len_lb = len(suggests_books)
            for x in suggests_books:
                self._suggestlb_searchbook.insert(END, x.listbox_fill)
            if len_lb > 10:
                len_lb = 10
            else:
                len_lb = len_lb
            self._framesuggest_book.place(x=300, y=25)
            self._suggestlb_searchbook.config(height=len_lb)
            self._suggestlb_searchbook.pack(side=LEFT)
            if len(self._nbibliothek_service.get_suggest_book(val)) > 10:
                self._scrollbarbook.pack(side=RIGHT, fill=Y)

    def draw_chart(self):
        fav_books = self._nbibliothek_service.get_fav_books_for_chart()
        self._ax.clear()
        self._titles.clear()
        self._scores.clear()
        self._legends.clear()
        for x in fav_books:
            self._titles.append(f"{x.title}-{x.score}x")
            self._scores.append(x.score)
            self._legends.append(x.isbn)
        if len(fav_books) == 0:
            self._ax.set_title(
                self._languagemanager.get_words("belumadabukudipinjam"))
            self._ax.pie([1], labels=[""])
            self._canvas.draw()
        else:
            self._ax.pie(self._scores, labels=self._titles)
            self._ax.axis('equal')
            self._ax.legend(labels=self._legends, title=self._languagemanager.get_words(
                "isbn"), loc="upper right", bbox_to_anchor=(0.145, 1.155))
            self._canvas.draw()

    def search_book_clicked(self):
        entry = self._entrycarijudul.get()
        entry_re = re.search(r"\(([A-Za-z0-9_]+)\)", entry)
        if entry_re is None:
            self._statuscarijudul.config(
                bg="red", text=self._languagemanager.get_words("buku_gak_ada"))
            self._nbibliothek_service.register_search_observer(entry)
            self._nbibliothek_service.notify_search(entry)
            return False
        current_isbn = entry_re[1]

        book = self._nbibliothek_service.get_book_by_isbn(current_isbn)
        if book is None:
            self._statuscarijudul.config(
                bg="red", text=self._languagemanager.get_words("buku_gak_ada"))
            self._nbibliothek_service.register_search_observer(entry)
            self._nbibliothek_service.notify_search(entry)
            return False
        else:
            self._statuscarijudul.config(
                bg="lime green", text=self._languagemanager.get_words("buku_ada"))
            self._hasiljudul.config(text=book.title)
            self._hasilpengarangbuku.config(text=book.author)
            self._hasilpenerbitbuku.config(text=book.publisher)
            self._hasilnoklasifikasi.config(text=book.classification)
            self._hasilnobarcode.config(text=book.isbn)
            self._hasilexemplar.config(
                text=f"{book.availability}/{book.quantity}")
            return True

    def show_borrows(self):
        get_entry = self._entrynim.get()
        get_entry_re = re.search(r"\(([A-Za-z0-9_]+)\)", get_entry)
        entry = get_entry_re[1]
        pinjaman = self._nbibliothek_service.get_current_borrows_by_nim(
            entry)
        ycoor = 410
        for x in range(len(pinjaman)):
            self._hasilpeminjaman.append(
                Label(self._framecari, font="none 10", text=f"{pinjaman[x].title} ({pinjaman[x].isbn})"))
            self._hasilpeminjaman[x].place(x=300, y=ycoor)
            self._buttonpengembalian.append(Button(
                self._framecari, text=self._languagemanager.get_words("tombol_kembalikan"), width=15, command=partial(self.kembalikan_clicked, x)))
            self._buttonpengembalian[x].place(x=625, y=ycoor)
            ycoor += 25

    def clear_borrows(self):
        g = self._buttonpengembalian
        if len(g) != 0:
            for x in range(len(g)):

                self._hasilpeminjaman[x].destroy()
                self._buttonpengembalian[x].destroy()
            self._hasilpeminjaman.clear()
            self._buttonpengembalian.clear()

    def search_nim_clicked(self):
        self.clear_borrows()
        self._hasiltanggalkembali.config(text="")
        get_entry = self._entrynim.get()
        get_entry_re = re.search(r"\(([A-Za-z0-9_]+)\)", get_entry)
        entry = get_entry_re[1]
        member = self._nbibliothek_service.get_member_by_nim(entry)
        if member is None:
            self._statuscarinim.config(
                bg="red", text=self._languagemanager.get_words("nim_tidak_ada"))
            return False
        else:
            self.show_borrows()
            self._statuscarinim.config(
                bg="lime green", text=self._languagemanager.get_words("nim_ada"))
            self._hasilnamamember.config(text=member.name)
            self._hasilnimcari.config(text=member.nim)
            return True

    def pinjam_clicked(self):
        get_entry_nim = self._entrynim.get()
        get_entry_re = re.search(r"\(([A-Za-z0-9_]+)\)", get_entry_nim)
        entry_nim = get_entry_re[1]
        entry_search_book = self._entrycarijudul.get()
        entry_re = re.search(r"\(([A-Za-z0-9_]+)\)", entry_search_book)
        if entry_re == None:
            self._buttoncari_judul.invoke()
            self._buttoncarinim.invoke()
            return None
        current_isbn = entry_re[1]
        if self.search_nim_clicked() is True and self.search_book_clicked() is True:

            if self._nbibliothek_service.if_already_borrows_x_books(entry_nim, current_isbn) == True:
                self._statuscarinim.config(text=self._languagemanager.get_words(
                    "lagipinjamjudulini"), bg="red")
            elif self._nbibliothek_service.if_max_quota_borrows(entry_nim) == True:
                self._statuscarinim.config(text=self._languagemanager.get_words(
                    "max_pinjam"), bg="red")
            else:
                self._nbibliothek_service.pinjam_buku_by_isbn(
                    entry_nim,  current_isbn)
                self._statuscarinim.config(text=self._languagemanager.get_words(
                    "berhasil_pinjam"), bg="lime green")
                oneweek = (datetime.today() + timedelta(days=7)
                           ).strftime('%d-%m-%Y')

                self._hasiltanggalkembali.config(text=oneweek)
                self._buttoncari_judul.invoke()
                self.clear_borrows()
                self.show_borrows()
                self._buttonshowchart.invoke()

    def kembalikan_clicked(self, n):
        bindex = (self._buttonpengembalian[n])
        titleindex = (self._hasilpeminjaman[n])
        judul = self._hasilpeminjaman[n].cget("text")
        isbn_in_judul = re.search(r"\(([0-9_]+)\)", judul)
        current_isbn = isbn_in_judul[1]
        get_entry_nim = self._entrynim.get()
        get_entry_re = re.search(r"\(([A-Za-z0-9_]+)\)", get_entry_nim)
        entrynim = get_entry_re[1]
        self._nbibliothek_service.kembalikan_buku_by_isbn(
            entrynim, current_isbn)
        get_books = self._nbibliothek_service.get_book_by_isbn(
            current_isbn)
        dipinjam = get_books.quantity - get_books.availability
        jumlahbuku = get_books.quantity
        self._nbibliothek_service.register_return_observer(
            judul, dipinjam, jumlahbuku)
        self._nbibliothek_service.notify_return_observer(judul)
        bindex.destroy()
        titleindex.destroy()
        self._buttonpengembalian.pop(n)
        self._hasilpeminjaman.pop(n)
        if self._entrycarijudul.get() == judul:
            self._buttoncari_judul.invoke()
        self.clear_borrows()
        self.show_borrows()

    def mainloop(self):
        self._window.mainloop()
