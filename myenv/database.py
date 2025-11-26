from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# NOTE: Replace @ in password with %40
DB_URL = "postgresql://postgres:Varshith%40999@localhost:5432/varshith"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

