
import pandas as pd
import datetime

# Load the Excel file (make sure 'timestamps.xlsx' is in the same directory)
input_file = "ratings.csv"  # Change this if your file has a different name

try:
    df = pd.read_csv(input_file)

    # Replace 'timestamp' with your actual column name if different
    def convert_timestamp(ts):
        try:
            return datetime.datetime.utcfromtimestamp(int(ts))
        except:
            return None  # In case of blank or invalid values

    df['DateTime_UTC'] = df['timestamp'].apply(convert_timestamp)

    # Save the result to a new Excel file
    output_file = "timestamps_converted.xlsx"
    df.to_excel(output_file, index=False)

    print(f"✅ Conversion complete. File saved as '{output_file}'.")

except FileNotFoundError:
    print(f"❌ File '{input_file}' not found. Please make sure it's in the same directory.")
except Exception as e:
    print(f"❌ An error occurred: {e}")
