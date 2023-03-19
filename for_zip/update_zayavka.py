import sqlite3
import time
import requests
import datetime


GLOBAL_SERVICES = {
    'ШПД': 1, 'Видеонаблюдение Феррари': 2, 'VPN': 3, 'Телефон': 4, None: 5, 'ШПД,': 6, 'Виртуальная АТС': 7,
    'IPTV, ШПД': 8, 'VOIP': 9, 'Видеонаблюдение': 10, 'IPTV': 11, 'ОТА': 12, 'Прямой провод': 13,
    'ШПД IPTV': 14, 'MVNO (OTT)': 15}

GLOBAL_STATES = {
    'Заведение заявки': 1,
    "Создание договоров": 2,
    'Отложена (нет тех. возможности)': 3,
    'Назначено тех. обследование': 4,
    'В работе': 5,
    'Заведение заявки': 6,
    'Обработка в СУС': 7,
    'Отложена по просьбе клиента': 8,
    'Назначение тех. данных': 9,
    'Отсутствие ТВП ШПД по запрашиваемой технологии': 10,
    'Закрытие наряда': 11,
    'Не подтверждена': 12,
}


def ret_ind_date(dates):
    ind = 0
    date = dates[0]
    for i in range(len(dates)):
        if not dates[i] is None:
            ind = i
            date = dates[i]
    return ind, date


def checked(num):
    url = f'http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/check/?number={num}'
    response = requests.get(url).json()
    return response


def post_if_yes(num, date, state, current):
    url = 'http://v1738409.hosted-by-vdsina.ru/api/v1/docs/change/make/'
    params = dict()
    params['application'] = int(num)
    params['create_date'] = date
    print(params['create_date'])
    params['current_status'] = current
    params['state'] = GLOBAL_STATES[state]
    # дописать параметр для state
    requests.post(url, json=params)


def post_if_no(num, date, client, service, current_status, state):
    url = 'http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/'
    params = dict()
    params['number'] = int(num)
    params['entry_date'] = date
    params['client'] = client
    params['service'] = GLOBAL_SERVICES[service]
    params['current_status'] = current_status
    params['state'] = GLOBAL_STATES[state]
    requests.post(url, json=params)


def check(INN):
    url = 'http://v1738409.hosted-by-vdsina.ru/api/v1/docs/auth/uploads/company/'
    params = dict()
    try:
        params['itn'] = int(INN)
        response = requests.get(url, params=params).json()
        return response['id']
    except Exception:
        return 'null'


asd = {
    'Дата входа заявки в статус': 1,
    'Дата регистрации под заявки': 2,
    'Рег. наряда на ТВП': 3,
    'Дата отклонения под заявки': 4,
    'Завершение проверки ТВП': 5,
    'Дата отправки на АПТВ': 6,
    'Завершение АТВП': 7,
    'Начало ДО': 8,
    'Завершение ДО': 9,
}

def main_zayavka(cur):
    results = cur.execute("""SELECT * FROM data """).fetchall()
    for i in results:
        _, num_zayavka, client, INN, \
            status, date_enter_in_status, usluga, date_reg_pod_zayav, \
            date_register, date_reg_naryad, \
            date_dicline_pod_zayavka, _, _, \
            finish_tvp, _, _, date_in_avtp, _, data_finish_avtp, _, \
            date_do, _, date_finish_do, _ = i
        dates = [date_enter_in_status, date_reg_pod_zayav, date_register, date_reg_naryad, date_dicline_pod_zayavka,
                 finish_tvp, date_in_avtp, data_finish_avtp, date_do, date_finish_do]
        
        ind, date = ret_ind_date(dates)
        date = str(datetime.datetime.fromisoformat(date))
        if len(checked(num_zayavka)) == 0:
            id_client = check(INN)
            post_if_no(num_zayavka, date, id_client, usluga, ind, status)
        else:
            post_if_yes(num_zayavka, date, status, ind)


if __name__ == "__main__":
    tm = time.time()
    con = sqlite3.connect('/home/nia/Desktop/rtk-stl/for_zip/base.db')
    cur = con.cursor()
    main_zayavka(cur)
