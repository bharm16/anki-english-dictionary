import csv
import logging
import sys

# Set up logging to include time, log level, and log message
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')


def convert_csv_for_anki(input_csv_path, output_csv_path):
    # Attempt to execute the CSV conversion
    try:
        # Increase the maximum field size limit due to the large size of definitions
        csv.field_size_limit(sys.maxsize)

        # Open the input and output files using the 'with' statement to ensure proper closure
        with open(input_csv_path, mode='r', encoding='utf-8', newline='') as infile, \
                open(output_csv_path, mode='w', encoding='utf-8', newline='') as outfile:

            # Initialize CSV reader and writer with appropriate settings
            # Using tab as a delimiter for input since the provided data is tab-separated
            reader = csv.reader(infile, delimiter=',')
            writer = csv.writer(outfile, delimiter=',')

            # Process each row in the input CSV file
            for row in reader:
                # Combine the POS and DEF columns into one column and construct the new row
                new_row = [row[0], ' '.join(row[1:]).strip()]

                # Write the new row to the output file
                writer.writerow(new_row)
                logging.info(f'Processed word: {new_row[0]}')

        logging.info('CSV file has been successfully converted.')

    except csv.Error as e:
        # Log any CSV-related errors that occur
        logging.exception(f'CSV error occurred: {e}')
    except Exception as e:
        # Log any other errors that occur
        logging.exception(f'An unexpected error occurred: {e}')


# File paths
input_csv_path = 'english Dictionary.csv'  # TODO: replace with your actual input file path
output_csv_path = 'anki-english-dict.csv'  # TODO: replace with your actual output file path


# Run the conversion function
convert_csv_for_anki(input_csv_path, output_csv_path)
