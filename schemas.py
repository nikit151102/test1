from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class EmailRecordBase(BaseModel):
    email: str

class EmailRecordCreate(EmailRecordBase):
    pass

class EmailRecord(EmailRecordBase):
    id: UUID
    date: datetime

    class Config:
        orm_mode = True
        
class EmailRecordOut(BaseModel):
    id: UUID
    email: str
    date: datetime

    class Config:
        orm_mode = True 

class FranchiseRequestBase(BaseModel):
    full_name: str
    phone: str
    email: str
    ownership_type: str
    planned_investments: str
    premises_type: str
    franchise_source: str
    date_submitted: datetime

class FranchiseRequestCreate(FranchiseRequestBase):
    pass

class FranchiseRequestUpdate(FranchiseRequestBase):
    pass

class FranchiseRequestInDB(FranchiseRequestBase):
    id: UUID

    class Config:
        orm_mode = True

