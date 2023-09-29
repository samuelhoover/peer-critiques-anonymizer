# ChE-401-402-peer-critiques-anonymizer

This module anonymizes, aggregates, and distributes the peer critiques 
in the given directory.

Written by Akash Jain for ChE 402 in Spring 2020,
modified by Sam Hoover for ChE 401 for Fall 2022 & Fall 2023.

Run code with `python3 anonymizer.py -s <path to folder with submissions>`.

# DEMO

Using the below file structure as an example,

```
=======================================================================
+---CHEM-ENG 401/402
|   +---anonymizer (this directory)
|   |       anonymizer.py
|   |       requirements.txt
|   |
|   +---peer-evaluations (where to store all the peer critiques)
|   |   +---section-01
|   |   |   +---round-01
|   |   |   |   +---progress-reports
|   |   |   |   |   +---reviewers
|   |   |   |   |   |   +---reviewer_01
|   |   |   |   |   |   |       review_01.xlsx
|   |   |   |   |   |   |       review_02.xlsx
|   |   |   |   |   |   |       review_03.xlsx
|   |   |   |   |   +---speakers
|   |   |   |   |   |   +---speaker_01
|   |   |   |   |   |   |       anonymized_review_01.xlsx
|   |   |   |   |   |   |       anonymized_review_02.xlsx
|   |   |   |   |   |   |       anonymized_review_03.xlsx
|   :   :   :   :   :
|   :   :   :   :   :
|   |   |   |   +---proposals
|   |   |   |   |   +---reviewers
|   |   |   |   |   |   +---reviewer_01
|   |   |   |   |   |   |       review_01.xlsx
|   |   |   |   |   |   |       review_02.xlsx
|   |   |   |   |   |   |       review_03.xlsx
|   |   |   |   |   +---speakers
|   |   |   |   |   |   +---speaker_01
|   |   |   |   |   |   |       anonymized_review_01.xlsx
|   |   |   |   |   |   |       anonymized_review_02.xlsx
|   |   |   |   |   |   |       anonymized_review_03.xlsx
:   :   :   :   :   :
:   :   :   :   :   :
=======================================================================
```

run `python3 anonymizer.py -s 
../peer-evaluations/section-01/round-01/proposals`
from the `anonymizer` directory to anonymize, aggregate, and
distribute the Section 1 proposal presentation peer critiques. All of 
the anonymized copies will be stored in the
`../peer-evaluations/section-01/round-01/proposals/speakers` directory.

Make sure to install the required packages. Run 
`pip install -r requirements.txt` if unsure.
