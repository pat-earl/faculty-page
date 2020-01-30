#! /usr/bin/python3

#import cgitb; cgitb.enable()
import cgi, os, sys, csv, json, statistics, traceback

def tofloat(x):
    try: return float(x)
    except: return 0


print( "Content-type: application/json;\n" )

data = {}

try:
    arguments = cgi.FieldStorage();
    #print( 'getgrades.py:', arguments, file=sys.stderr )

    user = os.environ.get( 'eppn', '' )[:-len('@andrew.cmu.edu')]
    docroot = os.environ.get( 'CONTEXT_DOCUMENT_ROOT',
                os.environ.get('PWD') )
    dirname = os.path.join( docroot, '{{path_prefix}}',
                 arguments.getvalue('dirname') )

    data['rows'] = []
    data['cols'] = []

    yourscores = []
    scores = []
    nsubs = []
    outof = []

    for filename in json.JSONDecoder().decode(
            arguments.getvalue('filename') ):
        with open( os.path.join( dirname, filename) ) as f:
            reader = csv.reader( f )
            header = next( reader )

            lname = header.index('Last Name')
            fname = header.index('Preferred/First Name')
            mi = header.index('MI')
            andrewid = header.index('Andrew ID')

            scores_start = max( lname, fname, mi, andrewid ) + 1
            scores_end = len( header )
            f_scores = [ [] for s in  range(scores_start, scores_end) ]
            # Counts no of non zero scores
            f_nsubs = [0] * (scores_end - scores_start)
            f_outof = [''] * (scores_end - scores_start)
            f_yourscores = [''] * (scores_end - scores_start)

            # Put assignment titles in rows
            data['rows'] += header[ scores_start:scores_end ]

            # Put assignment scores, and statistics in data.cols
            for row in reader:
                # Pad in case of missing fields at end
                row += [''] * (scores_end - len(row))

                # Check for users score
                if user == row[andrewid] and len(user):
                    f_yourscores = row[scores_start:]
                    data['name'] = row[fname] + ' ' + row[lname]

                # Get non-zero HW scores in scores to compute statistics
                if row[lname] and row[fname] and row[andrewid]:
                    for i, s in enumerate( row[scores_start:] ):
                        sf = tofloat(s)
                        if sf > 0:
                            f_scores[i].append(sf)
                            f_nsubs[i]+=1

                # Check for total points
                if arguments.getvalue('show_total', 'true') == 'true':
                    try:
                        row[:scores_start].index( 'Out of' )
                        f_outof = row[scores_start:scores_end]

                        # This is the last row we care about
                        break
                    except:
                        pass
        #end with
        outof += f_outof
        scores += f_scores
        nsubs += f_nsubs
        yourscores += f_yourscores

    # Combine data from all files 
    cols = [(yourscores, 'Your Score / Grade'),
        (outof, 'Out of'),
    ]
    if arguments.getvalue( 'show_stats', 'true' ) == 'true':
        cols += [([n if n else '' for n in nsubs], '# submissions')]
    for (a, t) in cols:
        if t or any(a): data['cols'].append( [t] + a )

    if arguments.getvalue( 'show_stats', 'true' ) == 'true':
        stats=[ ('Max', max),
            ('Median', lambda x: '{:.1f}'.format( statistics.median(x)) ),
            ('Mean', lambda x: '{:.1f}'.format( statistics.mean(x)) ),
            #('Std. Dev', lambda x: round( statistics.stdev(s), 2) ),
        ]
        for (name, fn) in stats:
            #print( name, nsubs, file=sys.stderr )
            data['cols'].append( [name]
                + [fn(s) if nsubs[i] else ''
                    for (i, s) in enumerate(scores) ] )

    #data['rows'] = [row for row in reader]
    #data['scores'] = scores
except Exception as e:
    data['error'] = traceback.format_exc()
        #str(e)

print( json.JSONEncoder().encode( data ) )
