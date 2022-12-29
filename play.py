import pandas as pd
import random
import time
import re
import os



def process_lyrics(lyrics):
    lines = lyrics.split("\n")
    lyrics = ""
    for line in lines:
        if len(line) > 0 and not (line[0] == "[" or line[-1] == "]"):
            lyrics += line + "\n"
    return lyrics.split()
    

def pretty_time(t):
    mins = t // 60
    secs = t - (60 * mins)
    return "%dmin %dsec" % (mins, secs)


def clean_word(word):
    clean = re.sub('[^a-z0-9]+', '', word.lower())
    return clean


def make_lyric_dict(lyrics):
    dic = dict()
    for idx, l in enumerate(lyrics):
        clean = clean_word(l)

        if not clean in dic.keys():
            dic[clean] = dict()
            dic[clean]["guessed"] = False
            dic[clean]["n"] = 0

        dic[clean]["n"] += 1

    return dic


def update_mask(lyrics, dic):
    mask = []
    for l in lyrics:
        clean = clean_word(l)
        if dic[clean]["guessed"]:
            mask.append(l)
        else:
            mask.append("___")
    return mask


def main():
    # set up timer
    start = time.time()
    time_limit = 600 # 10min time limit

    # load data
    titles = open("song_titles.txt","r").read().split("\n")
    songs = pd.read_csv("songs.csv")

    # pick random song
    title = random.choice(titles)

    # get lyrics of song
    lyrics = songs.loc[songs["Title"] == title]["Lyrics"].tolist()[0]
    lyrics = process_lyrics(lyrics)
    dic = make_lyric_dict(lyrics)

    # initialize mask
    mask = ["___" for l in lyrics]
    n_guessed = 0

    # play game
    while time.time() < start + time_limit:
        remaining = round(start + time_limit - time.time())

        os.system("clear")
        print(" ".join(mask))
        print("%d of %d guessed" % (n_guessed, len(lyrics)))
        print("%s remaining" % pretty_time(remaining))
        print("Guess a word:")

        guess = input()
        if guess == "QUIT":
            print("you quit.")
            break
        clean_guess = clean_word(guess)

        if clean_guess in dic.keys() and not dic[clean_guess]["guessed"]:
            dic[clean_guess]["guessed"] = True
            n_guessed += dic[clean_guess]["n"]
            mask = update_mask(lyrics, dic)
            if n_guessed == len(lyrics):
                break

    if n_guessed == len(lyrics):
        elapsed = round(time.time() - start)
        print("You win! Time to finish: %s" % pretty_time(elapsed))
    else:
        print(" ".join(lyrics))
        print("You lose... the song was %s" % title)


if __name__ == "__main__":
    main()
