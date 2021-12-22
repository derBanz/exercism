"""
Set task: Provide an abbreviation of the input words (String).
Method:
* Start with an empty result (String), define valid characters to be used in the abbreviation, split the input into separate words.
* Loop through each word
** Add the first valid character to the result.
** If the word is a composite linked by a hyphen, also add the first valid character after the hyphen to the result.
Example: abbreviate("Portable Network Graphics") -> "PNG"
"""

def abbreviate(words): 
    res="" 
    vocab = "abcdefghifjklmnopqrstuvwxyz" 
    words=words.split() 
    for w in words: 
        for i in w: 
            if i.lower() in vocab:
                res+=i.upper()
                break
        if "-" in w and len(w)>1: 
            for i in w[w.find("-")::]:
                if i.lower() in vocab:
                    res+=i.upper()
                    break
        
    return res