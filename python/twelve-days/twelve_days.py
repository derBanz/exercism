"""
Set Task: Given start_verse (int) and end_verse (int), output the lyrics to "The Twelve Days of Christmas".
Method:
* song (list) contains the last part of each link, which is what was given on the xth day of Christmas.
* day (list) contains the days.
* Afterwards we loop through the verses and generate the output.
Example: recite(1,3) -> [
    'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.',
    'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.',
    'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.'
]
"""

def recite(start_verse, end_verse):
    song=["and a Partridge in a Pear Tree.", "two Turtle Doves, ", "three French Hens, ", "four Calling Birds, ", "five Gold Rings, ", "six Geese-a-Laying, ", "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ", "nine Ladies Dancing, ", "ten Lords-a-Leaping, ", "eleven Pipers Piping, ", "twelve Drummers Drumming, "]
    day=["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    lyrics=[]
    if start_verse==1:
        lyrics.append("On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")
        start_verse=2
    for r in range(start_verse-1,end_verse):
        verse="On the "+day[r]+" day of Christmas my true love gave to me: "
        for s in reversed(range(r+1)):
            verse+=song[s]
        lyrics.append(verse)

    return lyrics

print(recite(1,3))