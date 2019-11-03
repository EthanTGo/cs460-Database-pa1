from database import CursorFromConnectionFromPool


def retrieve_info(to_retrieve):
    with CursorFromConnectionFromPool() as cursor:
        cursor.execute(to_retrieve)
        user_data = cursor.fetchall()
        return user_data

def add_query(to_add):
    with CursorFromConnectionFromPool() as cursor:
        cursor.execute(to_add)