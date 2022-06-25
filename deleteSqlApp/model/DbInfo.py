from pydantic import BaseModel

class DbInfo():

    # 在构造器里直接赋值，好像就不要写属性了。省了get和set方法了？
    def __init__(self,host=None,username=None,password=None,database=None,databasetype=None,port=None,note=None,charset="utf8"):
        self.host: str = host
        self.username: str= username
        self.password: str = password
        self.database: str = database
        self.databasetype: str = databasetype
        self.port: str = port
        self.note:str = note
        self.charset:str = charset






