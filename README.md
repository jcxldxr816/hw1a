# Team 3 | Homework 1-a
Prokaryotic Promoter Detection Program - Find all promoter consensus sequences in DNA!

## Flow
1. Run the program:
   ```
   python findProkaryoticPromoters.py
   ```
2. Enter the filename containing the DNA sequence:
   ```
   dna.txt
   ```
3. View comprehensive results showing all numbered promoter candidates!

## Program Overview
This program analyzes DNA sequences to identify potential prokaryotic promoter regions by locating conserved consensus sequences and evaluating their spatial arrangement. The code validates DNA sequences, finds **all occurrences** of promoter motifs, and scores each potential promoter based on optimal spacing criteria.

### Key Features
- **Multiple motif detection**: Finds ALL occurrences of -35 and -10 consensus sequences
- **Pairing**: Tests every possible promoter combination 
- **Scoring**: Grades promoters from 40-100 based on spacing quality
- **Numbered output**: Each promoter candidate gets a clear reference number
- **Display**: Visual representation with detailed candidate information
- **Validation**: Handles file input errors and sequence cleaning

### Consensus Sequences
- **-35 element**: `TTGACA` (Pribnow box upstream element)
- **-10 element**: `TATAAT` (Pribnow box)
- **Optimal spacing**: 16-19 base pairs between elements

### Scoring System
The program uses a simple gap distance scoring system:
- **100 points**: Perfect spacing (16-19 bp) - Excellent promoter
- **80 points**: Good spacing (14-21 bp) - Very functional
- **60 points**: Acceptable spacing (12-23 bp) - Moderately functional  
- **40 points**: Poor spacing (all others) - Likely non-functional

**Higher scores indicate better promoters**

### Sample Output
```
Found 3 promoter candidate(s):

Promoter #1:
  -35 motif (TTGACA) at position: 0
  -10 motif (TATAAT) at position: 22
  Gap distance: 16 bp
  Score: 100/100

Promoter #2:
  -35 motif (TTGACA) at position: 28
  -10 motif (TATAAT) at position: 47
  Gap distance: 13 bp
  Score: 60/100

Promoter #3:
  -35 motif (TTGACA) at position: 0
  -10 motif (TATAAT) at position: 47
  Gap distance: 41 bp
  Score: 40/100

DNA Sequence:        TTGACACCCCCCCCCCCCCCCCTATAATTTGACACCCCCCCCCCCCCTATAAT
Consensus Sequences: XXXXXX________________XXXXXXXXXXXX_____________XXXXXX
```

### Function Overview

**File Processing:**
- `sanitizeString(file_path: str) -> str:` - Remove whitespace and newline characters
- `validateDNAString(dna_seq: str) -> str:` - Remove non-nucleotide characters (keeps only A,T,C,G)

**Motif Detection:**
- `findAllMotifOccurrences(dna_sequence: str, motif: str) -> list:` - Find all occurrences of a specific motif
- `findAllPromoterCandidates(dna_sequence: str) -> list:` - Identify all valid promoter pairs with scoring

**Scoring:**
- `simple_gap_score(gap_distance: int) -> int:` - Score promoters based on spacing quality

**Output:**
- `output(first_index: int, last_index: int, promoter_candidates: list):` - Generate visual representation and results

**Helper functions for locating consensus: **
- `locateFirst(input_string: str) -> int:` - Find first -35 consensus sequence
- `locateLast(input_string: str) -> int:` - Find first -10 consensus sequence

### Results Summary
The program successfully identifies and analyzes all potential promoter candidates in DNA sequences:
- **Comprehensive detection**: Finds every possible -35/-10 motif combination
- **Quality assessment**: Scores each candidate based on biological relevance
- **Clear presentation**: Numbers each promoter for easy reference
- **Visual mapping**: Shows motif locations with X markers in sequence alignment

### Biological Background
Prokaryotic promoters are DNA regulatory sequences that facilitate transcription initiation by RNA polymerase. The -35 and -10 elements are recognized by sigma factors, with optimal spacing critical for promoter function and gene expression efficiency.
