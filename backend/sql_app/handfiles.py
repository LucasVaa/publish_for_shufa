import openpyxl
import os
from sqlalchemy.orm import Session

from . import models, schemas


def sheet5(db):
    wb = openpyxl.load_workbook(os.getcwd() + '/sql_app/hz.xlsx')
    sh = wb['Sheet5']
    for cases in list(sh.rows)[1:]:
        characterId = "AT2601" + cases[5].value[:6]
        fileName = cases[5].value
        date = cases[1].value[3:] if cases[1].value != None else ""
        type = cases[2].value
        creator = cases[3].value
        source = cases[4].value
        db_item = models.Hanzi(**{
            "characterId": characterId,
            "fileName": fileName,
            "date": date,
            "type": type,
            "creator": creator,
            "source": source,
        })
        db.add(db_item)
    db.commit()
    wb.close()


def sheet1(db):
    wb = openpyxl.load_workbook(os.getcwd() + '/sql_app/hz.xlsx')
    sh = wb['Sheet2']
    for cases in list(sh.rows)[1:]:
        characterId = "AT2601" + str(cases[0].value).zfill(6)
        pinyin = cases[1].value
        tone = cases[2].value
        title = cases[3].value
        db.query(models.Hanzi).filter(
            models.Hanzi.characterId == characterId).update({"pinyin": pinyin, "tone": tone, "title": title})
    db.commit()
    wb.close()
