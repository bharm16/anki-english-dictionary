import csv
import logging
import sys  # Import the sys module

# Configure logging to display the time, log level, and message
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')


def convert_csv_for_anki(input_csv_path, output_csv_path):
    try:
        # Increase the maximum field size limit
        maxInt = sys.maxsize
        while True:
            # Decrease the maxInt value by factor 10 as long as the OverflowError occurs.
            try:
                csv.field_size_limit(maxInt)
                break
            except OverflowError:
                maxInt = int(maxInt / 10)

        logging.info(f'Set CSV field size limit to: {maxInt}')

        # Open the input file in read mode and the output file in write mode
        with open(input_csv_path, mode='r', encoding='utf-8') as infile, \
                open(output_csv_path, mode='w', encoding='utf-8', newline='') as outfile:

            # Initialize a CSV reader that correctly handles comma-separated values
            reader = csv.reader(infile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

            # Initialize a CSV writer that uses semicolon as the delimiter
            writer = csv.writer(outfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # Attempt to read the header row, if present
            headers = next(reader, None)
            if headers is None:
                logging.warning('Input file is empty or the header row is missing.')
                return

            logging.info('Starting to process the CSV file.')

            # Process each row in the input CSV
            for row in reader:
                if len(row) < 2:  # Check for at least two columns (word and definition)
                    logging.warning(f'Skipped incomplete row: {row}')
                    continue

                # Combine all parts of the definition into a single string, if necessary
                word = row[0]
                definition = ' '.join(row[1:]).strip()

                # Write the processed row to the output file
                writer.writerow([word, definition])
                logging.info(f'Processed word: {word}')

            logging.info('Finished processing the CSV file.')

    except Exception as e:
        logging.exception(f'An error occurred while converting the CSV file: {e}')


# Paths for the input and output files
input_csv_path = 'english Dictionary.csv'  # Replace with your actual input file path
output_csv_path = 'anki-english-dict.csv'  # Replace with your actual output file path

# Run the conversion function
convert_csv_for_anki(input_csv_path, output_csv_path)
