# Playlist file cleaner 
A simple Pythons script that takes a txt-export from iTunes (Apple Music) and removes all information except for the artist and track title. The output text file can be used for Soundcloud descriptions etc. Ideal for dj's! 

## Requirements
- Have a version of [Python](https://www.python.org/) installed on your system. That's it!

## How to use
1. Export your playlist from iTunes (Apple Music) as a text file. You do this by selecting the playlist, then go to `File > Library > Export Playlist...` and choose `Text files (.txt)` as the format.
2. Download this repository as a ZIP file and extract it, or clone it using git. 
3. Place your exported playlist text file in the `data/` folder.
4. Edit the `clean_playlist.py` script to change the `INPUT_FILE` variable (to the name of your txt file) and `OUTPUT_FILE` variable if needed.
4. Open a terminal (command prompt) and navigate to the folder where you extracted/cloned the repository.
5. Run the script using the command: `python clean_playlist.py`
6. After running the script, you will find a new text file in the `data/` folder with the cleaned up playlist.