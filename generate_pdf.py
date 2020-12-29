#!/usr/bin/env python
#
#   Author: Patrick Earl
#   Date: 12/29/2020
#
#   File: generate_pdf.py
#   KU Admin likes paper versions of the first day handouts. Find them in the ./out dir and
#   convert the main part to a pdf.

import os, sys

import pypandoc
from bs4 import BeautifulSoup

from pprint import pprint

if __name__ == "__main__":

    if not os.path.isdir('./out'):
        print("./out directory isn't created!")
        sys.exit()

    if not os.path.isdir("./syllabus-pdfs/"):
        os.mkdir("./syllabus-pdfs")

    for (root, dirs, files) in os.walk("./out", topdown=False):

        for name in files:
            if 'firstday' in name:           
                soup = BeautifulSoup(open(os.path.join(root, name)), "html.parser")

                fdh = soup.find('div', {"class": "justify"})
                course_code = soup.find('span', {"id": "course_code"}).text
                semester = soup.find('span', {"id": "semester_code"}).text

                print("Generating {} PDF for Semester {}".format(course_code, semester))   

                # fdh = pypandoc.convert_text(fdh, 'md', format='html')


                pypandoc.convert_text(fdh, 'pdf', 
                    format='html', 
                    outputfile='./syllabus-pdfs/' + course_code + '_' + semester + '_FDH.pdf',
                    extra_args=['-V', 'geometry:margin=1in', '--pdf-engine=xelatex'])

    print("--- Done ---")