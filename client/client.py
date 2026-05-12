import requests

def get_all_words(api_url):
    response = requests.get(f"{api_url}/words")
    response.raise_for_status()
    return response.json()

def get_random_word(api_url):
    response = requests.get(f"{api_url}/words/random")
    response.raise_for_status()
    return response.json()

def show_word(word):
    print(f"Palavra: {word['word']}")
    print(f"Tradução: {word['translation']}")
    print(f"Exemplo: {word['example']}")
    print(f"Nível: {word['level']}")
    print("-" * 30)

def show_menu():
    print("Word of the Day Client")
    print("1 - Ver palavra do dia")
    print("2 - Listar todas as palavras")
    print("0 - Sair")

def main():
    api_url = "http://127.0.0.1:8000"

    while True:
        show_menu()
        option = input("Escolha uma opção: ")

        if option == "1":
            word = get_random_word(api_url)
            show_word(word)
        elif option == "2":
            words = get_all_words(api_url)
            for word in words:
                show_word(word)
        elif option == "0":
            print("Encerrando cliente.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()