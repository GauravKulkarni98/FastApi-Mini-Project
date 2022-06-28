from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import cx_Oracle

from sqlalchemy.orm import Session



host='illin659'
port=1521
sid='dmcnv'
user='soumyakp'
password='soumyakp'
sid = cx_Oracle.makedsn(host, port, sid=sid)

cstr = 'oracle://{user}:{password}@{sid}'.format(
    user=user,
    password=password,
    sid=sid
)

engine =  create_engine(
    cstr,
    convert_unicode=False,
    pool_recycle=10,
    pool_size=50,
    echo=True
)


Base = declarative_base()

session = Session(bind=engine, expire_on_commit=False)


