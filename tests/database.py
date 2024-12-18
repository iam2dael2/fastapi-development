from fastapi.testclient import TestClient
from app import schema
from app.main import app
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db, Base
import pytest
from alembic import command

# SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Blanksora132.@localhost:5432/fastapi_test"

# Establish a connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def session():
    # run our code after our test finishes
    Base.metadata.drop_all(bind=engine)
    # command.downgrade("base")
    
    # Run our code before we return our test
    Base.metadata.create_all(bind=engine)
    # command.upgrade("head")

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)