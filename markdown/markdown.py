"""
Set task: Refactor the given code, that parses markdown (String) and returns the associated HTML for that string.
Method:
* The code is split into lines and res (String), the empty result string is initiated.
* We loop through the lines. We first check if we have a headline, a list or a paragraph and wrap the text accordingly.
* If we have a list, the in_list (bool) variable tracks that we're inside a list. If we enter a headline or a paragraph with in_list active, the list gets closed before the next line gets computed.
* Next we check if the text contains bold and/or italic markers, and if so wrap those as well.
* We add each line to the result string. In the very end we close a potentially open list.
Example: parse("# Header!\n* __Bold Item__\n* _Italic Item_") (-> ["# Header!", "* __Bold Item__", "* _Italic Item_"]) -> "<h1>Header!</h1><ul><li><strong>Bold Item</strong></li><li><em>Italic Item</em></li></ul>"
"""

from re import match

def parse(markdown):
    lines = markdown.split("\n")
    res = ""
    in_list = False
    for i in lines:
        if i[0] == "#":
            # Headlines
            if in_list:
                i = f"</ul><h{i.find(' ')}>{i[i.find(' ')+1::]}</h{i.find(' ')}>"
                in_list = False
            else:
                i = f"<h{i.find(' ')}>{i[i.find(' ')+1::]}</h{i.find(' ')}>"
        elif i[0] == "*":
            # Lists
            if not in_list:
                i = f"<ul><li>{i[2::]}</li>"
                in_list = True
            else:
                i = f"<li>{i[2::]}</li>"
        else:
            # Paragraphs
            if in_list:
                i = f"</ul><p>{i}</p>"
                in_list = False
            else:
                i = f"<p>{i}</p>"
        bold = match('(.*)__(.*)__(.*)',i)
        if bold:
            i = f"{bold.group(1)}<strong>{bold.group(2)}</strong>{bold.group(3)}"
        italic = match('(.*)_(.*)_(.*)',i)
        if italic:
            i = f"{italic.group(1)}<em>{italic.group(2)}</em>{italic.group(3)}"
        res += i
    if in_list:
        res += "</ul>"
    return res

