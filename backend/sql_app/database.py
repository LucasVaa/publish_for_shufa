from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:123456@localhost:5432/shufa"

# echo=True表示引擎将用repr()函数记录所有语句及其参数列表到日志
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, encoding='utf8', echo=False, poolclass=NullPool
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
