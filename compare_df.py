import pandas as pd


def compare_dataframes(df_source, df_target, key_columns, compare_columns):
    # Merge dataframes on key columns
    merged_df = pd.merge(df_source, df_target, on=key_columns, suffixes=('_source', '_target'), how='outer',
                         indicator=True)

    # Initialize report dataframe
    report_data = []

    # Iterate over rows in merged dataframe
    for index, row in merged_df.iterrows():
        key_values = tuple(row[key] for key in key_columns)
        differences = {}

        # Check if the key values are present in both source and target
        if row['_merge'] == 'both':
            # Compare values in compare_columns
            for col in compare_columns:
                source_value = row[col + '_source']
                target_value = row[col + '_target']

                if source_value != target_value:
                    differences[col] = (source_value, target_value)

                    # Append difference for each column separately
                    diff_string = f"Source={source_value}, Target={target_value}"
                    report_data.append([key_values, col, source_value, target_value, diff_string])

        # Append rows to report dataframe
        if not differences:
            source_values = [row[col + '_source'] for col in compare_columns]
            target_values = [row[col + '_target'] for col in compare_columns]
            diff_string = "No differences"
            report_data.append([key_values] + source_values + target_values + [diff_string])

    # Create report dataframe
    report_df = pd.DataFrame(report_data,
                             columns=['Key'] + [f'Source_{col}' for col in compare_columns] + [f'Target_{col}' for col
                                                                                               in compare_columns] + [
                                         'Difference'])

    return report_df


# Example usage:
# Assuming df_source and df_target are your source and target dataframes, and you have specified key columns and columns to compare
# For demonstration purposes, let's assume the following sample dataframes:

df_source = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

df_target = pd.DataFrame({
    'ID': [1, 2, 4],
    'Name': ['Alice', 'Bobby', 'David'],
    'Age': [25, 28, 40]
})

key_columns = ['ID']
compare_columns = ['Name', 'Age']

report = compare_dataframes(df_source, df_target, key_columns, compare_columns)
print(report)

report.to_html('test.html')
# df = df.applymap(lambda x: None if pd.isna(x) or (isinstance(x, str) and x.strip() == '') else x)

# for col in df.columns:
    # df[col] = df[col].apply(lambda x: None if pd.isna(x) or (isinstance(x, str) and x.strip() == '') else x)

