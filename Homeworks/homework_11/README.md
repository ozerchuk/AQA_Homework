pip install flake8
pip install mypy
pip install requests
pip install pytest
pip install pytest-mock
pytest -v test_lib.py
pytest -s test_lib.py debug print
pytest -m test_lib.py deselect
pytest -k test_lib.py


Description of the executed work:

Changes that were made:

The 'get_random_number' function has been 
Renamed to 'generate_random_number' for better readability.

Import random as some_module was removed.

To generate random strings, Union[float, int] was 
used instead of float in the parameter.

Added handling of the case when the string length 
passed to the function is a float number.

The variable 'i' in the 'generate_random_string' function is replaced 
by '_' because we are not using the value of this variable in the loop.

Added comments to each function.



