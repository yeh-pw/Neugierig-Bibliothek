# Neugierig-Bibliothek
Neugierig-Bibliothek is an example of a library software. Based on SQLite as database and Python as language. This software could do searching book and member of the library. If the book and the member exist, You could return it. There are 3 versions of nbibliothek, the first version is Bahasa Indonesia based, the second version could change to English. The first and second version get their words from .json file attached in the configs. The difference is v1 is the factory method for language is 'locked' in Bahasa Indonesia, and in the v2 with inheriting the service of the v1, 'unlocking' the factory method so that the language could be change by an argument (default : Bahasa Indonesia). And on the v3 the language is obtained by Google Translate API.

# Requirements
* Python3
* Matplotlib
* Pytest
* Py-Googletrans 4.0.0-rc1
    * Used in v3 (Automatically installed by running v3 if not installed)

# Usage Example
-

 
 
