from .. import models, schema, utils
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database import engine, get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/{id}", response_model=schema.User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).where(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} does not exist.")
    
    return user

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    user.password = utils.hash(user.password)

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user