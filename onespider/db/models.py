"""
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

SQLAlchemy本身无法操作数据库，其必须以来pymsql等第三方插件，Dialect用于和数据API进行交流，根据配置文件的不同调用不同的数据库API，从而实现对数据库的操作.

复制代码
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
  
pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
  
MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
  
cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
  
更多详见：http://docs.sqlalchemy.org/en/latest/dialects/index.html
"""

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time
import uuid

# 创建对象的基类:
Base = declarative_base()
engine = create_engine('mysql+pymysql://root:root@localhost/scrspider?charset=utf8')
DBSession = sessionmaker(bind=engine)

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class MovieList(Base):
    __tablename__ = 'movielist'

    mlid = Column(String(200), primary_key=True)
    name = Column(String(200))
    url = Column(String(200))
    status = Column(String(200))
    tags = Column(String(200))
    tvstation = Column(String(200))
    updatetime = Column(String(200))


class t_zngirls_info(Base):
    __tablename__ = 't_zngirls_info'

    id = Column(String(200), primary_key=True)
    url = Column(String(200))
    photourl = Column(String(200))
    ms = Column(String(2000))
    name = Column(String(200))
    bname = Column(String(200))
    blood = Column(String(200))
    height = Column(String(200))
    weight = Column(String(200))
    bwh = Column(String(200))
    birthday = Column(String(200))
    age = Column(String(200))
    xz = Column(String(200))
    birthaddr = Column(String(200))
    job = Column(String(200))
    hobby = Column(String(200))

if __name__ == "__main__":
    session = DBSession()
    newmovie = MovieList(mlid=next_id(),
                         name="1",
                         url="1",
                         status="1",
                         tags="1",
                         tvstation="1",
                         updatetime="1"
                         )
    session.add(newmovie)
    session.commit()
    session.close()