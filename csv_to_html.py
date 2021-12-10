# importing pandas as pd
import pandas as pd
from IPython.display import HTML
  
# Make a reference to the weather_data.csv file path
csv_path = "Resources/weather_data.csv"
# Import the weather_data.csv file as a DataFrame
df = pd.read_csv(csv_path, encoding="utf-8")

# Assign to String
table = df.to_html("Resources/csv_to_html.html", index=False)
print(table)
