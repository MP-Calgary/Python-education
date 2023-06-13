print()
print("reference a function in another file")
columns_data = [['Date', '2015/11/25', '2015/11/30', '2015/12/07', '2015/12/11', '2015/12/15'],
                ['Client', 'RandP', 'GOA', 'Robots and Pencils', 'AHS', 'Decisive Farming'],
                ['Project', 'r&p-robofactory-pm/ba guild', 'goa-rmas0049-firebans', 'sales-goa queens printer ministry', 'ahs-wait times-ios', 'decisive-scouting'],
                ['Project Code', '013', '066', '112', '040', '095'],
                ['Hours', 8.5, 6.5, 1.5, 3, 2]]

import sys
 
# adding MP_learn to the system path 
sys.path.insert(0, '//Users/michaelparker/Dropbox (Personal)/MP_Python/MP_learn/')

from useful_functions import display_table

display_table(columns_data)