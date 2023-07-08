import math

from unit_of_work import UoW


def add_url(url):
    with UoW() as uow:
        url_repo = uow.get_url_repository()
        url = url_repo.add(url)
        url['url_short'] = convert_to_base62(url['id'])
        url_repo.update(url)
        uow.commit()


def convert_to_base62(number):
    map = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base = len(map)
    tmp = number
    result = []
    while tmp > 0:
        ratio = math.floor(tmp / base)
        reminder = tmp % base
        result.append(map[reminder])
        tmp = ratio

    result.reverse()
    return ''.join(result)
