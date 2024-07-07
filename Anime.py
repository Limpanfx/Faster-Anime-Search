import webbrowser

def search_anime(keyword):
    url = f"https://aniwave.to/filter?keyword={keyword}"
    webbrowser.open(url, new=2, autoraise=False)

if __name__ == "__main__":
    user_input = input("What anime do you want to watch?: ")
    search_anime(user_input)