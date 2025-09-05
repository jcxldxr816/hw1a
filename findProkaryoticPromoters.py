"""
PROKARYOTIC PROMOTER FINDER PROGRAM

What this program does:
This program helps scientists find special DNA patterns called "promoters" in bacterial DNA.
Think of promoters like "start buttons" that tell the cell where to begin reading genes.

In bacteria, promoters have two important parts:
1. A "-35 element" with the pattern TTGACA (located about 35 letters before the gene)
2. A "-10 element" with the pattern TATAAT (located about 10 letters before the gene)

The program reads DNA from a file, finds these patterns, and tells you:
- Where each pattern is located
- How far apart they are (the "gap distance")
- How good each promoter is (a score from 40-100)

Better promoters have the right spacing between the two parts (16-19 letters apart is perfect).
"""

import sys  # This helps us stop the program if something goes wrong

# These numbers define what we consider "good spacing" between promoter parts
GAP_MIN = 16     # Minimum good distance
GAP_AVERAGE = 17 # Perfect distance  
GAP_MAX = 19     # Maximum good distance

def sanitizeString(file_path: str) -> str:
    """
    STEP 1: READ AND CLEAN THE DNA FILE
    
    What this function does:
    - Opens a text file containing DNA letters
    - Removes extra spaces and line breaks that might mess up our analysis
    - Makes sure the file exists and isn't empty
    
    Think of this like cleaning up a messy document before reading it.
    
    Input: The name of a .txt file (like "dna.txt")
    Output: A clean string of DNA letters with no spaces or line breaks
    """
    
    # First, check if the filename ends with .txt
    if file_path.endswith('.txt') == False:
        print("Error: Please enter a valid .txt filename")
        sys.exit()  # Stop the program - we need a proper file
    
    try:
        # Try to open and read the file
        with open(file_path, "r") as f:        # Open the file in read mode
            data = f.read()                    # Read everything in the file as one big string
        
        # Check if the file is empty (no content or just spaces/newlines)
        if not data.strip():  
            print("Error: The file is empty.")
            sys.exit()  # Stop - we need actual DNA content
        
        # Clean up the DNA string by removing unwanted characters
        cleaned = data.replace(" ", "")        # Remove all spaces
        cleaned = cleaned.replace("\n", "")    # Remove all line breaks
        return cleaned
        
    except FileNotFoundError:
        # This happens if the file doesn't exist
        print("Error: '.txt' file does not exist.")
        sys.exit()  # Stop - we can't analyze a file that doesn't exist


def validateDNAString(dna_seq: str) -> str:
    """
    STEP 2: MAKE SURE WE HAVE VALID DNA
    
    What this function does:
    - Takes the cleaned file content and keeps only real DNA letters
    - DNA only has 4 letters: A, T, C, G (representing the 4 DNA bases)
    - Removes any other characters like numbers, punctuation, or weird letters
    
    Think of this like a spell-checker that only allows DNA letters.
    
    Input: A string that might have non-DNA characters
    Output: A clean string with only A, T, C, G letters
    """
    
    valid_bases = "ATCG"   # These are the only letters allowed in DNA
    cleaned = ""           # Start with an empty result string

    # Look at each character in the input, one by one
    for base in dna_seq.upper():   # Convert to uppercase (so 'a' becomes 'A')
        if base in valid_bases:    # If it's a valid DNA letter (A, T, C, or G)
            cleaned = cleaned + base   # Add it to our clean result string
        # If it's not a valid DNA letter, we just ignore it

    return cleaned


def locateFirst(input_string: str) -> int:
    """
    What this function does:
    - Looks for the first occurrence of "TTGACA" (the -35 promoter pattern)
    - Returns the position where it starts (counting from 0)
    Input: DNA string to search
    Output: Position number where TTGACA starts (or -1 if not found)
    """
    return input_string.find('TTGACA')  # Find first TTGACA pattern


def locateLast(input_string: str) -> int:
    """  
    What this function does:
    - Looks for the first occurrence of "TATAAT" (the -10 promoter pattern)
    - Returns the position where it starts (counting from 0)
    
    Note: Despite the name "Last", this actually finds the FIRST occurrence.
    Input: DNA string to search
    Output: Position number where TATAAT starts (or -1 if not found)
    """
    return input_string.find('TATAAT')  # Find first TATAAT pattern


def findAllMotifOccurrences(dna_sequence: str, motif: str) -> list:
    """
    STEP 3A: FIND ALL OCCURRENCES OF A DNA PATTERN
    
    What this function does:
    - Searches through the entire DNA sequence
    - Finds EVERY place where a specific pattern appears (not just the first one)
    - Returns a list of all the positions where the pattern was found
    
    This is like using "Find All" in a word processor instead of just "Find Next".
    
    Input: 
    - dna_sequence: The DNA string to search through
    - motif: The pattern to look for (like "TTGACA" or "TATAAT")
    
    Output: A list of position numbers where the pattern appears
    Example: If "TTGACA" appears at positions 5, 23, and 67, returns [5, 23, 67]
    """
    
    positions = []  # Start with an empty list to store positions
    start = 0       # Begin searching from the beginning of the DNA
    
    # Keep searching until we've checked the entire DNA sequence
    while True:
        # Look for the pattern starting from our current position
        pos = dna_sequence.find(motif, start)
        
        if pos == -1:  # -1 means "not found" - we've reached the end
            break      # Stop searching
            
        positions.append(pos)  # Add this position to our list
        start = pos + 1        # Start next search one position after this match
        
    return positions  # Return the complete list of positions


def simple_gap_score(gap_distance: int) -> int:
    """
    STEP 3B: SCORE HOW GOOD A PROMOTER IS
    
    What this function does:
    - Takes the distance between -35 and -10 promoter elements
    - Gives a score from 40-100 based on how "good" that distance is
    - Better spacing = higher score = more likely to be a real, working promoter
    
    Think of this like grading a test - perfect spacing gets 100%, poor spacing gets 40%.
    
    Scoring rules (based on real biology):
    - 16-19 letters apart = 100 points (PERFECT - this is what bacteria prefer)
    - 14-21 letters apart = 80 points (GOOD - still works well)  
    - 12-23 letters apart = 60 points (OK - might work, but not ideal)
    - Everything else = 40 points (POOR - probably doesn't work)
    
    Input: gap_distance (how many letters between the two promoter parts)
    Output: A score from 40 to 100
    """
    
    if 16 <= gap_distance <= 19:
        return 100  # Perfect spacing - this is the sweet spot for bacteria
    elif 14 <= gap_distance <= 21:
        return 80   # Good spacing - still very functional
    elif 12 <= gap_distance <= 23:
        return 60   # Acceptable spacing - might work but not optimal
    else:
        return 40   # Poor spacing - probably won't work as a promoter


def findAllPromoterCandidates(dna_sequence: str) -> list:
    """
    STEP 3C: FIND AND ANALYZE ALL POSSIBLE PROMOTERS
    
    What this function does:
    - Finds every -35 element (TTGACA) in the DNA
    - Finds every -10 element (TATAAT) in the DNA  
    - Tests every possible combination to see which ones could be promoters
    - Calculates how good each potential promoter is
    - Returns a sorted list of the best promoter candidates
    
    Think of this like a matchmaking service - it tries every possible pairing
    and tells you which combinations work best together.
    
    Rules for a valid promoter:
    1. Must have a -35 element (TTGACA) 
    2. Must have a -10 element (TATAAT)
    3. The -35 must come BEFORE the -10 in the DNA sequence
    4. We calculate the gap distance and score each combination
    
    Input: DNA sequence to analyze
    Output: List of promoter candidates, each containing:
            (position_of_-35, position_of_-10, gap_distance, quality_score)
    """
    
    # Find all the -35 elements (TTGACA patterns) in the DNA
    minus35_positions = findAllMotifOccurrences(dna_sequence, 'TTGACA')
    
    # Find all the -10 elements (TATAAT patterns) in the DNA
    minus10_positions = findAllMotifOccurrences(dna_sequence, 'TATAAT')
    
    promoter_candidates = []  # Start with empty list of candidates
    
    # Try every possible combination of -35 and -10 elements
    for pos35 in minus35_positions:      # For each -35 element we found
        for pos10 in minus10_positions:  # Try pairing it with each -10 element
            
            # Rule: -35 must come before -10 in the DNA sequence
            if pos35 < pos10:
                
                # Calculate the gap between the two elements
                # Gap = distance from END of -35 to START of -10
                gap_start = pos35 + 6  # End of -35 (TTGACA is 6 letters long)
                gap_end = pos10        # Start of -10 element
                gap_distance = gap_end - gap_start
                
                # Score this promoter candidate based on gap distance
                score = simple_gap_score(gap_distance)
                
                # Add this candidate to our list
                promoter_candidates.append((pos35, pos10, gap_distance, score))
    
    # Sort the candidates by score (best promoters first)
    # This uses a lambda function to sort by the 4th item (index 3) which is the score
    promoter_candidates.sort(key=lambda x: x[3], reverse=True)
    
    return promoter_candidates


def output(first_index: int, last_index: int, promoter_candidates: list):
    """
    STEP 4: CREATE VISUAL DISPLAY OF PROMOTER LOCATIONS
    
    What this function does:
    - Creates a visual map showing where promoters are located in the DNA
    - Uses 'X' marks to show promoter elements and '_' for regular DNA
    - Displays the original DNA sequence and the promoter map underneath
    
    Think of this like highlighting important parts of a document with a marker.
    
    The output looks like this:
    DNA Sequence:        TTGACACCCCCCCCCCCCCCCCTATAATTTGACACCCCCCCCCCCCCTATAAT
    Consensus Sequences: XXXXXX________________XXXXXXXXXXXX_____________XXXXXX
    
    Where:
    - Each letter in the top line is a DNA base (A, T, C, G)
    - Each 'X' in the bottom line marks a promoter element
    - Each '_' in the bottom line is regular DNA (not part of a promoter)
    """
    
    # Create a line of underscores the same length as our DNA sequence
    cs_indicator_string: str = '_' * len(validated_string)
    cs_indicator_string = list(cs_indicator_string)  # Convert to list so we can modify it
    
    # Mark all the promoter candidates we found with 'X' symbols
    for pos35, pos10, gap_distance, score in promoter_candidates:
        
        # Mark the -35 element (TTGACA) with 'X' marks
        for i in range(0, 6):  # TTGACA is 6 letters long
            if pos35 + i < len(cs_indicator_string):  # Make sure we don't go past the end
                cs_indicator_string[pos35 + i] = 'X'
        
        # Mark the -10 element (TATAAT) with 'X' marks  
        for i in range(0, 6):  # TATAAT is 6 letters long
            if pos10 + i < len(cs_indicator_string):  # Make sure we don't go past the end
                cs_indicator_string[pos10 + i] = 'X'

    # Also mark the legacy first occurrences (for backward compatibility)
    if first_index >= 0:  # If we found a -35 element
        for i in range(0, 6):  # Mark all 6 positions of TTGACA
            cs_indicator_string[first_index + i] = 'X'
    
    if last_index >= 0:   # If we found a -10 element
        for i in range(0, 6):  # Mark all 6 positions of TATAAT
            cs_indicator_string[last_index + i] = 'X'

    # Convert our list back to a string for display
    cs_indicator_string = ''.join(cs_indicator_string)

    # Print the results with nice formatting
    print(f"DNA Sequence: \t\t{validated_string}")
    print(f"Consensus Sequences: \t\033[31m{cs_indicator_string}\033[0m\n")  # Red color for visibility


# MAIN PROGRAM - THIS IS WHERE EVERYTHING STARTS

if __name__ == "__main__":
    """
    MAIN PROGRAM FLOW
  
    
    This is the main part of the program that runs when you start it.
    It follows these steps:
    
    1. Ask the user for a DNA file name
    2. Clean up the file content (remove spaces, line breaks)
    3. Validate the DNA (keep only A, T, C, G letters)
    4. Find all possible promoter combinations
    5. Score and rank each promoter candidate
    6. Display the results in an easy-to-read format
    7. Show a visual map of where promoters are located
    """
    
    # Step 1: Ask the user to type the file name
    print("Please make sure your DNA file is in .txt format.\n")
    file_name = input("Enter the DNA file name: ")
    
    # Step 2: Clean up the file (remove spaces and line breaks)
    print("Reading and cleaning the DNA file...")
    cleaned_string = sanitizeString(file_name)

    # Step 3: Validate the DNA (keep only valid DNA letters: A, T, C, G)
    print("Validating DNA sequence...")
    validated_string = validateDNAString(cleaned_string)

    # Step 4: Show the user what we're working with
    print("Here is the cleaned input DNA sequence:", validated_string, "\n")

    # Step 5: Find and analyze all promoter candidates
    print("Searching for promoter candidates...")
    promoter_candidates = findAllPromoterCandidates(validated_string)
    
    # Step 6: Display detailed results for each promoter found
    if promoter_candidates:
        print(f"\n🎉 SUCCESS! Found {len(promoter_candidates)} promoter candidate(s):\n")
        
        for i, (pos35, pos10, gap_distance, score) in enumerate(promoter_candidates, 1):
            # Determine quality description based on score
            if score == 100:
                quality = "EXCELLENT (Perfect spacing!)"
            elif score == 80:
                quality = "VERY GOOD (Good spacing)"
            elif score == 60:
                quality = "MODERATE (Acceptable spacing)"
            else:
                quality = "POOR (Suboptimal spacing)"
            
            print(f"Promoter #{i}: {quality}")
            print(f"  📍 -35 motif (TTGACA) starts at position: {pos35}")
            print(f"  📍 -10 motif (TATAAT) starts at position: {pos10}")
            print(f"  📏 Gap distance: {gap_distance} base pairs")
            print(f"  ⭐ Quality score: {score}/100")
            print()
    else:
        print("\n❌ No promoter candidates found in this sequence.")
        print("This DNA might not contain bacterial promoters, or they might be")
        print("too different from the standard consensus sequences we're looking for.")

    # Step 7: Legacy analysis (for backward compatibility with older code)
    first_index = locateFirst(validated_string)
    last_index = locateLast(validated_string)
    
    # Step 8: Show visual representation of where promoters are located
    print("\n" + "="*60)
    print("VISUAL MAP OF PROMOTER LOCATIONS")
    print("="*60)
    print("(X marks show where promoter elements are located)\n")
    output(first_index, last_index, promoter_candidates)
    
    print("Analysis complete! 🧬")
   
