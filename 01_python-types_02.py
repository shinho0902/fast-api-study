# 타입으로서의 클래스

# name 을 가지는 Person 클래스
class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

# 잘못된 방식
try:
    print(get_person_name('hello')) # X
except Exception as e:    # 에러 메시지를 출력할 때는 Exception을 사용
    print('예외 >> ', e) # 'str' object has no attribute 'name'

# Person 객체를 생성하고 함수에 전달
person = Person('hello')
print(get_person_name(person))

print("*"*30)
# Pydantic 모델
# 속성들을 포함한 클래스 형태로 "모양(shape)"을 선언할 수 있습니다

from datetime import datetime
from typing import List, Union

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123


# **FastAPI**는 모두 Pydantic을 기반으로 되어 있습니다 !!! 