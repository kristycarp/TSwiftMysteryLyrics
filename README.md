# Taylor Swift Mystery Lyrics Quiz
## Created by Kristy Carpenter

Taking inspiration from the numerous Sporcle quizzes that follow this format, I have created a script that will randomly pick a Taylor Swift song for you to guess the lyrics to. As you guess words, any correct guesses will be filled in. You have 10 minutes to try to guess all the lyrics to the mystery song.

Credit to `@shaynak` for scraping the song titles and lyrics -- I have taken `song_titles.txt` and `songs.csv` from her [Taylor Swift Lyric Scraper](https://github.com/shaynak/taylor-swift-lyrics) repository.

This is a work in progress and may have some bugs. Please feel free to let me know if you notice anything. Also I am not really into the whole web dev thing so it is a Python script for now but I might try to make it prettier/easier in the future.

### Usage
This script requires the `pandas` library.

Start the game with `python play.py`. You may then type your guesses. Each guess should only be one word. Guesses are case-insensitive and do not require punctuation.