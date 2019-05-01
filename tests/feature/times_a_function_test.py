import pytest
import sys
import os

sys.path.insert(0,os.path.abspath("lib"))

import timer 

class TestClass():
    def test_passes_a_result_to_a_csv_file(self):
        stopwatch = timer.Timer()
        function = lambda a,b :  a + b
        stopwatch.start(function(1,1))
