from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql://postgres:Anirudh%402002@localhost:5432/first_project"
engine=create_engine(DB_URL)
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()