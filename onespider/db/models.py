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
"""

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time
import uuid

# 创建对象的基类:
Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:root@localhost/scrspider?charset=utf8')
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