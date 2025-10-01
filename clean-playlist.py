import csv

from functions.filter_playlist_data import filter_playlist_data

# --- Configuration ---
INPUT_FILE = 'data/sot_2.txt'
OUTPUT_FILE = 'data/sot_2_filtered.txt'
# ---------------------

filter_playlist_data(INPUT_FILE, OUTPUT_FILE)