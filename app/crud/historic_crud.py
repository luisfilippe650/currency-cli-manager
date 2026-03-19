from app.core.database import connect


def save_value(base_currency, target_currency, exchange_rate):
    database = connect()
    cursor = database.cursor()

    sql = """
        INSERT INTO exchange_history (base_currency, target_currency, exchange_rate)
        VALUES (%s, %s, %s)
    """

    values = (base_currency, target_currency, exchange_rate)

    cursor.execute(sql, values)
    database.commit()

    cursor.close()
    database.close()

    return "saved in history successfully"


def list_history():
    database = connect()
    cursor = database.cursor()

    sql = "SELECT * FROM exchange_history"

    cursor.execute(sql)
    values = cursor.fetchall()

    cursor.close()
    database.close()

    return values


def delete_history():
    database = connect()
    cursor = database.cursor()

    sql = "DELETE FROM exchange_history"

    cursor.execute(sql)
    database.commit()

    cursor.close()
    database.close()

    return "history deleted successfully"