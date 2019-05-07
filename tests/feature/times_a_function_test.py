import pytest
import sys
import os
import csv

sys.path.insert(0,os.path.abspath("lib"))

import timer 

class TestClass():
    def test_function_passes_a_results_to_a_csv_file(self):
        times = [1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9,1,10,1,11,1]
        def time():
            return times.pop(0)
        timer.time.time = time
        stopwatch = timer.Timer()
        def test(array):
            return array + 1
        
        stopwatch.start(test)
        i = 1
        with open('test_v1.csv', 'r') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                assert row[0] == f'{i}'
                i += 1

    def teardown_class(self):
        os.remove('test_v1.csv')
                         
