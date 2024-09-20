from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://sit722_part3_xv6z_user:KZVLkWksW07sQoYJ2xZaHIm1k4XauoYL@dpg-crmhlna3esus73ftd3gg-a.oregon-postgres.render.com/sit722_part3_xv6z" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
