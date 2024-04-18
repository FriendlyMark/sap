import csv
import pyperclip

# Function to try decoding with utf-8 first, then latin-1 if it fails
def decode_with_utf8_or_latin1(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            return list(csv.reader(csvfile))
    except UnicodeDecodeError:
        with open(file_path, newline='', encoding='latin-1') as csvfile:
            return list(csv.reader(csvfile))

# Open the CSV file with appropriate encoding
file_path = r"<PATH>"
csv_data = decode_with_utf8_or_latin1(file_path)

# Initialize an empty list to store formatted lines
formatted_lines = []

# Slice the list to skip the header row
csv_data = csv_data[1:]

# Iterate over each row in the CSV data
for row in csv_data:
    # Extract values from the row
    MaterialNumber = row[0]  # Assuming MaterialNumber is in the first column
    OuterCaseCode = row[2]
    Length = row[3]
    Width = row[4]
    Height = row[5]
    
    # Format the values into a string and append to the list
    formatted_line = "('{}', '{}', '{}', '{}', '{}'),".format(MaterialNumber, OuterCaseCode, Length, Width, Height)
    formatted_lines.append(formatted_line)

# Join the formatted lines into a single string
output_text = '\n'.join(formatted_lines)

# Copy the output to the clipboard
pyperclip.copy(output_text)
print(output_text)
# Print a message
print("Formatted lines copied to clipboard.")
