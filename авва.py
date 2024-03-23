import time
def measure_execution_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

import unittest
class TestExecutionTime(unittest.TestCase):
    def test_execution_time(self):
        def dummy_function():
            for i in range(1000000):
                pass
        execution_time = measure_execution_time(dummy_function)
        self.assertGreaterEqual(execution_time, 0)
if __name__ == '__main__':
    unittest.main()

