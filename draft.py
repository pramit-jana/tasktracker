# import re

# # Regular expression pattern to match "day-1" to "day-30"
# pattern = r'day-(?:[1-9]|[12]\d|30)\b'  # Added a word boundary \b

# # Test strings
# test_strings = [
#     'day-1',
#     'day-10',
#     'day-20',
#     'day-30',
#     'day-0',    # Should not match (less than 1)
#     'day-31',   # Should not match (greater than 30)
#     'day-5.5',  # Should not match (contains a decimal point)
#     'day-15abc', # Should not match (contains non-numeric characters)
#     'day-40',   # Should not match (greater than 30)
#     'Some text before day-15 and more text after',
# ]

# for test_string in test_strings:
#     if re.search(pattern, test_string):
#         print(f'Match: {test_string}')
#     else:
#         print(f'No match: {test_string}')

from datetime import datetime, timedelta

# Starting date
start_date = datetime(2023, 1, 20)

# Add 30 days
result_date = start_date + timedelta(days=30)

print(result_date)
