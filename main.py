# FastAPI 임포트
from fastapi import FastAPI

# FastAPI "인스턴스" 생성
app = FastAPI()

# get(데이터생성), post(데이터읽기), put(데이터업데이트), delete(데이터삭제)... : operations 
@app.get("/") # decorator 데코레이터 정의
async def root(): # define the path operation function
    return {"message": "Hello World"}

# >> uvicorn main:app 명령으로 서버를 실행

# main: 파일 main.py (파이썬 "모듈").
# app: main.py 내부의 app = FastAPI() 줄에서 생성한 오브젝트.
# --reload: 코드 변경 시 자동으로 서버 재시작. 개발 시에만 사용.


# 대화형 api 문서
#  http://127.0.0.1:8000/docs

# Open API 스키마 구성
# http://127.0.0.1:8000/openapi.json

#######################################################
#################### 경로 매개 변수 ####################
#######################################################
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}



# 사전 정의 값 (Predefined values)

# Enum 클래스 생성
# Enum을 임포트하고 str과 Enum을 상속하는 서브 클래스를 만듭니다.

from enum import Enum

from fastapi import FastAPI

# create class attributes with fixed values, which will be the available valid values
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
# 열거형 클래스 ModelName 를 사용하는 타입 어노테이션으로 경로 매개변수를 만듭니다.
# create a path parameter with a type annotation using the enum class you created (ModelName)
async def get_model(model_name: ModelName): 
    # enumeration member in your created enum ModelName
    if model_name is ModelName.alexnet: 
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    # You can get the actual value
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}



# Starlette의 옵션을 직접 이용하여 다음과 같은 URL을 사용함으로써 *path*를 포함하는 *경로 매개변수*를 선언할 수 있습니다:

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    with open(file_path, 'r') as file:
        content = file.read()
    return {"file_path": file_path , "content": content}


#######################################################
#################### 쿼리 매개 변수 ####################
#######################################################

# 경로 매개변수의 일부가 아닌 다른 함수 매개변수를 선언하면 "쿼리" 매개변수로 자동 해석합니다.

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# 선택적 매개 변수
from typing import Union

@app.get("/items_2/{item_id}")
# 함수 매개변수 q는 선택적이며 기본값으로 None 값이 됩니다
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# 쿼리 매개변수 형변환
@app.get("/items_3/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# 여러 경로/쿼리 매개변수
"""
여러 경로 매개변수와 쿼리 매개변수를 동시에 선언할 수 있으며 
**FastAPI**는 어느 것이 무엇인지 알고 있습니다.
그리고 특정 순서로 선언할 필요가 없습니다.
매개변수들은 이름으로 감지됩니다:
"""

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# 필수 쿼리 매개변수
@app.get("/items_4/{item_id}")
# None 을 지정하지 않으면 기본적으로 required 임
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

# 일부 매개변수는 필수로, 다른 일부는 기본값을, 또 다른 일부는 선택적으로 선언할 수 있습니다
# item_id, needy 필수 // skip 기본값 // limit 선택적
@app.get("/items_5/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item