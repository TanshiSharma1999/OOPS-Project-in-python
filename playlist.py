#Playlist Project using oops
class playList:
    def __init__(self,name):
        self.name=name
        self.songs=[]
    def add_songs(self,song):
        self.songs.append(song)
        print(f"Added: {song}")
    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")
        else:
            print("Song not found!")
    def show_songs(self):
        print(f"Playlist '{self.name}': ")
        for song in self.songs:
            print(f"- {song}")
print("_"*30)
my_playlist = playList("Favorites")   
while True:
    
    print("Playlist Favourite!!!")
    print("Press 1 to add")
    print("Press 2 to remove")
    print("Press 3 to show playlist")
    print("Press 4 to exit")
    try:
        opt=int(input("Enter a value: "))
        if opt==1:
            s=input("Enter song wish to add to playlist: ")
            my_playlist.add_songs(s)
        elif opt==2:
            s=input("Enter song wish to remove from the playlist: ")
            my_playlist.remove_song(s)
        elif opt==3:
            my_playlist.show_songs()
        elif opt==4:
            print("See you soon!Bye")
            break
        else:
            print("Invalid Value! Only 4 options available!")
        print("_"*30)
    except ValueError:
        print("Press only 1-4 to choose!")
        print("_"*30)