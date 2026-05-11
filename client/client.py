import requests

def get_random_word(api_url):
    response = requests.get(f"{api_url}/words/random")
    response.raise_for_status()
    return response.json()

def show_word(word):
    print("Palavra do dia")
    print(f"Palavra: {word['word']}")
    print(f"Tradução: {word['translation']}")
    print(f"Exemplo: {word['example']}")
    print(f"Nível: {word['level']}")

def main():
    api_url = "http://127.0.0.1:8000"
    word = get_random_word(api_url)
    show_word(word)

if __name__ == "__main__":
    main()