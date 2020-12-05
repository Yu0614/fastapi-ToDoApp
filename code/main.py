from fastapi import FastAPI
from typing import List, Optional
from starlette.middleware.cors import CORSMiddleware  # CORSを回避するために必要
from db import session
from model import UsersTable, User, TodosTable, Todo, AddNewTodoResponse
from datetime import datetime
import json

import logging
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

# CORSを回避するために設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------APIの実装------------

# ---------- usersの実装 ------------
# テーブルにいる全ユーザ情報を取得 GET


@app.get("/users")
def read_users():
    users = session.query(UsersTable).all()
    return users

# idにマッチするユーザ情報を取得 GET


@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = session.query(UsersTable).\
        filter(UsersTable.id == user_id).first()
    return user

# ユーザ情報を登録 POST


@app.post("/user")
# クエリでnameとstrを受け取る
# /user?name="三郎"&age=10
async def create_user(name: str, age: int):
    user = UsersTable()
    user.name = name
    user.age = age
    session.add(user)
    session.commit()

# 複数のユーザ情報を更新 PUT


@app.put("/users")
# modelで定義したUserモデルのリクエストbodyをリストに入れた形で受け取る
# users=[{"id": 1, "name": "一郎", "age": 16},{"id": 2, "name": "二郎", "age": 20}]
async def update_users(users: List[User]):
    for new_user in users:
        user = session.query(UsersTable).\
            filter(UsersTable.id == new_user.id).first()
        user.name = new_user.name
        user.age = new_user.age
        session.commit()


# ---------- todosの実装 ------------


# 全todo情報を取得 : GET


@app.get("/todos")
def read_todos():
    todos = session.query(TodosTable).all()
    return todos

# idにマッチするtodos情報を取得 GET


@app.get("/todo/{id}")
def read_todo(id: int):
    todo = session.query(TodosTable).\
        filter(TodosTable.id == id).first()
    return todo

# 新しい todo を追加: POST
#  L required : user_id, title
#  L optional : place, url, memo, start_date, end_date
#  L 成功した際のレスポンスとして、投稿ユーザの最新のtodoを返します。


@app.post("/todos", status_code=201, response_model=AddNewTodoResponse)
async def create_todo(user_id: int, title: str, place: Optional[str] = None, url: Optional[str] = None, memo: Optional[str] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
    todo = TodosTable()
    todo.user_id = user_id
    todo.title = title

    if place:
        todo.place = place

    if url:
        todo.url = url

    if memo:
        todo.memo = memo

    if start_date:
        todo.start_date = start_date

    if end_date:
        todo.end_date = end_date

    try:
        session.add(todo)
        session.commit()
    except:
        session.rollback()
        raise

    # 作成したtodoのidを返してあげる
    latest = session.query(TodosTable).\
        filter(TodosTable.user_id == user_id).first()

    return {
        'id': latest.id
    }
