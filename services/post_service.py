from sqlalchemy.ext.asyncio import AsyncSession
from models.post import Post
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

async def create_post(session: AsyncSession, text: str, user_id: int):
    new_post = Post(text=text, owner_id=user_id)
    session.add(new_post)
    await session.commit()
    await session.refresh(new_post)
    return new_post

async def get_user_posts(session: AsyncSession, user_id: int):
    async with session.begin():
        result = await session.execute(select(Post).options(selectinload(Post.owner)).where(Post.owner_id == user_id))
        return result.scalars().all()

async def delete_post(session: AsyncSession, post_id: int, user_id: int):
    async with session.begin():
        result = await session.execute(select(Post).where(Post.id == post_id, Post.owner_id == user_id))
        post = result.scalars().first()
        if post:
            await session.delete(post)
            await session.commit()
            return True
    return False
