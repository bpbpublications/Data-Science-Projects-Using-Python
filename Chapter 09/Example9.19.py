import pandas as pd
# Sample data
data = {
    'Math': [80, 90, 75],
    'Science': [85, 95, 70],
    'Date': ['2025-11-28', '2025-11-29', '2025-11-30'],
    'Time': ['10:30:00', '14:45:00', '09:15:00']
}
df = pd.DataFrame(data)
# Numeric combination: sum of scores
df['Total_Score'] = df['Math'] + df['Science']
# Date-time combination: create complete timestamp
df['Full_Timestamp'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
print(df)
