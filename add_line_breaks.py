import csv
import logging
import sys

# Set up logging to include time, log level, and log message
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')


def convert_csv_for_anki_add_line_breaks(input_csv_path, output_csv_path):
    try:
        # Increase the maximum field size limit
        csv.field_size_limit(sys.maxsize)

        # Open the input CSV file for reading and the output CSV file for writing
        with open(input_csv_path, mode='r', encoding='utf-8', newline='') as infile, \
                open(output_csv_path, mode='w', encoding='utf-8', newline='') as outfile:

            reader = csv.reader(infile)  # Assuming tab delimiter
            writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_ALL)

            for row in reader:
                # If row has a definition column, process it
                if len(row) > 1:
                    # Replace ';' with ';<br><br>' in the definition column
                    definition_with_breaks = row[1].replace(';', ';<br><br>')
                    new_row = [row[0], definition_with_breaks]
                else:
                    # If no definition is present, write the row as is
                    new_row = row

                # Write the new row to the output file
                writer.writerow(new_row)
                logging.info(f'Processed term: {new_row[0]}')

        logging.info('CSV file conversion completed successfully.')

    except csv.Error as e:
        logging.exception(f'CSV error occurred: {e}')
    except Exception as e:
        logging.exception(f'An unexpected error occurred: {e}')


# File paths
input_csv_path = 'anki-english-dict.csv'  # TODO: Replace with your actual input file path
output_csv_path = 'anki-english-dict-processed.csv'  # TODO: Replace with your actual output file path

# Run the conversion function
convert_csv_for_anki_add_line_breaks(input_csv_path, output_csv_path)
