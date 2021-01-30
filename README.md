# Neugierig-Bibliothek
Neugierig-Bibliothek is a simple example of a library software. Based on SQLite as database and Python as language. 

# Requirements
* Python3
* SQLite
* Matplotlib
* Pytest
* Py-Googletrans 4.0.0-rc1
    * Used in v3 (Automatically installing by running v3 if not installed).

# Features
* Searching registered member.
* Searching available book.
* Borrowing a book.
* Returning a book.
* Showing graphic of five favorite book in current month.

# Input Arguments
* nbibliothek_v1
   - -db:file=xxxx\yyyy.db | Change database directory, where xxxx : directory address, and yyyy : database name.
   - -db:init=True | Initialize datas on new database.
   - -apps:report | Printing 5 most borrowed books in the current month.
      - -apps:report -db:init=True | Initialize dummy data of borrows and print 5 of the favorite books in the current month.
 
 * nbibliothek_v2
   - All arguments of v1.
   - -lang=xx | Where xx is either EN (English) or ID (Bahasa Indonesia).
      - Could add -lang=xx along with -apps:report
      
 * nbibliothek_v3
   - All arguments of v2.
   - More language support, examples:
      - -lang=DE (Deutsch), -lang=AR (Arabic), -lang=ZH-CN (China Mainland), etc.
      - Please refer to https://cloud.google.com/translate/docs/languages for more language support.
 
 
# Usage Example
-

 
 
