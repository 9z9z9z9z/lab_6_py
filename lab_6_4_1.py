import urllib.request
import time
from threading import Thread


sites = [
    "https://www.youtube.com/",
    "https://github.com/",
    "http://animego.org",
    "https://store.steampowered.com/",
    "https://github.com/",
    "https://orioks.miet.ru/",
    "https://classroom.google.com/",
    "https://www.microsoft.com/ru-ru/",
    "https://www.google.ru/?gws_rd=ssl",
    "https://translate.yandex.ru/",
    "https://ya.ru/"
]


def visit_sites(sites):
    for site in sites:
        urllib.request.urlopen(site)


start = time.time()
visit_sites(sites)
print(f"Without threading: {round(time.time() - start, 4)} seconds")
start = time.time()
t = Thread(target=visit_sites, args=(sites[:len(sites) // 2],))
t1 = Thread(target=visit_sites, args=(sites[len(sites) // 2:],))
t.start()
t1.start()
t.join()
t1.join()
print(f"With threading: {round(time.time() - start, 4)} seconds")
