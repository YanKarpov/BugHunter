import asyncpg
from config import DATABASE_URL

async def connect_to_db():
    """Подключение к базе данных."""
    return await asyncpg.connect(DATABASE_URL)

async def close_db_connection(conn):
    """Закрытие подключения к базе данных."""
    await conn.close()

async def save_bug_report(category_id: int, description: str):
    """Сохранение отчета о баге в базе данных."""
    conn = await connect_to_db()
    try:
        await conn.execute("""
            INSERT INTO bug_reports (category_id, description)
            VALUES ($1, $2)
        """, category_id, description)
    finally:
        await close_db_connection(conn)

async def get_bug_reports():
    """Получение всех отчетов о баге из базы данных."""
    conn = await connect_to_db()
    try:
        return await conn.fetch("""
            SELECT * FROM bug_reports
        """)
    finally:
        await close_db_connection(conn)

async def delete_bug_report(report_id: int):
    """Удаление отчета о баге по ID."""
    conn = await connect_to_db()
    try:
        await conn.execute("""
            DELETE FROM bug_reports WHERE id = $1
        """, report_id)
    finally:
        await close_db_connection(conn)