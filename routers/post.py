from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas.post import PostCreate, PostOut
from services.post_service import create_post, get_user_posts, delete_post
from utils.dependencies import get_current_user
from utils.cache import get_cached_posts, set_cached_posts
from models.user import User

router = APIRouter()

@router.post("/addpost", response_model=PostOut)
async def add_post(post_create: PostCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    post = await create_post(db, post_create.text, current_user.id)
    return post

@router.get("/getposts", response_model=List[PostOut])
async def get_posts(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    cached_posts = get_cached_posts(current_user.id)
    if cached_posts:
        return cached_posts
    posts = await get_user_posts(db, current_user.id)
    set_cached_posts(current_user.id, posts)
    return posts

@router.delete("/deletepost")
async def delete_post(post_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    success = await delete_post(db, post_id, current_user.id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found or not authorized to delete",
        )
    return {"detail": "Post deleted successfully"}
