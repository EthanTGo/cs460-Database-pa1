from psycopg2 import pool

class Database:
    #static variable
    __connection_pool = None

    @classmethod
    def initialise(cls, **kwargs):
        #**kwargs takes any number of named parameter so here it has user='postgres', password='1234', database='learning',host='localhost', port="5433"
        Database.__connection_pool = pool.SimpleConnectionPool(1, 1, **kwargs)

    # @classmethod
    # def initialise(cls):
    #     cls.connection_pool = pool.SimpleConnectionPool(1, 1, user='postgres', password='1234', database='learning',
    #                                                      host='localhost', port="5433")

    @classmethod
    def getConnection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def returnConnection(cls, connection):
        Database.__connection_pool.putconn(connection)

    @classmethod
    def closeAllConnection(cls):
        Database.__connection_pool.closeall()



# connection_pool = pool.SimpleConnectionPool(1, 1, user='postgres', password='1234', database='learning',
#                                                          host='localhost', port="5433")
class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.getConnection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        #error handling
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.returnConnection(self.connection)

# def connect():
#    return psycopg2.connect(user='postgres', password='1234', database='learning', host='localhost', port="5433")
