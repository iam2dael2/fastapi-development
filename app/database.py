from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# Establish a connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         connection = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="Blanksora132.", cursor_factory=RealDictCursor)
#         cursor = connection.cursor()
#         print("Database connection was succesful!")

#     except Exception as error:
#         print("Connecting to database failed.")
#         print(f"Error: {error}")
#         time.sleep(2)

#     else:
#         break