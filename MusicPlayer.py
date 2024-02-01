import os
from playsound import playsound
musicfolder=input("Enter your music folder path: ")
class MusicPlayer:
    def __init__(self):
        self.music_folder = musicfolder
        self.playlists = {}

    def list_songs(self):
        songs = [song for song in os.listdir(self.music_folder) if song.endswith(".mp3")]
        if songs:
            print("Available songs:")
            for index, song in enumerate(songs, start=1):
                print(f"{index}. {song}")
        else:
            print("No songs found in the music folder.")

    def play_song(self, song_name):
        song_path = os.path.join(self.music_folder, song_name)
        if os.path.exists(song_path):
            playsound(song_path)
        else:
            print("Song not found.")

    def create_playlist(self, playlist_name, songs):
        self.playlists[playlist_name] = songs

    def play_playlist(self, playlist_name):
        songs = self.playlists.get(playlist_name)
        if songs:
            for song in songs:
                self.play_song(song)
        else:
            print("Playlist not found.")

    def manage_music(self):
        while True:
            print("1. List songs")
            print("2. Play a song")
            print("3. Create playlist")
            print("4. Play playlist")
            print("5. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.list_songs()
            elif choice == "2":
                song_name = input("Enter the song name to play: ")
                self.play_song(song_name)
            elif choice == "3":
                playlist_name = input("Enter playlist name: ")
                songs = input("Enter comma-separated song names: ").split(",")
                self.create_playlist(playlist_name, songs)
            elif choice == "4":
                playlist_name = input("Enter the playlist name to play: ")
                self.play_playlist(playlist_name)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


player = MusicPlayer()
player.manage_music()
