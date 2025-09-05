"""
DNA Sequence Promoter Finder
----------------------------

Purpose:
This program reads a DNA sequence from a text file,
removes unnecessary characters (spaces, line breaks),
and validates that the sequence only contains the
four standard DNA bases: A, T, C, G.

It then compares the cleaned DNA sequence to known
promoter motifs stored in a CSV file, calculates
similarity scores, writes the results to a new CSV
file, and prints a quick summary of the best matches.

Biological context:
Promoters are short DNA motifs that signal where
gene transcription should begin. Identifying these
motifs helps us predict gene expression patterns.

Program flow:
1. Ask the user for the DNA file name.
2. Sanitize the DNA (remove spaces/newlines).
3. Validate the DNA (keep only A, T, C, G).
4. Print the cleaned DNA sequence.
5. Ask the user for a promoter motifs CSV file.
6. Read promoter motifs from the CSV file.
7. Compare DNA sequence to motifs and calculate scores.
8. Save results to a timestamped CSV file.
9. Print the highest scoring motifs in the terminal.

Usage:
$ python findProkPromoter.py
"""

import sys  # Standard library for exiting program on invalid input

GAP_MIN = 16
GAP_AVERAGE = 17
GAP_MAX = 19

def sanitizeString(file_path: str) -> str:
    """
    Reads a DNA sequence from a text file and removes
    whitespace and newline characters. Returns the cleaned string.
    """
    if file_path.endswith('.txt') == False:
        print("Error: Please enter a valid .txt filename")
        sys.exit()
    with open(file_path, "r") as f:        # Open the file in read mode
        data = f.read()                    # Read the entire file as a string
    if not data.strip():  # if file is empty or only spaces/newlines
        print("Error: The file is empty.")
        sys.exit()
    cleaned = data.replace(" ", "")        # Remove all spaces
    cleaned = cleaned.replace("\n", "")    # Remove all newlines
    return cleaned


def validateDNAString(dna_seq: str) -> str:
    """
    Takes a DNA sequence string and removes any characters
    that are not A, T, C, or G. Returns the cleaned DNA string.
    """
    valid_bases = "ATCG"   # Allowed characters
    cleaned = ""           # Start with empty string

    # Loop through each character in the input sequence
    for base in dna_seq.upper():   # Convert to uppercase (handles lowercase input)
        if base in valid_bases:    # Keep only A, T, C, G
            cleaned = cleaned + base   # Add valid base to output string

    return cleaned

# scoring: add point for every missing char out of 
def locateFirst(input_string: str) -> int:
    return input_string.find('TTGACA') # Will return index of first letter in substring, or -1


def locateLast(input_string: str): 
    return input_string.find('TATAAT') # Will return index of first letter in substring, or -1

def measureGapAndScore(first: int, last: int):
    gap_first = first + 6
    gap_last = last - 1
    gap_distance = gap_last - gap_first
    if gap_distance > GAP_AVERAGE:
        score = gap_distance - GAP_MAX # Positive diff = bad
    else:
        score = GAP_MIN - gap_distance # positive diff = bad
    return score

def output(first_index: int, last_index: int):
    cs_indicator_string: str = '_' * len(validated_string) # Populating indicator line with blanks
    cs_indicator_string = list(cs_indicator_string)
    if first_index >= 0: # Checking to make sure find() actually found substring
        for i in range(0, 6):
            cs_indicator_string[first_index + i] = 'X'
    
    if last_index >= 0:
        for i in range(0, 6):
            cs_indicator_string[last_index + i] = 'X'

    cs_indicator_string = ''.join(cs_indicator_string)

    print(f"DNA Sequence: \t\t{validated_string}")
    print(f"Consensus Sequences: \t\033[31m{cs_indicator_string}\033[0m\n")

if __name__ == "__main__":
    # Step 1: Ask the user to type the file name
    file_name = input("Enter the DNA file name: ")
    
    # Step 2: Sanitize (remove spaces/newlines)
    cleaned_string = sanitizeString(file_name)

    # Step 3: Validate (remove invalid characters)
    validated_string = validateDNAString(cleaned_string)

    # Step 4: Print results for the user
    # print("After sanitize:", cleaned)
    # print("After validate:", validated)
    print("Here is the cleaned input DNA sequence:", validated_string, "\n")

    # Step 5: Locate -35 and -10 consensus sequences
    first_index = locateFirst(validated_string)
    last_index = locateLast(validated_string)
    is_scoreable: bool = True
    if (first_index < 0) or (last_index < 0):
        print("Could not find one of the consensus sequences. Will not score.")
        is_scoreable = False

    # Step 6: Calculate Score based on gap between two CS
    if is_scoreable:
        score = measureGapAndScore(first_index, last_index)
        print(f"Score: {score}")
    else:
        print(f"No Score Calculated")
        
    output(first_index, last_index)
