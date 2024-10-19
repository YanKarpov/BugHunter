import asyncpg
from config import DATABASE_URL

async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

async def close_db_connection(conn):
    await conn.close()
