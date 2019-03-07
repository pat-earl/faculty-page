#! /usr/bin/python3

#import cgitb; cgitb.enable()
import cgi, os, sys, csv, json, statistics

def tofloat(x):
    try: return float(x)
    except: return 0


print( "Content-type: application/json;\n" )

docroot = os.environ.get( 'CONTEXT_DOCUMENT_ROOT',
            os.environ.get('PWD') )
fname = os.path.join( docroot, '{{path_prefix}}',
            os.environ.get('QUERY_STRING') )

user = os.environ.get( 'eppn', '' )[:-len('@andrew.cmu.edu')]
{% if dev_env == 'local' %}
# No authentication; just impersonate someone for testing
user = 'afogelso'
{% endif %}

data = {}

try:
    with open(fname) as f:
        reader = csv.reader( f )
        header = next( reader )

        lname = header.index('Last Name')
        fname = header.index('Preferred/First Name')
        mi = header.index('MI')
        andrewid = header.index('Andrew ID')

        scores_start = max( lname, fname, mi, andrewid ) + 1
        scores_end = len( header )
        scores = [ [] for s in  range(scores_start, scores_end) ]

        # Put assignment titles in rows
        data['rows'] = header[ scores_start:scores_end ]

        # Put assignment scores, and statistics in columns
        data['cols'] = []

        for row in reader:
            # Check for users score
            if user == row[andrewid]:
                data['cols'].append( ['Your Score']
                        + row[scores_start:] + ['']*(scores_end - len(row)) )
                data['name'] = row[fname] + ' ' + row[lname]

            # Get non-zero HW scores in scores to compute statistics
            if row[lname] and row[fname] and row[andrewid]:
                for i, s in enumerate( row[scores_start:] ):
                    sf = tofloat(s)
                    if sf > 0: scores[i].append(sf)

            # Check for total points
            if row[lname] == '' and row[fname] == '':
                # print( 'getgrades.py:', row, file=sys.stderr )
                rf = map( tofloat, row[scores_start:scores_end] )
                if all( s != 0 for s in rf ):
                    data['cols'].append( ['Out of']
                            + row[scores_start:scores_end] )

                    # This is the last row we care about
                    break

    data['cols'].append( ['# Submissions']
            + [len(s) for s in scores] )

    data['cols'].append( ['Max']
            + [max(s) for s in scores] )

    #data['cols'].append( ['Min']
    #        + [min(s) for s in scores] )

    data['cols'].append( ['Median']
            + [round(statistics.median(s), 1) for s in scores] )

    data['cols'].append( ['Mean']
            + [round(statistics.mean(s), 1) for s in scores] )

    #data['cols'].append( ['Std. Dev']
    #        + [round(statistics.stdev(s), 2) for s in scores] )


    #data['rows'] = [row for row in reader]
    #data['scores'] = scores
except Exception as e:
    data['error'] = str(e)

print( json.JSONEncoder().encode( data ) )
