#Import the necessary models
import pandas as pd
import xlsxwriter

#Print statement to introduce the script to the user
print('\nWelcome to the gene name fixing script!\n')

#Set the prompt variable equal to a constant value
prompt = "> "

#Function to read in files and convert them to pandas data frames
def make_df(df):
    try:
        return pd.read_excel(df)
    except:
        return pd.read_csv(df)

#Read the master gene name into pandas and store the read file as a variable
official_gene_df_read = make_df('Gene_Symbol_Master.xlsx')

#Print statement to get the file that needs the gene names matched and fixed
print('\nPlease type in the full path to the file that you want to correct.\n')

#Store the file to be fixed as a variable
fix_df = input(prompt)

#Read the data frame and store the read file as a variable
fix_df_read = make_df(fix_df)

#Print statement
print('\nCongratulations! The file has been read. Here are the columns: \n')
print(list((fix_df_read.columns)))

#Print statement asking what column needs to be fixed
print('\nWhich column would you like to fix?\n')

#Variable to store the user inputted column name
fix_gene_column = input(prompt)

#Print statement
print('\nThe computer elves are hard at work fixing your gene names!')

#For loop to check if the gene name matches the offical column and appending if so
all_gene_rows = []
for genes in fix_df_read[fix_gene_column]:
    one_gene_row = []
    for gene in str(genes).split(';'):
        if gene in official_gene_df_read['Gene_Symbol'].values:
            one_gene_row.append(gene)
            break
    all_gene_rows.append(one_gene_row)

#Add the new names to the original to fix file
fix_df_read['Updated_Gene_Names'] = all_gene_rows
fix_df_read['Updated_Gene_Names'] = fix_df_read['Updated_Gene_Names'].map\
                            (lambda x: str(x)[2:-2])

#Write the data frame with fixed gene names to an excel file
out_file = pd.ExcelWriter(fix_df, engine='xlsxwriter')
fix_df_read.to_excel(out_file)
out_file.close()

#Print statements
print('\nDone!')
print('Your original file has been updated with fixed gene names!')
