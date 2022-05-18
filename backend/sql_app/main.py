from tokenize import String
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


from . import crud, models, schemas
from .database import SessionLocal, engine

import os.path

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.post("/script/hanzi")
def create_hanzi_items(db: Session = Depends(get_db)):
    items = crud.create_hanzi_item(db)
    return items


@app.get("/getImage/{fileName}")
def get_image(db: Session = Depends(get_db), fileName: str = ""):
    for i in range(1, 9):
        path = "/home/lucas/Documents/shufa/CD-" + \
            str(i) + "/HanziDatabase2014/Hanzi_Image/" + fileName
        if (os.path.isfile(path)):
            return FileResponse(path)
    print(fileName)
    print("++++")
    return FileResponse("/home/lucas/Documents/shufa/CD-1/HanziDatabase2014/Hanzi_Image/000001.a.jinxiandai.zhuanshu.qibaishi.yinzhangwenzi.10.jpg")


@app.get("/getShufaList")
def get_shufa_list(db: Session = Depends(get_db)):
    items = crud.get_shufa_list(db)
    return items


@app.get("/getShufaListById")
def get_shufa_list_by_id(db: Session = Depends(get_db),
                         id: int = 0, size: int = 10,
                         title: str = "", creator: str = "",
                         date: str = "", type: str = ""):
    items = crud.get_shufa_list_by_id(
        db=db, id=id, size=size, title=title, creator=creator, date=date, type=type)
    return items


@app.get("/getShufaTotal")
def get_shufa_total(db: Session = Depends(get_db),
                    title: str = "", creator: str = "",
                    date: str = "", type: str = ""):
    item = crud.get_shufa_total(
        db, title=title, creator=creator, date=date, type=type)
    return item


@app.get("/x")
def exe_oai_pmh(db: Session = Depends(get_db), verb: str = "", offset: int = 0, rows: int = 10):
    items = crud.exe_oai_pmh(db=db, verb=verb, offset=offset, rows=rows)
    return items
