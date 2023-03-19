from transliterate import translit
import requests
import time
import sqlite3


def check(INN):
    url = 'http://v1738409.hosted-by-vdsina.ru/api/v1/docs/auth/uploads/company/'
    params = dict()
    try:
        params['itn'] = int(INN)
        response = requests.get(url, params=params).json()
        return response['id']
    except Exception:
        return {}


def post_company(email, password, username, itn):
    url = 'http://v1738409.hosted-by-vdsina.ru/api/v1/docs/auth/register/'
    params = dict()
    params['email'] = email.replace('№', '')
    params['password'] = password
    params['username'] = username
    params['status'] = 2
    params['name'] = ''
    params['surname'] = ''
    try:
        params['itn'] = int(itn)
        response = requests.post(url, json=params).json()
        return response['id']
    except Exception:
        pass


def main_company(cur):
        results = cur.execute("""SELECT DISTINCT "Клиент*", "ИНН" FROM data""").fetchall()
        for i in results:
            INN = i[1]
            res = check(INN)
            if len(res) == 0:
                name_company = i[0].lower().replace(' ', '').replace('"', '').replace("'", "")
                email = translit(name_company, 'ru', True).replace("'", "") + '@gmail.com'
                password = translit(name_company, 'ru', True).replace("'", "")
                ID_company = post_company(email, password, i[0], INN)
            else:
                ID_company = res

if __name__ == '__main__':
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    tm = time.time()
    main_company(cur)
