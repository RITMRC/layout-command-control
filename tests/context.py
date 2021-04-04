import os
import sys
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import module_under_test
# in test files themselves do:
# from .context import module_under_test