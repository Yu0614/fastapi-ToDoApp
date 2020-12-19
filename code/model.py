# -*- coding: utf-8 -*-
# モデルの定義
from sqlalchemy import Column, Integer, String, DateTime
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from db import Base
from db import ENGINE

#
# Users Model


class UsersTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)
# Users Request Body


class User(BaseModel):
    id: int
    name: str
    age: int


# Todos Model


class TodosTable(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    place = Column(String(255), nullable=True)
    url = Column(String(255), nullable=True)
    memo = Column(String(255), nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)

# Todos Request Body


class Todo(BaseModel):
    id: Optional[int]
    user_id: int
    title: str
    place: Optional[str]
    url: Optional[str]
    memo: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    
    
# add new Todos Response Body for post


class AddNewTodoResponse(BaseModel):
    id: int

# main function


def main():
    # テーブルが存在しなければ、テーブルを作成
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
