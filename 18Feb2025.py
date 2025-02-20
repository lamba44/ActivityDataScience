import pandas as pd


# Helper function: creates a DataFrame from a dictionary.
def create_dataframe_from_dict(data_dict, key_col_name, value_col_name):
    """
    Convert a dictionary to a DataFrame.

    Parameters:
      data_dict (dict): Dictionary with keys as responses (numeric) and values as counts.
      key_col_name (str): Column name for the response.
      value_col_name (str): Column name for the count.

    Returns:
      pd.DataFrame: DataFrame created from the dictionary.
    """
    df = pd.DataFrame(list(data_dict.items()), columns=[key_col_name, value_col_name])
    return df


# ==========================
# Define Dictionaries for Each Question
# ==========================

# 1. Year of Study
# Mapping: 1 = 1st year, 2 = 2nd year, etc.
year_of_study = {1: 4, 2: 4, 3: 11, 4: 3}

# 2. Preferred Way of Studying
# Mapping: 1 = Lecture-based, 2 = Hands-on projects, 3 = Group discussions, 4 = Self-Study
preferred_study = {1: 9, 2: 8, 3: 2, 4: 3}

# 3. Overall Course Quality (ratings 1-5)
overall_quality = {1: 1, 2: 2, 3: 7, 4: 4, 5: 8}

# 4. Instructor Satisfaction
# (Using "How satisfied are you with the lecture delivery by instructors?")
instructor_satisfaction = {1: 4, 2: 2, 3: 4, 4: 4, 5: 8}

# 5. Engaging Assignments/Projects
assignments_projects = {1: 1, 2: 1, 3: 4, 4: 9, 5: 7}

# 6. Course Materials Effectiveness
course_materials = {1: 5, 2: 2, 3: 2, 4: 5, 5: 8}

# 7. Instructor Explains Concepts Clearly
instructor_explains = {1: 1, 2: 3, 3: 4, 4: 9, 5: 5}

# 8. Student Participation Encouraged by Instructor
student_participation = {1: 2, 2: 2, 3: 5, 4: 5, 5: 8}

# 9. Instructor is Approachable for Doubts
approachable_for_doubts = {1: 1, 2: 2, 3: 4, 4: 9, 5: 6}

# 10. Well-Equipped Classroom (projectors, seating, board visibility)
well_equipped_classroom = {1: 4, 2: 1, 3: 2, 4: 7, 5: 8}

# 11. Effective Lab Sessions
effective_lab_sessions = {1: 2, 2: 1, 3: 2, 4: 7, 5: 10}

# 12. University Resources (library, online databases, study areas)
university_resources = {1: 5, 2: 1, 3: 2, 4: 9, 5: 5}

# 13. Hours per Week Spent Studying Outside Class
# (Some keys are non-numeric and will be filtered out.)
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
    "12 hours": 1,  # Non-numeric, will be filtered out
    "4-5 hrs": 1,  # Non-numeric, will be filtered out
}

# 14. How Often Do You Attend Lectures?
# Mapping: 1 = Always, 2 = Frequently, 3 = Occasionally, 4 = Rarely
attend_lectures = {1: 11, 2: 5, 3: 4, 4: 2}

# 15. Biggest Challenges Affecting Learning
# Mapping: 1 = Difficult course material, 2 = Ineffective teaching methods,
# 3 = Lack of study resources, 4 = Time management, 5 = Personal motivation
biggest_challenges = {1: 10, 2: 11, 3: 12, 4: 8, 5: 6}

# ==========================
# Create DataFrames for Each Question
# ==========================

df_year_of_study = create_dataframe_from_dict(year_of_study, "Year", "Count")
df_preferred_study = create_dataframe_from_dict(
    preferred_study, "Study Method", "Count"
)
df_overall_quality = create_dataframe_from_dict(overall_quality, "Rating", "Count")
df_instructor_satisfaction = create_dataframe_from_dict(
    instructor_satisfaction, "Rating", "Count"
)
df_assignments_projects = create_dataframe_from_dict(
    assignments_projects, "Rating", "Count"
)
df_course_materials = create_dataframe_from_dict(course_materials, "Rating", "Count")
df_instructor_explains = create_dataframe_from_dict(
    instructor_explains, "Rating", "Count"
)
df_student_participation = create_dataframe_from_dict(
    student_participation, "Rating", "Count"
)
df_approachable_for_doubts = create_dataframe_from_dict(
    approachable_for_doubts, "Rating", "Count"
)
df_well_equipped_classroom = create_dataframe_from_dict(
    well_equipped_classroom, "Rating", "Count"
)
df_effective_lab_sessions = create_dataframe_from_dict(
    effective_lab_sessions, "Rating", "Count"
)
df_university_resources = create_dataframe_from_dict(
    university_resources, "Rating", "Count"
)


# For study hours, filter non-numeric keys.
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


numeric_study_hours = {k: v for k, v in study_hours.items() if is_numeric(k)}
# Convert keys to numeric (float or int)
numeric_study_hours = {float(k): v for k, v in numeric_study_hours.items()}
df_study_hours = create_dataframe_from_dict(numeric_study_hours, "Hours", "Count")

df_attend_lectures = create_dataframe_from_dict(attend_lectures, "Attendance", "Count")
df_biggest_challenges = create_dataframe_from_dict(
    biggest_challenges, "Challenge", "Count"
)

# ==========================
# Print Individual DataFrames
# ==========================
print("Year of Study Data:")
print(df_year_of_study)

print("\nPreferred Study Method Data:")
print(df_preferred_study)

print("\nOverall Course Quality Data:")
print(df_overall_quality)

print("\nInstructor Satisfaction Data:")
print(df_instructor_satisfaction)

print("\nEngaging Assignments/Projects Data:")
print(df_assignments_projects)

print("\nCourse Materials Data:")
print(df_course_materials)

print("\nInstructor Explains Concepts Clearly Data:")
print(df_instructor_explains)

print("\nStudent Participation Data:")
print(df_student_participation)

print("\nInstructor Approachable for Doubts Data:")
print(df_approachable_for_doubts)

print("\nWell-Equipped Classroom Data:")
print(df_well_equipped_classroom)

print("\nEffective Lab Sessions Data:")
print(df_effective_lab_sessions)

print("\nUniversity Resources Data:")
print(df_university_resources)

print("\nStudy Hours per Week Data:")
print(df_study_hours)

print("\nLecture Attendance Data:")
print(df_attend_lectures)

print("\nBiggest Challenges Data:")
print(df_biggest_challenges)

# ==========================
# Optional: Combine Multiple Questions into One DataFrame
# ==========================
combined_data = []


# Helper function to add data from a question dictionary into the combined list.
def append_data(question_name, data_dict, response_label="Response"):
    for response, count in data_dict.items():
        combined_data.append(
            {"Question": question_name, response_label: response, "Count": count}
        )


append_data("Year of Study", year_of_study, "Year")
append_data("Preferred Study Method", preferred_study, "Study Method")
append_data("Overall Course Quality", overall_quality)
append_data("Instructor Satisfaction", instructor_satisfaction)
append_data("Engaging Assignments/Projects", assignments_projects)
append_data("Course Materials", course_materials)
append_data("Instructor Explains Concepts", instructor_explains)
append_data("Student Participation", student_participation)
append_data("Instructor Approachable for Doubts", approachable_for_doubts)
append_data("Well-Equipped Classroom", well_equipped_classroom)
append_data("Effective Lab Sessions", effective_lab_sessions)
append_data("University Resources", university_resources)
# For study hours, we already have numeric keys.
append_data("Study Hours per Week", numeric_study_hours, "Hours")
append_data("Lecture Attendance", attend_lectures, "Attendance")
append_data("Biggest Challenges", biggest_challenges, "Challenge")

df_combined = pd.DataFrame(combined_data)

print("\nCombined DataFrame:")
print(df_combined)
