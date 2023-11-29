import requests

def fetch_random_chuck_norris_joke():
    api_url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(api_url)
        data = response.json()
        joke_text = data['value']
        print("Chuck Norris Joke:")
        print(joke_text)
    except requests.RequestException as e:
        print(f"Error fetching Chuck Norris joke: {e}")

if _name_ == "_main_":
    fetch_random_chuck_norris_joke()