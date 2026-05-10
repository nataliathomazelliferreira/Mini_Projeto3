import requests

def get_words(api_url):
    response = requests.get(f"{api_url}/words")
    response.raise_for_status()
    return response.json()

def show_words(words):
    for word in words:
        print(f"ID: {word['id']}")
        print(f"Palavra: {word['word']}")
        print(f"Tradução: {word['translation']}")
        print(f"Exemplo: {word['example']}")
        print(f"Nível: {word['level']}")
        print("-" * 30)

def main():
    api_url = "http://127.0.0.1:8000"
    words = get_words(api_url)
    show_words(words)

if __name__ == "__main__":
    main()