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