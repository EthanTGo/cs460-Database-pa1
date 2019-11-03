from database import CursorFromConnectionFromPool

class Request:
    def __init__(self, query):
        # init allows parameters of object definition
        self.query = query

    def __repr__(self):
        # the .format method will replace {} in the String, the python toString() method
        return "<Query information {}>".format(self.query)

    def add_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute(self.query)

    def retrieve_from_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute(self.query)
            data = cursor.fetchone()
            return data