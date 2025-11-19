import requests
import random


class APIJoke:

    URL = "https://icanhazdadjoke.com/search"

    def get_random_joke(self, user_input):

        print(f"HTTP status code is: {requests.get(self.URL).status_code}")
        res = requests.get(self.URL,
                          headers={"Accept": "application/json"},
                           params={"term": user_input},
                           ).json()

        num_jokes = res["total_jokes"]
        results = res["results"]
        one_rand_joke = random.choice(results)["joke"]

        if num_jokes > 1:
            print(f"I found {num_jokes} jokes about {user_input} Here is one:")
            print(one_rand_joke)
        elif num_jokes == 1:
            print(f"I just found 1 joke about {user_input}")
            print(one_rand_joke)
        else:
            print(f"sorry couldn't fine any jokes about {user_input}")

        return one_rand_joke
