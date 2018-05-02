"""Решение домашнего задания №16 курса Нетология Пайтон."""
import requests


def getfriends(token, version, source_uid):
    """Запрос ID друзей пользователя."""
    params = {
        'user_id': source_uid,
        'access_token': token,
        'v': version
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    friends = response.json()['response']['items']
    return friends


def findcommonfriends(token, version, source_uid, target_uids):
    """Запрос ID общий друзей пользователя и списка друзей пользователя."""
    params = {
        'source_uid': source_uid,
        'target_uids': target_uids,
        'access_token': token,
        'v': version
    }
    response = \
        requests.get('https://api.vk.com/method/friends.getMutual', params)
    public_friends = response.json()['response']
    return public_friends


def main():
    """Инициализация программы и вывод результатов."""
    VERSION = '5.74'
    TOKEN = \
        '4adc0458cb22fdb75db1ac1ce82ed636ca48327ba46b7c5e' \
        '57bf4f544a02b56544597fd5965c3d862cebd'
    url_users_vk = 'https://vk.com/id'
    choose = 0

    print('ПОИСК ОБЩИХ ДРУЗЕЙ:')
    print('Между произвольными ID (1)')
    print('Среди друзей друзей (2)')

    while not(choose == '1' or choose == '2'):
        choose = input('? ')
        if choose == '1' or choose == '2':
            user_id = int(input('Введите ID пользователя '))

        if choose == '1':
            friends = int(input('Введите ID другого пользователя '))
        elif choose == '2':
            friends = getfriends(TOKEN, VERSION, user_id)

        if choose == '1' or choose == '2':
            public_friends = \
                findcommonfriends(TOKEN, VERSION, user_id, friends)
            for friend in public_friends:
                print('Общие друзья ID {} ({}) и ID {} ({}):'.
                      format(user_id, url_users_vk + str(user_id),
                             friend['id'], url_users_vk + str(friend['id'])))
                for common_friend in friend['common_friends']:
                    print('ID - {} {}'.
                          format(common_friend,
                                 url_users_vk + str(common_friend)))


main()
