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
3. View comprehensive results showing all promoter candidates!

## Program Overview
This program analyzes DNA sequences to identify potential prokaryotic promoter regions by locating conserved consensus sequences and evaluating their spatial arrangement. The code validates DNA sequences, finds **all occurrences** of promoter motifs, and scores each potential promoter based on optimal spacing criteria.

### Key Features
- **Multiple motif detection**: Finds ALL occurrences of -35 and -10 consensus sequences
- **Pairing**: Tests every possible promoter combination 
- **Scoring**: Grades promoters from 40-100 based on spacing quality
- **Output**: Visual representation with detailed candidate information
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
Promoter Candidates:
Minus 35 Position: 0, Minus 10 Position: 22, Gap Distance: 16, Score: 100
  -35 Score: 100% (exact match)
  -10 Score: 100% (exact match)
Minus 35 Position: 28, Minus 10 Position: 47, Gap Distance: 13, Score: 60
  -35 Score: 100% (exact match)
  -10 Score: 100% (exact match)

DNA Sequence:        TTGACACCCCCCCCCCCCCCCCTATAATTTGACACCCCCCCCCCCCCTATAAT
Consensus Sequences: XXXXXX________________XXXXXXXXXXXX_____________XXXXXX
```

### Function Overview

**File Processing:**
- `sanitizeString(file_path: str) -> str:` - Remove whitespace and newline characters
- `validateDNAString(dna_seq: str) -> str:` - Remove non-nucleotide characters (keeps only A,T,C,G)

**Motif Detection:**
- `findAllMotifOccurrences(dna_sequence: str, motif: str) -> list:` - Find all occurrences of a specific motif
- `findAllPromoterCandidates(dna_sequence: str) -> list:` - Identify all valid promoter pairs

**Scoring:**
- `simple_gap_score(gap_distance: int) -> int:` - Score promoters based on spacing quality

**Output:**
- `output(first_index: int, last_index: int, promoter_candidates: list):` - Generate visual representation and results

**Legacy Functions (backward compatibility):**
- `locateFirst(input_string: str) -> int:` - Find first -35 consensus sequence
- `locateLast(input_string: str) -> int:` - Find first -10 consensus sequence

### Biological Background
Prokaryotic promoters are DNA regulatory sequences that facilitate transcription initiation by RNA polymerase. The -35 and -10 elements are recognized by sigma factors, with optimal spacing critical for promoter function and gene expression efficiency.
