import pandas as pd

raw_data = pd.read_csv('../web_project/final_report.csv')

raw_data_df = pd.DataFrame(raw_data)

print(raw_data_df).head()

raw_data_df.to_html("../web_project/dataforsite.html")