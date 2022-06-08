import os
import yaml
from deleteSqlApp.model.DbInfo import *
class YmlUtil:

    # path = os.path.abspath()

    @staticmethod
    def readDbYml(filePath):
        f = open(filePath, 'r', encoding='utf-8')
        cont = f.read()
        x = yaml.load(cont,Loader=yaml.FullLoader)
        print(x['DB'])
        print(x['DB']['host'])
        dbInfo=DbInfo(host=x['DB']['host'],
               username=x['DB']['username'],
               password=x['DB']['password'],
               database=x['DB']['database'],
               port=x['DB']['port']
               )
        # 设置类属性——setattr(object,key,value)
        # 类似于建造者模式
        setattr(dbInfo,"note",x['DB']['note'])

        return dbInfo




if __name__ == '__main__':
    db=YmlUtil.readDbYml("KD_SALE_DX.yml")
    print("端口号："+str(db.port))
    print(db.port)



