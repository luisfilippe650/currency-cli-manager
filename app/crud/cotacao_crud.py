from app.core.database import connect


def add_coin(code):
    database = connect()
    cursor = database.cursor()

    sql = "INSERT INTO currencies(code) VALUES (%s)"
    values = (code.upper(),)

    cursor.execute(sql, values)
    database.commit()

    cursor.close()
    database.close()

    return "currency added successfully"


def list_coins():
    database = connect()
    cursor = database.cursor()

    sql = "SELECT * FROM currencies"

    cursor.execute(sql)
    values = cursor.fetchall()

    cursor.close()
    database.close()

    return values


def delete_coin(id):
    database = connect()
    cursor = database.cursor()

    sql = "DELETE FROM currencies WHERE id = %s"
    values = (id,)

    cursor.execute(sql, values)
    database.commit()

    cursor.close()
    database.close()

    return "currency deleted successfully"


def find_coin(code):
    database = connect()
    cursor = database.cursor()

    sql = "SELECT code FROM currencies WHERE code = %s"
    values = (code.upper(),)

    cursor.execute(sql, values)
    result = cursor.fetchone()

    cursor.close()
    database.close()

    if result is None:
        return None

    return result