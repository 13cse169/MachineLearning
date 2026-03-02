try:
          import pandas as pd
          
except Exception:
          print("Something went wrong...")
          
def pandas_series():
          a = [1, 2, 3, 4]
          myVar = pd.Series(a)
          
          print(myVar)
          print(myVar[2])
          
          index = ['a', 'b', 'c']
          
          s = pd.Series(a, index = index)
          print(s)

def data_frame():
          data = {
                    "calories": [420, 380, 390],
                    "duration": [50, 40, 45]
          }
          
          df = pd.DataFrame(data)
          print(df)
          
          print(df.loc[0])
          print(df.loc[[0, 1]])
          
          df_2 = pd.DataFrame(data, index=["day_1", "day_2", "day_3"])
          print(df_2)
          print(df_2.loc["day_2"])

def read_csv():
          df = pd.read_csv("../../data/data.csv")
          
          print(df) # If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows
          print(df.to_string()) # use to_string() to print the entire DataFrame.
          
          print(pd.options.display.max_rows)
          
          pd.options.display.max_rows = 999 # You can change the maximum rows number with the same statement.
          

def analyzing_data_frames():
          df = pd.read_csv("../../data/data.csv")
          
          print("Print first 5 row of the DataFrame: \n", df.head())
          print("Using head function with 10: \n", df.head(10))
          #Note: if the number of rows is not specified, the head() method will return the top 5 rows.
          
          print(df.tail())
          # Print the last 5 rows of the DataFrame:
          
          print("\n\nThe DataFrame info : \n\n", df.info())
          

def main():
          #Pandas Series
          # pandas_series()
          
          #Pandas DataFrame
          # data_frame()
          
          #Pandas Read CSV
          # read_csv()
          
          #Analyzing DataFrames
          analyzing_data_frames()

if __name__ == "__main__":
          main()
          