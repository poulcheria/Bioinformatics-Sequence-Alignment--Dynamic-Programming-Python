# Bioinformatics Sequence Alignment - Dynamic Programming in Python (Needleman-Wunsch/Smith-Waterman)

## Overview
This repository contains a Python script for performing sequence alignment using dynamic programming. The alignment can be either global, where the entire sequences are aligned, or local, where only a region of the sequences is aligned.

### Dynamic Programming
Dynamic programming is an optimization technique that stores the solutions to overlapping subproblems and reuses them to avoid redundant calculations. In the context of sequence alignment, dynamic programming helps find the optimal alignment by considering all possible alignments and choosing the one with the best score.

### Global Alignment
Global alignment aims to align two sequences completely from start to end, allowing gaps to be introduced at the beginning or end of the sequences if necessary. The Needleman-Wunsch algorithm is used for global alignment, and it takes into account three factors: match bonus, mismatch penalty, and gap penalty.

### Local Alignment
Local alignment finds the best alignment within a specific region of the sequences, allowing gaps to be introduced internally in the sequences. The Smith-Waterman algorithm is used for local alignment, considering match bonus, mismatch penalty, and gap penalty.

### Match Bonus, Mismatch Penalty, and Gap Penalty
- Match Bonus: A reward given when two characters in the sequences match.
- Mismatch Penalty: A penalty applied when two characters do not match.
- Gap Penalty: A penalty for introducing a gap (insertion or deletion) in the alignment.

### Alignment Score
The alignment score is a numerical value that reflects the quality of the alignment. Higher scores indicate better alignments. The alignment score is calculated based on the match bonuses, mismatch penalties, and gap penalties.

### Alignment Visualization
After running the alignment functions, the alignments can be visualized, showing the aligned sequences along with gaps and matches.

## Examples
The example sequences used in the scripts are for the sake of convenience ("GGTTCGTGGA" and "GATCGTGAATT"). However, in real-world scenarios, you can find gene codes or nucleic acid sequences in databases like NCBI (National Center for Biotechnology Information). 

## Installation and Usage
1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required libraries using `pip install numpy`.
4. Run the `bio_merged.py` script to execute the sequence alignment. Adjust the match bonuses, mismatch penalties, and gap penalties as needed for your specific alignment.


