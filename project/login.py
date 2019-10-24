from user import User
from database import Database




# database_one = Database()
# database_two = Database()
# print(database_one.connection_pool)
# database_one.initialise()
# print(database_two.connection_pool)

#
# print(Database.connection_pool)
#
# Database.initialise()
#
# print(Database.connection_pool)

Database.initialise(user='postgres', password='1234', database='learning',
                                                               host='localhost', port="5433")

my_user = User.load_from_db_by_email('ethango1997@bu.edu')
print(my_user)
