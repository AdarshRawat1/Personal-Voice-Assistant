from Body.wish import wishMe
from Body.automation import queryToTask

from Body.intro import play_gif
from utils.command import takeCommand
from Controls.control import lang


if __name__ == "__main__":
    play_gif()
    wishMe(lang)
    while True:
        # if 1:
        query = takeCommand()
        query=query.lower()
        queryToTask(query)
