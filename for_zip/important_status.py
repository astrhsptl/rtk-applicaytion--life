
import time


def important_status(con, cur):
    tm = time.time()
    status = ['Удалена', 'Удалена (ошибка ввода)', 'Удалена (Смена ТП)', 'Удалена (абонент уже подключен)', 'Тест',
              'Закрыт', 'Закрыт (не удалось связаться с клиентом)', 'Закрыт (нет тех. возможности)',
              'Закрыт (отказ клиента)']

    for i in status:
        cur.execute(f"""DELETE FROM data
        WHERE "Статус"='{i}'""")
    con.commit()
    print(f"Status: {time.time() - tm}")