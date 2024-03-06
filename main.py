import csv
import logging
import sys

# Set up logging to include time, log level, and log message
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')


def convert_csv_for_anki(input_csv_path, output_csv_path):
    try:
        # Increase the maximum field size limit
        csv.field_size_limit(sys.maxsize)

        with open(input_csv_path, mode='r', encoding='utf-8', newline='') as infile, \
                open(output_csv_path, mode='w', encoding='utf-8', newline='') as outfile:

            reader = csv.reader(infile)
            writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_ALL)

            for row in reader:
                # Combine the POS and DEF columns into one, ensuring HTML breaks are used for separation
                combined_def = '<br><br>'.join(row[1:]).strip()
                new_row = [row[0], combined_def]
                writer.writerow(new_row)
                logging.info(f'Processed word: {new_row[0]}')

        logging.info('CSV file conversion completed successfully.')

    except csv.Error as e:
        logging.exception(f'CSV error occurred: {e}')
    except Exception as e:
        logging.exception(f'An unexpected error occurred: {e}')


# File paths
input_csv_path = 'english Dictionary.csv'  # TODO: replace with your actual input file path
output_csv_path = 'anki-english-dict.csv'  # TODO: replace with your actual output file path


# Run the conversion function
convert_csv_for_anki(input_csv_path, output_csv_path)
