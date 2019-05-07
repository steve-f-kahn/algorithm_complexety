import pytest
import sys
import os
import csv

sys.path.insert(0,os.path.abspath("lib"))

import timer 

class TestClass():
    def test_passes_a_result_to_a_csv_file(self):
        times = [1,2,3]
        def time():
            return times.pop(0)
        timer.time.time = time
        stopwatch = timer.Timer()
        def test(array):
            return array + 1
        
        stopwatch.start(test)
        with open('test_v1.csv', 'r') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                assert row[0] == '1'
    
    def teardown_class(self):
        os.remove('test_v1.csv')
                         
