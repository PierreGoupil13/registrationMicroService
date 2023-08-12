import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
db = True


def test_connection():
    try:
        print("Connecting to database...")
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        print("Connected to database")

        result = db.execute("SELECT version()").scalar()
        print(result)

    except Exception as e:
        print(e)


def close_connection(db):
    db.close()
    print("Connection closed")


if __name__ == "__main__":
    test_connection()
