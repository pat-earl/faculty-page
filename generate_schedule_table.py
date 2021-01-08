#!/usr/bin/env python

#   Author:     Patrick Earl
#   Date:       12/29/2020
#   
#   File:       generate_schedule_table.py
#   
#       Use this file to generate an HTML table for a given semester. 
#       Will need to know the start and end date of the semester :-)

from datetime import datetime, timedelta
import sys, os
from pprint import pprint

START_DATE = datetime(2021, 1, 19)
END_DATE = datetime(2021, 5, 7)

WEEK_DATE_FORMAT = "%m/%d"

if __name__ == "__main__":

    # Holds the output. No need to write to files, just use bash redirect
    OUTPUT_HTML = """<table class="table">
    <thead>
        <tr>
            <th scope="col">Week</th>
            <th scope="col">Topic(s)</th>
            <th scope="col">Reading(s)</th>
        </tr>
    </thead>
    <tbody>"""

    cur_date = START_DATE
    week_num = 1

    # Special cases if the semester starts on a day other than monday
    week_start_date = cur_date

    while week_num <= 16:

        cur_date += timedelta(days=1)
        day_name = cur_date.strftime("%a")

        if day_name == "Mon":
            week_num += 1
            week_start_date = cur_date

        if day_name == "Fri":
            OUTPUT_HTML += "\n\t\t<tr>\n\t\t\t<td scope='row'>" + str(week_num) + "<br>(" + \
                            week_start_date.strftime(WEEK_DATE_FORMAT) + " - " + \
                            cur_date.strftime(WEEK_DATE_FORMAT) + ")</td>"

            OUTPUT_HTML += "\n\t\t\t<td></td>"
            OUTPUT_HTML += "\n\t\t\t<td></td>"

            OUTPUT_HTML += "\n\t\t</tr>"
    
    OUTPUT_HTML += "\n\t</tbody>\n</table>"
    # Replace tabs with 2 spaces (Markdown funny stuff :-))
    OUTPUT_HTML = OUTPUT_HTML.replace('\t', '  ')

    # pprint(OUTPUT_HTML)
    print(OUTPUT_HTML)
            
        

