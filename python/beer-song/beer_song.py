"""
Set task: Recite the lyrics to the song '99 Bottles of Beer on the Wall'.
Method: Lyrics are stored in lyrics (list), looping through depending on
        bottles.
Example: recite(10, 2) -> ['10 bottles...', 'Take one...', ...]
"""


def recite(start, take=1):
    lyrics = list()
    bottles = start
    while bottles >= 0 and bottles > start - take:
        if bottles == 0:
            lyrics.extend([
                "No more bottles of beer on the wall, "
                "no more bottles of beer.",
                "Go to the store and buy some more, "
                "99 bottles of beer on the wall.",
                ""
            ])
        elif bottles == 1:
            lyrics.extend([
                "1 bottle of beer on the wall, "
                "1 bottle of beer.",
                "Take it down and pass it around, "
                "no more bottles of beer on the wall.",
                ""
            ])
        elif bottles == 2:
            lyrics.extend([
                "2 bottles of beer on the wall, "
                "2 bottles of beer.",
                "Take one down and pass it around, "
                "1 bottle of beer on the wall.",
                ""
            ])
        else:
            lyrics.extend([
                f"{bottles} bottles of beer on the wall, "
                f"{bottles} bottles of beer.",
                "Take one down and pass it around, "
                f"{bottles - 1} bottles of beer on the wall.",
                ""
            ])
        bottles -= 1
    return lyrics[:-1]
