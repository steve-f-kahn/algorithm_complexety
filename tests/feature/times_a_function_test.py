import pytest
import sys
import os
import csv

sys.path.insert(0,os.path.abspath("lib"))

import timer 

class TestClass():
    def test_passes_a_result_to_a_csv_file(self):
        stopwatch = timer.Timer()
        def add(a,b):
            return a + b
        function = lambda a,b :  a + b
        stopwatch.start(add(1,1))
        # open csv file
        with open('add.csv', 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                    print(row)
                    assert len(row) > 0
                    return
            assert True == False 
                            
        # assert contents 
