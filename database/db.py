import asyncpg
from config import DATABASE_URL

async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

async def close_db_connection(conn):
    await conn.close()

async def save_bug_report(category_id: int, description: str):
    conn = await connect_to_db()
    await conn.execute("""
        INSERT INTO bug_reports (category_id, description)
        VALUES ($1, $2)
    """, category_id, description)
    await close_db_connection(conn)
