import os 
import glob
import pandas as pd


parent_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(parent_path, "input")
print(file_path)

dir_path = r'{}\**\sample_data*'.format(file_path)

df = pd.DataFrame()
for file in glob.glob(dir_path, recursive=True):   
    df_file = pd.read_csv(file)    
    df_file['file_name'] = os.path.basename(file)
    pd.concat([df,df_file], axis = 1)
    df = df.append(df_file, ignore_index=True)

out_path = os.path.join(parent_path, "output")
if not os.path.exists(out_path):
    os.mkdir(out_path)
out_put_file = os.path.join(out_path, "consolidated_output.1.csv")
df.to_csv(out_put_file)