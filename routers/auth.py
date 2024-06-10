from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from services.auth_service import create_access_token, get_password_hash, authenticate_user
from schemas.user import UserCreate, UserLogin, UserOut
from models.user import User

router = APIRouter()

@router.post("/signup", response_model=UserOut)
async def signup(user_create: UserCreate, db: AsyncSession = Depends(get_db)):
    hashed_password = get_password_hash(user_create.password)
    new_user = User(email=user_create.email, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@router.post("/login")
async def login(user_login: UserLogin, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, user_login.email, user_login.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
