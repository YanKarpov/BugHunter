# Установка и запуск проекта

## Требования
- Python 3.11 или выше
- pip (пакетный менеджер Python)

## Шаги для установки

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/YanKarpov/BugHunter.git
   cd BugHunter
   ```

2. **Создайте виртуальную среду:**
   ```bash
   python -m venv venv
   ```

3. **Активируйте виртуальную среду:**
   - На Windows:
     ```bash
     venv\Scripts\activate
     ```
   - На macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Установите зависимости указанные в файле txt:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Настройте базу данных (если необходимо):**
   - Опишите процесс создания и инициализации базы данных.

   #### Для PostgreSQL:
   1. **Создайте новую базу данных:**
      ```bash
      createdb -U <username> <new_database_name>
      ```

   2. **Восстановите базу данных из дампа:**
      ```bash
      psql -U <username> -d <new_database_name> -f path/to/dump.sql
      ```

   #### Для MySQL:
   1. **Создайте новую базу данных:**
      ```bash
      mysql -u <username> -p -e "CREATE DATABASE <new_database_name>;"
      ```

   2. **Восстановите базу данных из дампа:**
      ```bash
      mysql -u <username> -p <new_database_name> < path/to/dump.sql
      ```

   #### Для SQLite:
   - Если вы используете SQLite, просто скопируйте файл базы данных `.db` в нужное место вашего проекта и укажите его в коде. Например, поместите его в папку `/database` вашего проекта и настройте путь к файлу в вашем приложении.


6. **Запустите проект в локальной среде:**
   ```bash
   python -m bot.main
   ```

   P.S Убедитесь, что файл .env правильно настроен с вашим токеном и параметрами подключения к базе данных.
  ```bash
  BOT_TOKEN=
  DEV_BOT_TOKEN=
  ENV=development
  DATABASE_URL=
  ```

7. **Тестирование на внешнем сервере:**
   - Для развертывания и тестирования проекта на внешнем сервере я использовал платформу [Railway](https://railway.app).
   - Для тестирования бота вы можете использовать [@BugHunBot](https://t.me/BugHunBot).
   



