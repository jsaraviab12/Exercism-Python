def recite(start_verse, end_verse):
    days = ["first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth"
            ,"seventh",
            "eighth",
            "ninth",
            "tenth",
            "eleventh",
            "twelfth"]
    strfirst = "On the "
    
    strlast = " day of Christmas my true love gave to me: "
    
    verses = ["a Partridge in a Pear Tree.",
              "two Turtle Doves, and ", "three French Hens, ",
              "four Calling Birds, ", 
              "five Gold Rings, ", 
              "six Geese-a-Laying, ",
              "seven Swans-a-Swimming, ",
              "eight Maids-a-Milking, ",
              "nine Ladies Dancing, ",
              "ten Lords-a-Leaping, ",
              "eleven Pipers Piping, ", 
              "twelve Drummers Drumming, "]
    
    return [strfirst + days[n-1] + strlast + ''.join(verses[n-1::-1]) for n in range(start_verse, end_verse+1)]
