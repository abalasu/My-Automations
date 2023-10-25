import random, os
music_dir = 'D:\\Music'
songs = os.listdir(music_dir)
print(len(songs))
song = random.randint(0,len(songs))
print(song)
# Prints The Song Name
print(songs[song])  

os.startfile(os.path.join(music_dir, songs[song])) 
