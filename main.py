import csv


# Function to convert the original CSV to the Anki importable CSV
def convert_csv_for_anki(input_csv_path, output_csv_path):
    with open(input_csv_path, mode='r', encoding='utf-8') as infile, \
            open(output_csv_path, mode='w', encoding='utf-8', newline='') as outfile:

        # Create a csv reader object from the input file (assuming tab-delimited)
        reader = csv.reader(infile, delimiter='\t')

        # Create a csv writer object for the output file
        writer = csv.writer(outfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Read the header row
        next(reader, None)

        # Iterate over the rows in the provided CSV
        for row in reader:
            if len(row) < 3:  # Skip incomplete rows
                continue
            word, pos, definition = row[:3]

            # Combine the POS and definition for the back of the card
            card_back = f"{pos}\n{definition}" if pos else definition

            # Write the word and the combined POS and definition to the output file
            writer.writerow([word, card_back])


# File paths
input_csv_path = 'english Dictionary.csv'  # TODO: replace with your actual input file path
output_csv_path = 'anki-english-dict.csv'  # TODO: replace with your actual output file path

# Convert the CSV
convert_csv_for_anki(input_csv_path, output_csv_path)
