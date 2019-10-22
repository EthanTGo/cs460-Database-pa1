from database import CursorFromConnectionFromPool


class User:
    def __init__(self, email, first_name, last_name, id):
        # init allows parameters of object definition
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        # the .format method will replace {} in the String, the python toString() method
        return "<User {}>".format(self.email)

    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('insert into users (email, first_name, last_name) values (%s, %s, %s)',
                           (self.email, self.first_name, self.last_name))

    @classmethod  # cls is currently bound class and self is currently bound object
    def load_from_db_by_email(cls, email):  # since we want to return a new object
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('select * from users where email=%s', (email,))
            user_data = cursor.fetchone()
            return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])
