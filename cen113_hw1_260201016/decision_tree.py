"""260201016"""
import sys
outlook = sys.argv[1]
temperature = sys.argv[2]
humidity = sys.argv[3]
windy = sys.argv[4]

if outlook == "overcast":
    play = "The match will be played"
if outlook == "sunny":
    if humidity == "high":
        play = "The match will not be played"
    else:
        play = "The match will be played"
if outlook == "rain":
    if windy == "true":
        play = "The match will not be played"
    else:
        play = "The match will be played"
print(play)        
