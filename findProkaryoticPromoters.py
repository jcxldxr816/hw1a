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


import csv # Standard library for reading and writing CSV files (Lib/csv.py)
import datetime # Standard library for getting current time (Lib/datetime.py)
import heapq # Standard library for min-heap data structure. Used to track top X scores for quick output (Lib/heapq.py)
import sys  # Standard library for exiting program on invalid input

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


def outputQuickOverview(data_to_sort: list, amount_to_display: int, mismatch_masterlist: list):
    """
    Provides a quick overview of script results in the terminal.
    Takes as input the promoter motif CSV data, after score calculation.
    Takes as input the desired number of results to display.
    Takes as input the list of lists detailing character mismatch locations.
    """
    top_scores = []
    for index, row in enumerate(data_to_sort):
        score = row["Score"]
        motif_entry = (score, index, row) # Using index as a tiebreaker value for heap comparison. heapq can't compare equal values

        if len(top_scores) < amount_to_display:
            heapq.heappush(top_scores, motif_entry)
        else:
            heapq.heappushpop(top_scores, motif_entry) # This pops(removes) the smallest value from the heap
    top_scores = sorted(top_scores, key=lambda x: x[0], reverse=True) # Sorting by scores
    
    for score, _, row in top_scores:
        error_indicator_string: str = '_' * len(row['PromoterSeq']) # Populating error indicator line with blanks


        for error_indices_list in mismatch_masterlist:
            if error_indices_list[0] == row['PromoterSeq'].upper(): # Checking for error data on top score strings
                for i in range(1, len(error_indices_list)):
                    # Replacing blank with a red X to indicate mismatch
                    error_indicator_string = error_indicator_string[:error_indices_list[i]] + "X" + error_indicator_string[error_indices_list[i]+1:]

        print(f"Promoter ID: {row['id']}\t\tScore: {score:.3f}")
        print(f"DNA Sequence: \t\t{validated_string}")
        print(f"Promoter Sequence: \t{row['PromoterSeq'].upper()}")
        print(f"Mismatch View: \t\t\033[31m{error_indicator_string}\033[0m\n")

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