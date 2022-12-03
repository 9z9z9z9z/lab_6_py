import urllib.request
import time
from threading import Thread

sites = [
    "https://www.youtube.com/",
    "https://github.com/",
    "http://animego.org",
    "https://store.steampowered.com/",
    "https://github.com/",
    "https://classroom.google.com/",
    "https://www.microsoft.com/ru-ru/",
    "https://www.google.ru/?gws_rd=ssl",
    "https://translate.yandex.ru/",
    "https://ya.ru/"
]


def visit_sites():
    global sites
    for site in sites:
        tmp = time.time()
        urllib.request.urlopen(site)


start = time.time()
visit_sites()
visit_sites()
print(f"Without threading: {round(time.time() - start, 4)} seconds")
start = time.time()
for i in range(2):
    t = Thread(target=visit_sites())
    t.start()
print(f"With threading: {round(time.time() - start, 4)} seconds")
