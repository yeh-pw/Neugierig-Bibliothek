from nbibliothek_v1.services import NbibliothekService
import os
import sys


if __name__ == "__main__":

    db_cwd = os.getcwd()+r'\nbibliothek_v1\configs\db_path.txt'

    if os.stat(db_cwd).st_size == 0:
        db_path = os.getcwd()+r'\nbibliothek_v1\configs\nbibliothek.db'
    else:
        f = open(db_cwd, "r")
        db_path = f.readline()
        f.close()

    db_url = db_path
    init_db = ''

    # Normal Sys Taker
    for x in range(1, len(sys.argv)):

        a = sys.argv[x].split("=")

        if a[0].lower() == "-db:file":
            b = open(db_cwd, "w")
            b.write(a[1])
            db_url = a[1]
            b.close()

        elif sys.argv[x].lower() == "-db:init=true":
            init_db = 'apps.init_db()'

    # Bonus Sys Taker
    init_report_dummy = ''
    report_app = ''

    if "-apps:report" in sys.argv:
        if "-db:init=True" in sys.argv:
            init_report_dummy = 'apps.init_borrows_db_dummy()'
            report_app = 'apps.get_fav_books_for_dummy()'
        else:
            report_app = 'apps.get_fav_books_for_dummy()'
        apps = NbibliothekService(db_url)
        exec(init_report_dummy)
        exec(report_app)

    # Finally
    else:
        apps = NbibliothekService(db_url)
        exec(init_db)
        apps.run_ui()
