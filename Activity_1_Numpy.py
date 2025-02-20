import numpy as np
import pandas as pd

# ============================================================
# Step 1: Define the Survey Data (using our real counts)
# ============================================================

# Each dictionary maps a numeric response (or key) to the count.
year_of_study = {1: 4, 2: 4, 3: 11, 4: 3}
preferred_study = {1: 9, 2: 8, 3: 2, 4: 3}
overall_quality = {1: 1, 2: 2, 3: 7, 4: 4, 5: 8}
instructor_satisfaction = {1: 4, 2: 2, 3: 4, 4: 4, 5: 8}
assignments_projects = {1: 1, 2: 1, 3: 4, 4: 9, 5: 7}
course_materials = {1: 5, 2: 2, 3: 2, 4: 5, 5: 8}
instructor_explains = {1: 1, 2: 3, 3: 4, 4: 9, 5: 5}
student_participation = {1: 2, 2: 2, 3: 5, 4: 5, 5: 8}
approachable_for_doubts = {1: 1, 2: 2, 3: 4, 4: 9, 5: 6}
well_equipped_classroom = {1: 4, 2: 1, 3: 2, 4: 7, 5: 8}
effective_lab_sessions = {1: 2, 2: 1, 3: 2, 4: 7, 5: 10}
university_resources = {1: 5, 2: 1, 3: 2, 4: 9, 5: 5}

# For study hours, some keys are non-numeric (they will be filtered out)
study_hours = {
    "0": 3,
    "2": 1,
    "3": 1,
    "4": 2,
    "5": 2,
    "6": 1,
    "7": 1,
    "8": 1,
    "10": 1,
    "12": 2,
    "14": 1,
    "20": 2,
    "24": 1,
    "26": 1,
    "12 hours": 1,  # non-numeric key
    "4-5 hrs": 1,  # non-numeric key
}

attend_lectures = {1: 11, 2: 5, 3: 4, 4: 2}
biggest_challenges = {1: 10, 2: 11, 3: 12, 4: 8, 5: 6}

# ============================================================
# Step 2: Combine All the Numerical Data into One List
# ============================================================
# We want a uniform two-column data: [Value, Count]
combined_list = []


def append_to_combined(data_dict):
    """
    Append the key-value pairs from data_dict into combined_list.
    Keys that cannot be converted to a float are skipped.
    """
    for key, count in data_dict.items():
        try:
            numeric_key = float(key)
        except ValueError:
            continue  # skip non-numeric keys
        combined_list.append([numeric_key, count])


# Append each question's data
append_to_combined(year_of_study)
append_to_combined(preferred_study)
append_to_combined(overall_quality)
append_to_combined(instructor_satisfaction)
append_to_combined(assignments_projects)
append_to_combined(course_materials)
append_to_combined(instructor_explains)
append_to_combined(student_participation)
append_to_combined(approachable_for_doubts)
append_to_combined(well_equipped_classroom)
append_to_combined(effective_lab_sessions)
append_to_combined(university_resources)
append_to_combined(study_hours)  # only numeric keys will be kept
append_to_combined(attend_lectures)
append_to_combined(biggest_challenges)

# Create the NumPy array
data_array = np.array(combined_list)

# ============================================================
# Step 3: Basic Information About the Array
# ============================================================
print("Data Array:")
print(data_array)

# Shape and size of the array
print("\nShape of the array:", data_array.shape)
print("Size (total number of elements):", data_array.size)

# ============================================================
# Step 4: Reshape the Array
# ============================================================
# Our data_array has shape (81, 2) = 162 elements.
# We choose a shape that multiplies to 162. For example, (9, 18) works because 9*18 = 162.
reshaped_array = data_array.reshape(9, 18)
print("\nReshaped Array (9 rows, 18 columns):")
print(reshaped_array)

# ============================================================
# Step 5: Extract Rows/Columns Satisfying a Condition
# ============================================================
# For example, extract all rows where the "Count" (second column) is greater than 5.
condition_filtered = data_array[data_array[:, 1] > 5]
print("\nRows where Count > 5:")
print(condition_filtered)

# ============================================================
# Step 6: Statistical Operations
# ============================================================
# Compute statistics column-wise.
mean_vals = np.mean(data_array, axis=0)
median_vals = np.median(data_array, axis=0)
std_vals = np.std(data_array, axis=0)
variance_vals = np.var(data_array, axis=0)

print("\nMean (per column):", mean_vals)
print("Median (per column):", median_vals)
print("Standard Deviation (per column):", std_vals)
print("Variance (per column):", variance_vals)

# Find the minimum and maximum values in the entire array and their indices.
min_val = np.min(data_array)
max_val = np.max(data_array)
min_index = np.unravel_index(np.argmin(data_array), data_array.shape)
max_index = np.unravel_index(np.argmax(data_array), data_array.shape)

print("\nMinimum value:", min_val, "at index", min_index)
print("Maximum value:", max_val, "at index", max_index)

# ============================================================
# Step 7: Indexing and Slicing
# ============================================================
# Retrieve the first 10 rows.
first_10_rows = data_array[:10]
print("\nFirst 10 rows of the array:")
print(first_10_rows)

# Extract the "Count" column (column index 1) and multiply it by 2.
count_column = data_array[:, 1]
count_times_two = count_column * 2
print("\n'Count' column multiplied by 2:")
print(count_times_two)

# ============================================================
# Step 8: Element-wise Operations
# ============================================================
# Create another array of the same shape (e.g., an array of ones) for demonstration.
ones_array = np.ones_like(data_array)

# Element-wise addition, subtraction, and multiplication.
addition_result = data_array + ones_array
subtraction_result = data_array - ones_array
multiplication_result = data_array * ones_array

print("\nElement-wise Addition (data_array + ones_array):")
print(addition_result)
print("\nElement-wise Subtraction (data_array - ones_array):")
print(subtraction_result)
print("\nElement-wise Multiplication (data_array * ones_array):")
print(multiplication_result)

# Normalize the data_array so its values range between 0 and 1.
normalized_array = (data_array - np.min(data_array)) / (
    np.max(data_array) - np.min(data_array)
)
print("\nNormalized Array (values between 0 and 1):")
print(normalized_array)

# ============================================================
# Step 9: Sorting and Searching
# ============================================================
# Sort the array along axis 0 (sort each column independently).
sorted_array_axis0 = np.sort(data_array, axis=0)
print("\nArray sorted along axis 0 (column-wise):")
print(sorted_array_axis0)

# Sort the array along axis 1 (each row sorted independently).
sorted_array_axis1 = np.sort(data_array, axis=1)
print("\nArray sorted along axis 1 (row-wise):")
print(sorted_array_axis1)

# Search for the indices where values are greater than a threshold (e.g., > 5).
indices_greater_than_5 = np.where(data_array > 5)
print("\nIndices where array values > 5:")
print(indices_greater_than_5)
