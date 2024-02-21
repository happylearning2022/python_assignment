# Original string
original_string = '''|column1 | column2 | column3   |
|a | aa | aaa   |
|b | bb | ccc   |
+ this line should be ignored'''

# Split the string into lines
original_strings = original_string.split('\n')

# Prepare insert statements
insert_statements = []
header_row = original_strings[0].strip('|').split('|')
for string in original_strings[1:]:
    if string.startswith('+'):
        continue
    values = [value.strip() for value in string.strip('|').split('|')]
    # Ensure number of values matches number of columns in header row
    if len(values) != len(header_row):
        print("Number of columns doesn't match with header row.")
        continue
    # Generate column names dynamically
    columns = ', '.join([column.strip() for column in header_row])
    # Generate values dynamically
    formatted_values = ", ".join([f"'{value}'" for value in values])
    insert_statement = f"INSERT INTO table_name ({columns}) VALUES ({formatted_values});"
    insert_statements.append(insert_statement)

# Print insert statements
for statement in insert_statements:
    print(statement)
