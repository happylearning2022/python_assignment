# Original string
original_strings = [
    '|column1 | column2 | column3   |',
    '|a | aa | aaa   |',
    '|b | bb | ccc   |',
    '+ this line should be ignored'
]

# Prepare insert statements
insert_statements = []
for string in original_strings[1:]:
    if string.startswith('+'):
        continue
    values = [value.strip() for value in string.strip('|').split('|')]
    insert_statement = f"INSERT INTO table_name (column1, column2, column3) VALUES ('{values[0]}', '{values[1]}', '{values[2]}');"
    insert_statements.append(insert_statement)

# Print insert statements
for statement in insert_statements:
    print(statement)
