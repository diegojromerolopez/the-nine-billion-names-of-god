import csv
import itertools
import os
from typing import List, Optional

from validate_ipa import Validator


def three_equal_consecutive_characters(god_name_candidate: str) -> bool:
    for i in range(len(god_name_candidate)):
        try:
            if god_name_candidate[i] == god_name_candidate[i+1] == god_name_candidate[i+2]:
                return True
        except IndexError:
            pass
        return False


def load_god_name_alphabet(god_name_alphabet_file_path: str) -> List[str]:
    god_name_alphabet: List[str] = []
    with open(god_name_alphabet_file_path, newline='') as csv_file:
        god_name_alphabet_reader = csv.DictReader(csv_file, delimiter=',', quotechar='|')
        for csv_row in god_name_alphabet_reader:
            god_name_alphabet.append(csv_row['ipa'])
    return god_name_alphabet


def write_the_nine_billion_names_of_god(
        output_file_path: str, name_length: int = 9,
        alphabet_file_path: Optional[str] = None
) -> int:
    # Default alphabet is IPA if not passed anyone
    if alphabet_file_path is None:
        alphabet_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'ipa_all.csv'
        )

    # Generate all possible combinations of alphabet characters
    god_name_counter = 0
    with open(output_file_path, 'w') as god_names_output_file:
        god_name_alphabet = load_god_name_alphabet(god_name_alphabet_file_path=alphabet_file_path)
        for god_name_list in itertools.combinations(god_name_alphabet, name_length):
            god_name_candidate = ''.join(god_name_list)
            if three_equal_consecutive_characters(god_name_candidate):
                continue

            if Validator().validate(god_name_candidate):
                god_names_output_file.write(f'{god_name_candidate}\n')
                god_name_counter += 1
    return god_name_counter


def main():
    output_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..', 'god_names.txt'
    )
    god_name_number = write_the_nine_billion_names_of_god(output_file_path=output_file_path)
    print('%s god name(s) have been generated' % god_name_number)


if __name__ == '__main__':
    main()
