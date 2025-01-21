from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import email_router, franchise_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


app.include_router(email_router.router, prefix="/email", tags=["email"])
app.include_router(franchise_router.router, prefix="/franchise", tags=["franchise"])
