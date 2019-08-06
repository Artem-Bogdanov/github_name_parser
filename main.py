from requests import get
from typing import List
from termcolor import colored
from threading import Thread


GITHUB_LINK: str = 'https://github.com/'


def get_names() -> List[str]:
    return ['god', 'god2131231']


def check_name(name: str) -> bool:
    profile_link: str = GITHUB_LINK + name
    req = get(profile_link)
    status_code: int = req.status_code
    if status_code == 200:
        print(colored('Name is busy: ' + name, 'red'))
    elif status_code == 404:
        print(colored('Name is free: ' + name, 'green'))
        

def check_names(names_list: List[str]):
    th_list: List[Thread] = list()
    for name in names_list:
        th: Thread = Thread(target=check_name, args=(name,), name='checking name: ' + name)
        th.start()
        th_list.append(th)

    for th in th_list:
        if th.is_alive():
            th.join()


if __name__ == "__main__":
    names: List[str] = get_names()
    check_names(names)