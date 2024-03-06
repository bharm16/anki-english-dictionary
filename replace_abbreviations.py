import csv
import logging
import sys
import re  # Import the regular expressions module

# Set up logging to include time, log level, and log message
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')

# Dictionary mapping abbreviations to their full forms
abbreviation_map = {
    'n.': 'noun',
    'adv.': 'adverb',
    'a.': 'adjective',
    'pl.': 'plural',
    'v. t.': 'verb transitive',
    'p. p.': 'past participle',
    'p. pr. & vb. n.': 'present participle and verbal noun',
    'prep.': 'preposition',
    'imp.': 'imperfect',
    'v. i.': 'verb intransitive'
}

def replace_abbreviations(text):
    # Use regular expression to replace abbreviations
    def replace_match(match):
        # The match group 1 contains the matched abbreviation without the potential HTML tag after it
        return abbreviation_map.get(match.group(1), match.group(1)) + match.group(2).lower()

    # Pattern to find the abbreviations followed by a period and optional HTML tag like '<br>'
    pattern = r'\b(' + '|'.join(re.escape(abb) for abb in abbreviation_map.keys()) + r')(</?\w+>|\b)'
    return re.sub(pattern, replace_match, text)


def convert_csv_and_replace_abbreviations(input_csv_path, output_csv_path):
    try:
        # Increase the maximum field size limit
        csv.field_size_limit(sys.maxsize)

        # Open the input CSV file for reading and the output CSV file for writing
        with open(input_csv_path, mode='r', encoding='utf-8', newline='') as infile, \
                open(output_csv_path, mode='w', encoding='utf-8', newline='') as outfile:

            reader = csv.reader(infile)  # Assuming tab delimiter
            writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_ALL)

            for row in reader:
                # Replace abbreviations with their full names in the definition column
                row[1] = replace_abbreviations(row[1])
                # Write the new row to the output file
                writer.writerow(row)
                logging.info(f'Processed term: {row[0]}')

        logging.info('CSV file conversion completed successfully.')

    except csv.Error as e:
        logging.exception(f'CSV error occurred: {e}')
    except Exception as e:
        logging.exception(f'An unexpected error occurred: {e}')


# File paths
input_csv_path = 'anki-english-dict-processed.csv'  # Replace with the actual input file path
output_csv_path = 'anki-english-dict-processed-abbreviations.csv'  # Replace with the actual output file path

# Run the conversion function
convert_csv_and_replace_abbreviations(input_csv_path, output_csv_path)
