from tokenize import String
from typing import List

from fastapi import Depends, FastAPI, HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


from . import crud, models, schemas
from .database import SessionLocal, engine

import os
import os.path

from PIL import Image
import requests
import json

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
        path = "/root/shufa/CD-" + \
            str(i) + "/HanziDatabase2014/Hanzi_Image/" + fileName
        if (os.path.isfile(path)):
            return FileResponse(path)
    print(fileName)
    print("++++")
    return FileResponse("/root/shufa/CD-1/HanziDatabase2014/Hanzi_Image/000001.a.jinxiandai.zhuanshu.qibaishi.yinzhangwenzi.10.jpg")


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


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@app.post('/getResource')
def get_resource(item: schemas.getResource, db: Session = Depends(get_db)):
    try:
        if (item.resType == 3):
            data = {
                "resType": item.resType,
                "pageNumber": item.pageNumber,
                "pageSize": item.pageSize
            }
            url = "http://172.20.112.138:8000/getMusic"
            f = requests.post(url, data=json.dumps(data))
            result = f.json()
            return result
        elif (item.resType == 1):
            result = crud.get_shufa_re(db=db, pageNumber=item.pageNumber,
                                resType=item.resType, pageSize=item.pageSize)
            data = []
            for i in result:
                w = 100
                h = 100
                s = 100
                for inum in range(1, 9):
                    path = "/root/shufa/CD-" + str(inum) + "/HanziDatabase2014/Hanzi_Image/" + i.fileName
                    if (os.path.isfile(path)):
                        img = Image.open(path)
                        w = img.width
                        h = img.height
                        s = os.path.getsize(path)
                data.append({
                    "id": i.id,
                    "name": i.title,
                    "type": 1,
                    "publishingHouse": "开明文教音像出版社",
                    "author": i.creator,
                    "createDate": "",
                    "dynasty": i.date,
                    "categoryName": i.type,
                    "label": "",
                    "materialDescribe": "",
                    "coverImage": "",
                    "materialPath": "http://172.20.112.124:8000/getImage/" + i.fileName,
                    "audioTime": "",
                    "format": "jpg",
                    "size": s,
                    "height": h,
                    "width": w
                })
            return {"returnCode": 1, "returnMsg": "API调用成功!", "returnData": data}
        else:
            return{"returnCode": 1, "returnMsg": "API调用成功!", "returnData": []}
    except Exception as e:
        print(e)
        return {"returnCode": 0, "returnMsg": "API调用失败!!", "returnData": []}
