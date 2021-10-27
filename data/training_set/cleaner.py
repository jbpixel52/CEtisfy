#%%
import csv
#%%
with open('./log_mini.csv',mode='r') as input, open('./log_out.csv',mode='w',newline='') as output:
    writer = csv.writer(output)
    reader = csv.reader(input)
    for row in reader:
        if row[6]=='true':
            writer.writerow(row)
    input.close()
    output.close()

# %%
