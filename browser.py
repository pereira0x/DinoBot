import webbrowser

url = 'https://offline-dino-game.firebaseapp.com/'
chrome_path = '/usr/bin/google-chrome %s'

def start_game():
    webbrowser.get(chrome_path).open(url)
    print('Game started')
    return

if __name__ == '__main__':
    start_game()
