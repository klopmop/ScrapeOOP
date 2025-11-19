
class AppJoke:
    def __init__(self, api, file_manager, database):
        self.api = api
        self.file_manager = file_manager
        self.database = database

    def run(self):
        user_input = input("What would you like to search for: ")
        joke = self.api.get_random_joke(user_input)

        if joke is None:
            return "no joke found"
        else:
            print(f"Here is your joke: {joke}")

        self.file_manager.save_joke_to_file(joke)
        self.database.save_to_db(joke)

        print("Joke saved to file and database")
        return "Joke saved to file and database"
