#!/bin/python3.9
"""

*******************
*** PLEASE READ ***
*******************

This module anonymizes and aggregates the peer critiques in the given directory.

Written by Akash Jain for CHE-402-SPRING-2020,
modified by Sam Hoover for CHE-401-FALL-2022.

Run code with `python3 anonymizer.py --path <path to folder with submissions>`.

************
*** DEMO ***
************

Using the below file structure as an example,

=======================================================================
+---CHEM-ENG 401/402
|   +---anonymize_and_aggregate (this directory)
|   |       anonymize_and_aggregate.py
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

run `python3 anonymizer.py --path ../peer-evaluations/section-01/round-01/proposals`
from the `anonymize-and-aggregate` directory to anonymize and aggregate the Section 1
proposal presentation peer critiques. All of the anonymized copies will be stored in the
../peer-evaluations/section-01/round-01/proposals/speakers` directory.

Make sure to install the required packages. Run `pip install -r requirements.txt` if unsure.
"""
import os
import shutil
import argparse
import openpyxl


# TODO:
# add email capability (will need to download student email list and match names based on similarity)


class Anonymizer():
    def __init__(self, path=''):
        self.path = path


    def get_path(self):
        """
        parse the argument from the command line.

        returns:
        - path ([string]): path to directory with submissions
        """
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-p', '--path', action='store',
            help='path to directory with peer reviews'
        )

        return parser.parse_args().path


    def anonymize_reviews(self, path):
        """
        Remove the name of reviewer and save graded files in .xlxs format.

        Arguments:
        - path ([string]): path to directory with submissions
        """
        speakers = {}
        save_path = os.path.join(path, '../speakers')
        if os.path.exists(save_path):  # check if graded_copies already exists
            print('\nspeakers directory already exists, removing and starting fresh.\n')
            shutil.rmtree(save_path)  # if exists, delete

        os.mkdir(save_path)  # create directory for anonymized copies to return to speaker

        count = 1
        reviewers = [x for x in os.listdir(path) if x.endswith('_assignsubmission_file_')]
        for rev in reviewers:  # reviewers
            for xls in os.listdir(os.path.join(path, rev)):  # reviews

                xls = os.path.join(path, rev, xls)  # create path to spreadsheet
                wb_obj = openpyxl.load_workbook(xls, data_only=True)  # load spreadsheet
                wb_obj.worksheets[0]['D6'] = ''  # remove reviewer name

                sheet_obj = wb_obj.active

                # extract, transform to lower case, and replace space with hyphen if cells not empty, else skip
                try:
                    sp = sheet_obj.cell(row=10, column=4).value.lower().replace(' ', '-')
                    exp = sheet_obj.cell(row=14, column=4).value.lower().replace(' ', '-')
                except:  # else, skip
                    print(f'An exception occured in review #{count:02} -> {rev}.')
                    break

                nem = f'{count:02}_{sp}_{exp}_anonymized_copy.xlsx'  # anonymized copy file name

                # create folder for speaker if does not exist, save to folder
                if sp in speakers:
                    speakers[sp].append(nem)
                else:
                    speakers[sp] = [nem]
                
                # check if folder exists for speaker, if not create
                if not os.path.exists(os.path.join(save_path, sp)):
                    os.mkdir(os.path.join(save_path, sp))

                # save anonymized copy to folder for speaker
                wb_obj.save(filename=os.path.join(save_path, sp, nem))
                
                count += 1


def main():
    """
    Get path and then anonymize and aggregate peer critiques.
    """
    anonymizer = Anonymizer()
    path = anonymizer.get_path()
    anonymizer.anonymize_reviews(path)


if __name__ == '__main__':
    main()
    print('\nDone!')
