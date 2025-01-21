from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import EmailRecord, FranchiseRequest
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from sqlalchemy.future import select


async def get_emails_to_db(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(EmailRecord).offset(skip).limit(limit)
    )
    return result.scalars().all()  


async def add_email_to_db(db: AsyncSession, email: str):
    db_email = EmailRecord(email=email, date=datetime.now())
    db.add(db_email)
    await db.commit()  
    await db.refresh(db_email) 
    return db_email


async def delete_email_from_db(db: AsyncSession, email_id: UUID):
    db_email = await db.get(EmailRecord, email_id)
    if db_email is None:
        raise HTTPException(status_code=404, detail="Email not found")
    await db.delete(db_email)
    await db.commit()
    return db_email




async def update_email_in_db(db: AsyncSession, email_id: UUID, new_email: str):
    db_email = await db.get(EmailRecord, email_id)
    if db_email is None:
        raise HTTPException(status_code=404, detail="Email not found")
    db_email.email = new_email
    db_email.date = datetime.now()  
    await db.commit()
    await db.refresh(db_email)
    return db_email








async def add_franchise_request_to_db(db: AsyncSession, full_name: str, phone: str, email: str,
                                       ownership_type: str, planned_investments: str,
                                       premises_type: str, franchise_source: str):
    """
    Функция для добавления новой заявки на франшизу в базу данных.
    """
    new_request = FranchiseRequest(
        full_name=full_name,
        phone=phone,
        email=email,
        ownership_type=ownership_type,
        planned_investments=planned_investments,
        premises_type=premises_type,
        franchise_source=franchise_source,
        date_submitted=datetime.utcnow()
    )
    
    db.add(new_request)
    await db.commit()  # Сохраняем изменения в базе данных
    await db.refresh(new_request)  # Обновляем объект после сохранения, чтобы получить его ID
    return new_request



async def create_franchise_request(db: AsyncSession, full_name: str, phone: str, email: str,
                                   ownership_type: str, planned_investments: str, 
                                   premises_type: str, franchise_source: str):
    """
    Функция для добавления новой заявки в базу данных.
    """
    new_request = FranchiseRequest(
        full_name=full_name,
        phone=phone,
        email=email,
        ownership_type=ownership_type,
        planned_investments=planned_investments,
        premises_type=premises_type,
        franchise_source=franchise_source,
        date_submitted=datetime.utcnow()
    )
    
    db.add(new_request)
    await db.commit()  # Сохраняем изменения в базе данных
    await db.refresh(new_request)  # Обновляем объект после сохранения, чтобы получить его ID
    return new_request



async def get_franchise_requests(db: AsyncSession, skip: int = 0, limit: int = 10):
    """
    Функция для получения списка заявок с пагинацией.
    """
    result = await db.execute(
        select(FranchiseRequest).offset(skip).limit(limit)
    )
    return result.scalars().all()



async def get_franchise_request_by_id(db: AsyncSession, request_id: UUID):
    """
    Функция для получения заявки по ID.
    """
    db_request = await db.get(FranchiseRequest, request_id)
    if db_request is None:
        raise HTTPException(status_code=404, detail="Заявка не найдена")
    return db_request


async def update_email_in_db(db: AsyncSession, email_id: UUID, new_email: str):
    db_email = await db.get(EmailRecord, email_id)
    if db_email is None:
        raise HTTPException(status_code=404, detail="Email not found")
    db_email.email = new_email
    db_email.date = datetime.now()  
    await db.commit()
    await db.refresh(db_email)
    return db_email

import logging

# Функция обновления данных заявки
async def update_franchise_request(db: AsyncSession, request_id: UUID, full_name: str = None, 
                                   phone: str = None, email: str = None, ownership_type: str = None, 
                                   planned_investments: str = None, premises_type: str = None, 
                                   franchise_source: str = None):
    """
    Функция для обновления данных заявки.
    """
    db_franchise = await db.get(FranchiseRequest, request_id)
    if db_franchise is None:
        logging.error(f"Request with id {request_id} not found.")
        raise HTTPException(status_code=404, detail="Заявка не найдена")
    
    logging.info(f"Original record: {db_franchise}")

    # Обновляем поля, если значения не None
    if full_name is not None:
        db_franchise.full_name = full_name
    if phone is not None:
        db_franchise.phone = phone
    if email is not None:
        db_franchise.email = email
    if ownership_type is not None:
        db_franchise.ownership_type = ownership_type
    if planned_investments is not None:
        db_franchise.planned_investments = planned_investments
    if premises_type is not None:
        db_franchise.premises_type = premises_type
    if franchise_source is not None:
        db_franchise.franchise_source = franchise_source

    logging.info(f"Updated record: {db_franchise}")

    # Используем асинхронный контекстный менеджер для работы с сессией
    try:
        async with db.begin():  # Начинаем транзакцию
            # Весь код внутри этого блока будет автоматически зафиксирован при выходе
            await db.flush()  # Если нужно, для немедленного сохранения изменений в базе
            logging.info("Changes committed successfully.")
    except Exception as e:
        logging.error(f"Error during commit: {e}")
        raise HTTPException(status_code=500, detail="Ошибка при обновлении базы данных")

    # Попробуем обновить объект после коммита
    try:
        await db.refresh(db_franchise)
        logging.info(f"Record after refresh: {db_franchise}")
    except Exception as e:
        logging.error(f"Error during refresh: {e}")
        raise HTTPException(status_code=500, detail="Ошибка при обновлении данных в базе")
    
    return db_franchise




async def delete_franchise_request(db: AsyncSession, request_id: UUID):
    """
    Функция для удаления заявки по ID.
    """
    db_request = await db.get(FranchiseRequest, request_id)
    if db_request is None:
        raise HTTPException(status_code=404, detail="Заявка не найдена")
    await db.delete(db_request)
    await db.commit()
    return db_request