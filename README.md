# peer-critiques-anonymizer

This module anonymizes, aggregates, and distributes the peer critiques 
in the given directory.

Written by Akash Jain for ChE 402 in Spring 2020,
modified by Sam Hoover for ChE 401 for Fall 2022 & Fall 2023.

Run code with `python anonymizer.py -s <path to folder with submissions>`.

# PREREQUISITES
Need to download student list from Moonami! First, on the course webpage, go to
the "Participants" tab. Click on the box to select all participants then scroll
to the bottom of the list and download table as as .csv file from the "With
selected users..." dropdown menu. Using `anonymizer.py` for the first will
prompt you to input the full name of the .csv file of the student list
(including the extension). `anonymizer.py` will create a formatted version of
the student list file and replace the original file. All subsequent times using
`anonymizer.py` will use the student list file it created and will not prompt
for a student list file.


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

Run `python anonymizer.py -s ../peer-evaluations/section-01/round-01/proposals`
from the `anonymizer` directory ($ pwd is `<parent>/CHEM-ENG-401/anonymizer`)
to anonymize, aggregate, and distribute the Section 1 proposal presentation
peer critiques. All of the anonymized copies will be stored in the
`../peer-evaluations/section-01/round-01/proposals/speakers` directory. To do
the same for the Section 2 Round 3 progress reports, the command would be
`python anonymizer.py -s
../peer-evaluations/section-02/round-03/progress-reports`.

Make sure to install the required third-party packages:
[openpxyl](https://openpyxl.readthedocs.io/en/stable/) and
[pandas](https://pandas.pydata.org). Run `pip install -r requirements.txt` if
unsure.
