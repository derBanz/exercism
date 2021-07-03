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
        print(verse)
        lyrics.append(verse)

    return lyrics

recite(3,3)