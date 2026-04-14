from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://terrarun_user:5NUing8mHoPZrMozMz8AoDpiL6yu8CsW@dpg-d7f8t54vikkc739mib1g-a/terrarun"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
