from bs4 import BeautifulSoup
import asyncio
import time


async def correct_span(cxn, cur):
    tm = time.time()
    results = cur.execute("""SELECT "Номер заявки", "Клиент*" FROM data
    WHERE "Клиент*" like '<%';""").fetchall()
    tasks = []
    for i, j in results:
        tasks.append(delete_span(cur, i, j))
    await asyncio.gather(*tasks)
    cxn.commit()
    print(f"Span: {time.time() - tm}")


async def delete_span(cur, i, j):
    j = BeautifulSoup(j, features="html.parser").text
    cur.execute(f"""UPDATE data
            SET "Клиент*"='{j}'
            WHERE "Номер заявки"={i}""")
