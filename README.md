# Sample ETL Exercise
### Write a program/script that performs the following:
* Reads the 3 sample_files.* in Input/data_source_1/ and Input/data_source_2/ folders into a dataframe
* Consolidates the data from each file into a single dataframe
* Create a new column that will help track which data source the products originally came from
* Saves to a new output file in the Output dir using the name consolidated_output.1.csv
* Try to make this as 'production-ready' as possible - consider readability, stability, scalability and performance
* Consider building this so that it is easy to include new files to this process.

### Setup - please make sure your project is set up as per the below structure:
```
Input /
  data_source_1 /
  - sample_data.1.txt --> rename to sample_data.1.csv
  - sample_data.2.txt --> rename to sample_data.2.dat
  data_source_2 /
  - sample_data.3.txt --> rename to sample_data.3.dat
  - material_reference.txt --> rename to material_reference.csv
Output /
README.md
```

## Not required but would be nice to try the below bonuses

### Bonus 1:
* The `sample_data.1` file has a number of products we do not want in our output. Filter this data so that the only products that remain are products with a `worth` of MORE than `1.00`
* The true worth of products in `sample_data.3` is based on the listed `worth` TIMES the `material_id`, recalculate the `worth` for this file to show that.
* Products in `sample_data.2` have indivudal parts listed as separate products. Aggregate this data on `product_name`, keeping the FIRST `quality`, MAX `material_id`, and SUM of `worth`
* Load and use the `material_reference` data file to get the material name for each product in the final dataframe
* Write functionality that would also load the consolidated dataframe to a table in a database (this can be largely stubbed or mocked out - especially any actual DB calls)

### Bonus 2:
* Build a simple rest api framework (Django or Flask preferred) to return data from the consolidate_output file
* example: take quality as a param and return all products of that type

### Bonus 3:
* Build a simple UI to show the data (your choice of language/framework)