import pathlib

class FileManagerJoke:

    FILE = "random_joke.txt"

    def save_joke_to_file(self, joke_file):
        f_exists = pathlib.Path(self.FILE)
        if f_exists.exists():
            with open(self.FILE, "r") as f:
                lines = f.readlines()
            number = len(lines) +1

            with open(self.FILE, "a") as file_joke:
                file_joke.write(f"{number}. {joke_file} \n")
        else:
            pathlib.Path(self.FILE).touch()

            with open(self.FILE, "r") as f:
                lines = f.readlines()
            number = len(lines) + 1

            with open(self.FILE, "a") as file_joke:
                file_joke.write(f"{number}. {joke_file} \n")
