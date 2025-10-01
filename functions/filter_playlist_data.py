import csv

def filter_playlist_data(input_filename, output_filename):
    """
    Reads a tab-delimited Apple Music/iTunes text export and writes
    a new file with only the Artist and Track Title.
    """
    try:
        # 1. Read the tab-delimited input file
        with open(input_filename, 'r', encoding='cp1252') as infile:
            # Tell the csv reader that the delimiter is a tab
            reader = csv.reader(infile, delimiter='\t')
            header = next(reader) # Read the header row

            # Find the indices (column numbers) for Artist and Name (Track Title)
            try:
                artist_index = header.index('Artist')
                name_index = header.index('Name')
            except ValueError:
                print("Error: 'Artist' or 'Name' column not found in the header.")
                return

            # 2. Write the filtered data to a new text file
            with open(output_filename, 'w', encoding='utf-8', newline='') as outfile:
                # Write a simple header for the new file
                outfile.write("Artist\tTitle\n")

                # Iterate through the rest of the rows
                for row in reader:
                    if len(row) > max(artist_index, name_index):
                        artist = row[artist_index]
                        title = row[name_index]
                        outfile.write(f"{artist} - {title}\n")

        print(f"✅ Success! Data filtered and saved to '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")