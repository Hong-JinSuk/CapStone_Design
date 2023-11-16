import pandas as pd
import numpy as np

def random_place(Day_Schedule, isvisited): # 어느정도 가중치로 되는듯
    new_isvisited = isvisited.copy()  # Create a new isvisited DataFrame to track changes
    for col in Day_Schedule.columns:
        if not isvisited[col].all().item():  # Check if the column is not fully visited (at least one False)
            for row in Day_Schedule.index:
                if not isvisited.loc[row, col]:
                    values = Day_Schedule.loc[row, col].split(',')
                    
                    remaining_names = [name for name in values if not isvisited.get(name, False)]
                    if len(remaining_names) > 0:
                        sorted_remaining_names = sorted(remaining_names, key=lambda name: len(Day_Schedule[Day_Schedule == name].stack()))
                        selected_name = sorted_remaining_names[0]
                        
                        Day_Schedule.loc[row, col] = selected_name
                        new_isvisited[selected_name] = True
                        for other_row in Day_Schedule.index:
                            if other_row != row:
                                other_values = Day_Schedule.loc[other_row, col].split(',')
                                if selected_name in other_values:
                                    other_values.remove(selected_name)
                                    Day_Schedule.loc[other_row, col] = ','.join(other_values)
            
            new_isvisited[col] = True  # Set the column as fully visited
        
    new_isvisited = new_isvisited.iloc[:, :7]  # Slice to keep only the relevant columns
    return Day_Schedule, new_isvisited