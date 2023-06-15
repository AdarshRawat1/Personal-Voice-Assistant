#make alarm https://www.youtube.com/watch?v=rgGDTO8g2Pg
from Body.wish import wishMe
from Body.automation import queryToTask
from utils.listen import takeCommand
from Controls.control import lang

if __name__ == "__main__":
    wishMe(lang)
    while True:
        # if 1:
        query = takeCommand()
        query=query.lower()
        queryToTask(query)
