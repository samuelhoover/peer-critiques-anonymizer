# ChE-401-402-peer-critiques-anonymizer

This module anonymizes and aggregates the peer critiques for CHEM-ENG 401/402 in the given directory. Written by Akash Jain for CHE-402-SPRING-2020, modified by Sam Hoover for CHE-401-FALL-2022.

Run code with `python3 anonymize_and_aggregate.py --path <path to folder with submissions>`.

# DEMO

Using the below file structure as an example,

```
+---CHEM-ENG 401/402
|   +---anonymize_and_aggregate (this directory)
|   |       anonymize_and_aggregate.py
|   |       requirements.txt
|   |
|   +---peer-evaluations (where to store all the peer critiques)
|   |   +---section-01
|   |   |   +---round-01
|   |   |   |   +---progress-reports
|   |   |   |   |   +---reviewer_01
|   |   |   |   |   |       review_01.xlsx
|   |   |   |   |   |       review_02.xlsx
|   |   |   |   |   |       review_03.xlsx
|   |   |   |   |   +---reviewer_02
|   |   |   |   |   |       review_01.xlsx
|   |   |   |   |   |       review_02.xlsx
|   |   |   |   |   |       review_03.xlsx
|   :   :   :   :   :
|   :   :   :   :   :
|   |   |   |   +---proposals
|   |   |   |   |   +---reviewer_01
|   |   |   |   |   |       review_01.xlsx
|   |   |   |   |   |       review_02.xlsx
|   |   |   |   |   |       review_03.xlsx
|   |   |   |   |   +---reviewer_02
|   |   |   |   |   |       review_01.xlsx
|   |   |   |   |   |       review_02.xlsx
|   |   |   |   |   |       review_03.xlsx
:   :   :   :   :   :
:   :   :   :   :   :
```

run `python3 anonymize_and_aggregate.py --path ../peer-evaluations/section-01/round-01/proposals` while in the `anonymize-and-aggregate` directory to anonymize and aggregate the Section 1 proposal presentation peer critiques. All of the anonymized copies will be stored in the `../peer-evaluations/section-01/round-01/proposals/graded-copies` directory.

Make sure to install the required packages. Run `pip install -r requirements.txt` from this directory if unsure.
