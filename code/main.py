from fastapi import FastAPI
from typing import List  # ネストされたBodyを定義するために必要
from starlette.middleware.cors import CORSMiddleware  # CORSを回避するために必要
from db import session  # DBと接続するためのセッション
from model import UsersTable, User  # 今回使うモデルをインポート

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
