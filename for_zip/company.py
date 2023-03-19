import sqlite3
import time


def main():
    result = cur.execute("""SELECT DISTINCT "Клиент*", "ИНН" FROM data
    WHERE "Клиент*" NOT IN (SELECT name FROM company)""").fetchall()
    print(len(result))
    for name, INN in result:
        cur.execute(
            f"""INSERT INTO company(name, INN, client_SYS) VALUES ('{name.replace("'", '"')}', '{INN}', 'a')""")
    con.commit()


if __name__ == '__main__':
    tm = time.time()
    con = sqlite3.connect("/home/nia/Desktop/rtk-stl/for_zip/base.db")
    cur = con.cursor()
    try:
        cur.execute("""CREATE TABLE company (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT,
    INN        TEXT,
    client_SYS TEXT
);""")
        con.commit()
    except Exception:
        pass
    main()
    print(time.time() - tm)
