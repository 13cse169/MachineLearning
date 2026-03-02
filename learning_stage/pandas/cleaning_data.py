try:
          import pandas as pd
except Exception:
          print("Something went wrong...!")
          

def read_csv_files():
          
          df = pd.read_csv("../../data/data.csv")
          
          print("\n Total Rows and Columns in CSV : ", df.shape)
          print("\n All Columns in CSV : ", df.columns)
          print("\n Datatype : \n", df.dtypes)
          print(df.info())
          
          # if the number of rows is not specified, the head() method will return the top 5 rows.
          print("\n Top 5 rows in CSV : \n", df.head())
          
          # The tail() method returns the headers and a specified number of rows, starting from the bottom.
          print("\n Buttom 5 rows in CSV : \n", df.tail())
          
          # use to_string() to print the entire DataFrame.
          print(df.to_string())
          
          new_df = df
          new_df.fillna(0, inplace=True)
          print(new_df.to_string())
          
          new_df.rename(columns={"Pulse": "HeartRate"}, inplace=True)
          print(new_df)
          
          new_df.drop(columns=['Calories'], inplace=True)
          print(new_df.shape)
          
          df.sort_values(by='Duration', inplace=True)
          print(df.to_string())
          
          # Export cleaned data
          # df.to_csv("cleaned_data.csv", index=False)
          
          
def cleaning_empty_cells():
          
          new_df = df.dropna()
          # By default, the dropna() method returns a new DataFrame, and will not change the original.
          print(new_df.to_string())
          print(new_df.shape)
          
          new_df_2 = df
          
          new_df_2.dropna(inplace = True)
          # Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.
          print(new_df_2.to_string())
          print(new_df_2.shape)

def cleaning_wrong_format():
          
          df = pd.read_csv("../../data/data.csv")
          print(df.to_string())
          print(df.shape)
          
          df['Date'] = pd.to_datetime(df['Date'], format='mixed')
          # Let's try to convert all cells in the 'Date' column into dates.
          print(df.to_string())
          print(df.shape)
          
          df.dropna(subset=['Date'], inplace=True)
          # Remove rows with a NULL value in the "Date" column
          print(df.to_string())
          print(df.shape)
          
          df.dropna(inplace=True)
          print(df.to_string())
          print(df.shape)
          
def fixing_wrong_data():
          
          df = pd.read_csv("../../data/data.csv")
          print(df.to_string())
          
          # df.loc[7, 'Duration'] = 45
          # print(df.to_string())
          
          df.loc[df.loc['Duration'] > 120, 'Duration'] = 120
          
          # for x in df.index:
                    # if df.loc[x, 'Duration'] > 120:
                              # df.loc[x, 'Duration'] = 120
                              # If the value is higher than 120, set it to 120:
                              
                              # df.drop(x, inplace=True)
                              # Delete rows where "Duration" is higher than 120:

          df['Date'] = pd.to_datetime(df['Date'], format='mixed')
          df.dropna(inplace=True)
          print(df.to_string())
          print(df.shape)
          
def removing_duplicates():
          
          df = pd.read_csv("../../data/data.csv")
          print(df.shape)
          
          df.dropna(inplace=True)
          df['Date'] = pd.to_datetime(df['Date'], format='mixed')
          
          df.loc[df.loc['Duration'] > 120, 'Duration'] = 120
          
          # for x in df.index:
                    # if df.loc[x, 'Duration'] > 120:
                              # df.loc[x, 'Duration'] = 120
          
          # Returns True for every row that is a duplicate, otherwise False:
          print(df.duplicated())
          
          # The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.
          df.drop_duplicates(inplace=True)
          
          print(df.to_string())
          print(df.shape)

def data_correlations():
          
          df = pd.read_csv("../../data/corr_data.csv")
          print(df.to_string())
          print(df.corr())
          
def main():
          #Read CSV Files
          read_csv_files()
          
          # Cleaning Empty Cells
          # cleaning_empty_cells()
          
          # Cleaning Data of Wrong Format
          # cleaning_wrong_format()
          
          # Fixing Wrong Data
          # fixing_wrong_data()
          
          # Removing Duplicates
          # removing_duplicates()
          
          # Data Correlations
          # data_correlations()

if __name__ == "__main__":
          main()