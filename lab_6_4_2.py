import urllib.request
import time
from threading import Thread

<<<<<<< HEAD
=======

>>>>>>> 5923f3d (master)
sites = [
    "https://www.youtube.com/",
    "https://github.com/",
    "http://animego.org",
    "https://store.steampowered.com/",
<<<<<<< HEAD
    "https://github.com/",
=======
    "https://orioks.miet.ru/",
>>>>>>> 5923f3d (master)
    "https://classroom.google.com/",
    "https://www.microsoft.com/ru-ru/",
    "https://www.google.ru/?gws_rd=ssl",
    "https://translate.yandex.ru/",
    "https://ya.ru/"
]


<<<<<<< HEAD
def visit_sites():
    global sites
    for site in sites:
        tmp = time.time()
=======
def visit_sites(sites):
    for site in sites:
        print(f"Site: {site}")
>>>>>>> 5923f3d (master)
        urllib.request.urlopen(site)


start = time.time()
<<<<<<< HEAD
visit_sites()
visit_sites()
print(f"Without threading: {round(time.time() - start, 4)} seconds")
start = time.time()
for i in range(2):
    t = Thread(target=visit_sites())
    t.start()
=======
visit_sites(sites)
print(f"Without threading: {round(time.time() - start, 4)} seconds")
start = time.time()
t = Thread(target=visit_sites, args=(sites[:len(sites) // 2],))
t.start()
t1 = Thread(target=visit_sites, args=(sites[len(sites) // 2:],))
t1.start()
t.join()
t1.join()
>>>>>>> 5923f3d (master)
print(f"With threading: {round(time.time() - start, 4)} seconds")
