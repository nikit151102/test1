from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

Base = declarative_base()

class EmailRecord(Base):
    __tablename__ = 'emails'

    id = Column(UUID, primary_key=True, default=uuid.uuid4)  
    email = Column(String, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.utcnow) 
    
class FranchiseRequest(Base):
    __tablename__ = 'franchise_requests'

    id = Column(UUID, primary_key=True, default=uuid.uuid4)  # Уникальный идентификатор заявки
    full_name = Column(String, nullable=False)  # ФИО
    phone = Column(String, nullable=False)  # Телефон
    email = Column(String, nullable=False)  # Электронная почта
    ownership_type = Column(String, nullable=False)  # Форма собственности
    planned_investments = Column(String, nullable=False)  # Планируемые инвестиции
    premises_type = Column(String, nullable=False)  # Помещение (своё или арендованное)
    franchise_source = Column(String, nullable=False)  # Источник информации о франшизе
    date_submitted = Column(DateTime, nullable=False, default=datetime.utcnow)  # Дата отправки заявки

