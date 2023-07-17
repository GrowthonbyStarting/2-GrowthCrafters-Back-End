from databases import Database
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
import uuid

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3306",
    "http://ptgod.s3-website.ap-northeast-2.amazonaws.com",
  # Update with your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base = declarative_base()


class MyData(Base):
    __tablename__ = 'mydata'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(1000))
    phone = Column(String(1000))
    email = Column(String(1000))
    category = Column(String(1000))
    q1 = Column(String(1000))
    q2 = Column(String(1000))
    q3 = Column(String(1000))
    q4 = Column(String(1000))
    q5 = Column(String(1000))
    attachment = Column(String(100))


# 데이터베이스 연결 설정
DATABASE_URL = "sqlite:///data.db"
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@app.on_event("startup")
async def startup():
    await database.connect()
    Base.metadata.create_all(bind=engine)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/data")
async def create_data(name: str, phone: str, email: str, category: str,
                      q1: str, q2: str, q3: str = '', q4: str = '', q5: str = '',
                      attachment: UploadFile = File(None)):
    # 파일 업로드 처리
    file_path = None
    if attachment is not None:
        file_extension = os.path.splitext(attachment.filename)[1]  # 파일 확장자 추출
        random_filename = f"{uuid.uuid4().hex}{file_extension}"  # 무작위 파일 이름 생성

        file_path = os.path.join("uploads", random_filename)
        with open(file_path, "wb") as f:
            contents = await attachment.read()
            f.write(contents)

    async with database.transaction():
        session = SessionLocal()
        new_data = MyData(name=name, phone=phone, email=email,
                          category=category, q1=q1, q2=q2, q3=q3, q4=q4,
                          q5=q5, attachment=file_path)
        session.add(new_data)
        session.commit()
        session.refresh(new_data)

    return {"message": "Data created successfully"}
