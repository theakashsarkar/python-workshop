# # from dataclasses import dataclass

# # @dataclass
# # class C:
# #     i: int
# #     j: int  = None
# #     database: InitVar[DatabaseType] = None

# #     def __post__init__(self, database):
# #         if self.j is None and database is not None:
# #             self.j = database.lookup('j')
# # c = C(10, database=my_database)
# # print(c.i, c.j)

from dataclasses import dataclass, InitVar, field
from typing import Optional, Dict

class Database:
    def __init__(self):
        self._data = {
            'user_1' : {'j': 20, 'name': 'Alice'},
            'user_2' : {'j': 21, 'name': 'Bob'}
        }

    def lookup(self, field: str, user_id: str) -> any:
        return self._data.get(user_id, {}).get(field)
@dataclass
class UserProfile:
    i: int
    j: Optional[int] = None
    name: Optional[str] = None
    database: InitVar[Database] = None
    user_id: InitVar[str] = None
    metadata: Dict[str, any] = field(default_factory=dict)
    def __post_init__(self, database: Database, user_id: str):
        if database is not None and user_id is not None:
            if self.j is None:
                self.j = database.lookup('j', user_id)
            if self.name is None:
                self.name = database.lookup('name', user_id)
            self.metadata['last_lookup'] = 'database'
            self.metadata['user_id'] = user_id

def demonstrate():
    my_database = Database()

    user1 = UserProfile(1, database=my_database, user_id='user_1')
    user2 = UserProfile(2, j = 25, database=my_database, user_id='user_2')

    print(f"User 1 metadata: {user1.metadata}")
    print(f"User 2: i={user2.i}, j={user2.j}, name={user2.name}")
    print(f"User 2 metadata: {user2.metadata}")

if __name__ == '__main__':
    demonstrate()

# from dataclasses import dataclass, InitVar, field

# @dataclass
# class MyClass:
#     init_only: InitVar[int]
#     x: int = field(init=False)

#     def __post_init__(self, init_only):
#         self.x = init_only * 2
# my = MyClass(10)
# print(my.x)