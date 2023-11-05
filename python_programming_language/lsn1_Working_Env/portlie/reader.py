#reader.py
#Modify file reader to be generic using Module - exercise 6.2

import csv

def read_csv(filename, types, *, errors='warn'):
    '''
    Read a CSV file with type conversion into a list of dicts 
    '''
    
    if errors not in { 'warn', 'silent', 'raise' }:
        raise ValueError("Errors must be one of 'warn', 'silent', 'raise'")
    
    records = []   # make empty list initialise list of records

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)           #skip a single line of input to accomodate header row
        for rowno, row in enumerate(rows, start=1): #enumerate function allows builtin counter
            try:
                row = [ func(val) for func, val in zip(types, row)]
            except ValueError as err:  #write exception ValueError reason to variable err
                if errors == 'warn':
                    print('Row:', rowno, 'Bad row:', row)
                    print('Row:', rowno, 'Error Reason:', err)
                elif errors == 'raise':
                    raise              #reraises the last exception
                else:
                    pass               #ignore
                continue               #skips to next row
            record = dict(zip(headers, row))
            records.append(record)
        return records 




