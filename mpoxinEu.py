import pandas as pd
import json
import matplotlib.pyplot as plt


json_file_path = r'C:\Users\abdul\Desktop\HI -3\INNOVATION AND COMPLEXITY\project data representation\mpox.json'

# Load JSON data into a DataFrame
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Create a DataFrame from the loaded JSON data
df = pd.DataFrame(data)

# Convert 'DateRep' column to datetime type for better plotting
df['DateRep'] = pd.to_datetime(df['DateRep'])

# Plotting a line chart for Confirmed Cases over time for each country
plt.figure(figsize=(14, 8))

# Iterate over unique countries and plot their Confirmed Cases
for country in df['CountryExp'].unique():
    country_data = df[df['CountryExp'] == country]
    plt.plot(country_data['DateRep'], country_data['ConfCases'], label=country, marker='o', linestyle='-')

# Set plot details
plt.title('Confirmed Monkeypox Cases Over Time in European Countries')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Position the legend outside the plot
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
