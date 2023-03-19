import sqlite3
from important_status import important_status
import pandas as pd
import asyncio
from correct_span import correct_span
from update_check_company import main_company
from update_zayavka import main_zayavka


def main(*file_names):
    for file_name in file_names:
        ex = pd.read_excel('/home/nia/Desktop/rtk-stl/for_zip/content/' + file_name, dtype=str, usecols=usecols)
        ex.to_sql(name='data', con=con, if_exists='replace', dtype='TEXT', index=False)
    con.commit()
    important_status(con, cur)
    asyncio.run(correct_span(con, cur))
    main_company(cur)
    main_zayavka(cur)


if __name__ == '__main__':
    con = sqlite3.connect('/home/nia/Desktop/rtk-stl/for_zip/base.db')
    cur = con.cursor()
    usecols = ['УЭС (АРМ)', 'Номер заявки', 'Клиент*', 'ИНН', 'Статус', 'Дата входа заявки в статус',
               'Услуга', 'Дата регистрации заявки', 'Дата регистрации под заявки', 'Рег. наряда на ТВП',
               'Дата отклонения под заявки', 'Тип проверки ТВП', 'Наличие ТВП', 'Завершение проверки ТВП',
               'Длит. проверки ТВП', '№ клиентский СУС', 'Дата отправки на АПТВ', 'Дата окончания АПТВ планируемая',
               'Дата окончания АПТВ фактическая', 'Длительность этапа АПТВ', 'Дата отправки на ДО',
               'Дата окончания ДО планируемая', 'Дата окончания ДО фактическая', 'Длительность этапа ДО']
    names = ['Аудит заявок РФ_09.03.23.xlsx']
    main(*names)
