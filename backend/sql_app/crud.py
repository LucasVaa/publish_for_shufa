from re import L
from sqlalchemy.orm import Session
from sqlalchemy import select, or_, and_

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_hanzi_item(db: Session):
    # handfiles.sheet5(db)
    # handfiles.sheet1(db)
    return "db_item"


def get_shufa_list(db: Session):
    statement = select(models.Hanzi).where(
        models.Hanzi.id >= 0, models.Hanzi.id < 20)
    result = db.execute(statement).scalars().all()
    return result


def get_shufa_list_by_id(db: Session, id: int, size: int, title: str, creator: str, date: str, type: str):
    if (title == "" and creator == "" and date == "" and type == ""):
        statement = select(models.Hanzi).where(
            models.Hanzi.id >= (id - 1) * size + 1, models.Hanzi.id < (id - 1) * size + size + 1)
        result = db.execute(statement).scalars().all()
    else:
        statement = select(models.Hanzi).where(
            or_(models.Hanzi.title == title, title == ""),
            or_(models.Hanzi.creator == creator, creator == ""),
            or_(models.Hanzi.date == date, date == ""),
            or_(models.Hanzi.type == type, type == ""))
        result = db.execute(statement).scalars().all()[
            (id - 1) * size: (id - 1) * size + size]

    return result


def get_shufa_total(db: Session, title: str, creator: str, date: str, type: str):
    if (title == "" and creator == "" and date == ""):
        result = db.query(models.Hanzi).count()
    else:
        statement = select(models.Hanzi).where(
            or_(models.Hanzi.title == title, title == ""),
            or_(models.Hanzi.creator == creator, creator == ""),
            or_(models.Hanzi.date == date, date == ""),
            or_(models.Hanzi.type == type, type == ""))
        result = len(db.execute(statement).scalars().all())
    return result


def exe_oai_pmh(db: Session, verb: str, offset: int, rows: int):
    if (verb == "ListRecords"):
        id = offset + 1
        size = rows
        statement = select(models.Hanzi).where(
            models.Hanzi.id >= (id - 1) * size + 1, models.Hanzi.id < (id - 1) * size + size + 1)
        result = db.execute(statement).scalars().all()
        return result
    else:
        return {}

def get_shufa_re(db: Session, resType: int, pageNumber: int, pageSize: int):
    statement = select(models.Hanzi).order_by(models.Hanzi.id)
    result = db.execute(statement).scalars().all()[
        (pageNumber - 1) *pageSize: (pageNumber - 1)* pageSize + pageSize]
