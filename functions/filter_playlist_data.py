import csv

def filter_playlist_data(input_filename, output_filename):
    # Try multiple encodings in order of likelihood
    encodings_to_try = ['utf-8', 'cp1252', 'latin1', 'iso-8859-1', 'utf-16']
    
    for encoding in encodings_to_try:
        try:
            with open(input_filename, 'r', encoding=encoding) as infile:
                reader = csv.reader(infile, delimiter='\t')
                header = next(reader)
                
                try:
                    artist_index = header.index('Artist')
                    name_index = header.index('Name')
                except ValueError:
                    print("Error: 'Artist' or 'Name' column not found in the header.")
                    return
                
                with open(output_filename, 'w', encoding='utf-8', newline='') as outfile:
                    outfile.write("Artist\tTitle\n")
                    for row in reader:
                        if len(row) > max(artist_index, name_index):
                            artist = row[artist_index]
                            title = row[name_index]
                            outfile.write(f"{artist} - {title}\n")
                
                print(f"✅ Success! Data filtered and saved to '{output_filename}'")
                print(f"   (File was encoded as: {encoding})")
                return  # Success, exit function
                
        except (UnicodeDecodeError, UnicodeError):
            continue  # Try next encoding
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' was not found.")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return
    
    print(f"Error: Could not decode file with any standard encoding.")
    print(f"Tried: {', '.join(encodings_to_try)}")