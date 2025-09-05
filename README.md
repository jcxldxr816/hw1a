# Team 3 | Homework 1-a
Find prokaryotic promoter consensus sequences!
## Flow
1. Run the program:
`python findProkaryoticPromoters.py`
2. Enter the filename containing the DNA sequence:
`sampleFile.txt`
3. View results!

*Note: If only a single consensus sequence is located, a score will not be generated. This was a deliberate decision to avoid scoring inaccuracies due *

## Script
The following script for part 'a' of this assignent is a working prototype that reads a single strand of DNA. The code valdiates the DNA sequence and converts any lowercase nucletoides to uppercase and omits invalid characters. It finds exact matches to the common promoter motifs of TTGACT and TATATT for -35 and -10 consensus sequences. Lastly, it reports an an output highlighting the consensus sequences and gives a match score based off of the distance between the consensus sequences.

### Input Validation
The input DNA sequence is scanned for any whitespace or newline characters. The characters are also checked to ensure that they are either a 'T', 'A', 'C', or 'G'.

### Scoring - NEEDS UPDATING
Score is calculated using a point system. The score increases for every nucleotide that the distance deviates from the expected range. 

**The lower the score, the better**

### Function Overview
Remove whitespace and newline characters.
- `def sanitizeString(file_path: str) -> str:`

Remove any non-nucleotide characters (CGTA).
- `def validateDNAString(dna_seq: str) -> str:`

Determine the index for -35 and -10 consensus sequences.
- `def locateFirst(input_string: str) -> int:`
- `def locateLast(input_string: str) -> int:`

Determine the gap/distance between the two consensus sequences and then determine the score.
- `def measureGapAndScore(first: int, last: int):`

Output to the terminal a nun-numeric, readable report of consensus sequence locations.
- `def output(first_index: int, last_index: int):`

