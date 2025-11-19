from joke_api import APIJoke
from file_manager import FileManagerJoke
from database import DatabaseJoke
from app import AppJoke

def main():
    api = APIJoke()
    file_manager = FileManagerJoke()
    db = DatabaseJoke()

    db.init_db()
    app = AppJoke(api, file_manager, db)
    app.run()




if __name__ == '__main__':
    main()