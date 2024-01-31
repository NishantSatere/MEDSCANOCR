from pydantic import BaseModel
from datetime import date

class patient(BaseModel):
    name:str
    age:int
    gender:str
    collecte_date:date
    bg: str
    rbc: int
    hb: int




