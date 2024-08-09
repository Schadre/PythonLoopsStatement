genres = ["Jazz", "Rock", "Hip-Hop", "Classical"]

for genre in genres:
    print(f"Now playing {genre}")

for index in range(len(genres)):
    print(f"Track {str(index +1)} : {genres[index]} - Light show is on!")

full_playlist = ["track1", "track2", "track3", "track4", "track5"]

middle_tracks = full_playlist[1:4]

for track in middle_tracks:
    print(f"Playing track {track} - The heart of our playlist!")