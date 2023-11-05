#table.py

def print_table(objects, columns):
    '''
    Make a nicely formatted table showing attributes from a list of objects
    '''

    for colname in colnames:
        print('{:>10s}'.format(colname), end=' ') #print column name without new line
    print()
    for obj in objetcts:
        for colname in colnames:
             print('{:>10s}'.format(str(getattr(obj, colname))), end=' ')
        print()
