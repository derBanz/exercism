"""
Set task: Encode a plain_text (String) according to the Crypto Square Cipher.
Method:
* The plain_text is cleared of punctuation, whitespace and special characters.
* Column and row amount of the crypto square are defined and both rows (list) and columns (list) defined.
* The text gets filled into the rows.
* We loop through the rows and fill the nth character in each row into the nth column.
* Finally the columns are returned in order separated by a space.
Example: cipher_text("Chill out.") (-> "chillout" -> ["chi","llo","ut "] -> ["clu", "hlt", "io "]) -> "clu hlt io "
"""

from math import ceil, sqrt

def cipher_text(plain_text):
    text = ""
    for i in plain_text:
        if i not in "!\"§$%&/()=?`´'#,;.:<>|-_ \n@7":
            text += i.lower()
    if text == "":
        return ""
    c = int(ceil(sqrt(len(text))))
    r = int(ceil(len(text) / c))
    text += " " * ((c * r) - len(text))
    rows = list()
    columns = list()
    for i in range(r):
        rows.append(text[i * c:(i + 1) * c])
    for i in range(c):
        txt = ""
        for j in range(r):
            txt += rows[j][i]
        columns.append(txt)
    res = ""
    for i in columns:
        res += i + " "
    return res[:-1:]