from pydantic import BaseModel
class ExecuteResult():
    def __init__(self,result=None,message=None):
        self.result: str = result
        self.message: str = message
