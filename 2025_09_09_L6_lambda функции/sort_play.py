def load_playlist ():
    playlist = []
    try:
        with open ("3. playlist.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(" - ")
                if len(parts) >= 3:
                    song = {
                        "artist": parts[0],
                        "name": parts[1],
                        "duration": parts[2]
                    }
                    playlist.append(song)
        return playlist
    except FileNotFoundError:
        return []

# Перевод в секунды
def duration_to_seconds(duration):
    try:
        for el in duration: #el - строка
            # списковое включение
            els = [int(x) for x in el.split(":")] # els - список
            minutes, second = els
            # можно тоже самое сделать через функцию map: map(int,
        return minutes * 60 + second
    except:
        return 0


def sort_by_duration(playlist):
    return sorted(playlist, key=lambda x: duration_to_seconds(x["duration"]))

def save_sorted_playlist(filename):
    playlist = load_playlist()
    sorted_playlist = sort_by_duration(playlist)
    with open(filename, "w", encoding="utf-8") as file:
        for song in sorted_playlist:
            file.write(f"{song['artist']} - {song['name']} - {song['duration']}\n")

def search_by_artist(artist_name):
    playlist = load_playlist()
    result = []

    for song in playlist:
        # if song['artist'].lower() == artist_name.lower():
        if artist_name.lower() in song["artist"].lower():
            result.append(song)
    return result

def test():
    playlist = load_playlist()
    print(playlist)
    sort_playlist = sort_by_duration(playlist)
    print(sort_playlist)
    save_sorted_playlist("sort_playlist.txt")
    art = input("Введите имя исполнителя: ")
    print(search_by_artist(art))

if __name__ == "__main__":
    test()
