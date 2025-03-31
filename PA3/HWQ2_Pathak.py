#%%
#File Name: HW2Q2_Pathak.py
#Author: Shivam Pathak
#Date: 2.22.25
#Complete Programs + Extra credit
#Question 2-1: Measure execution times of both insertion and merge sort using 6 data files
import time
import numpy as np
import pandas as pd

#Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

#Measure the time efficiency from HW1
def timeEfficiency(funcName, *args, **kwargs):
    """Measures execution time of a function."""
    # Normalize the base time
    start = time.time()   # Start time relative to base
    result = funcName(*args, **kwargs)  # Run the function
    end = time.time()  # End time relative to base

    total_time = round(end - start, 6)  # Calculate total time

    # Store results in a dictionary
    #result_dict = {
    #    'start': round(start, 6),
    #    'end': round(end, 6),
    #    'time efficiency': round(total_time, 6),
    #    'result': result[:10] + ["..."] + result[-10:] if len(result) > 20 else result
    #}

    #Removed the result print and only returns execution time
    return total_time


#Load the datasets
file_paths = {
    "rand1000": r"C:\Users\patha\PyCharmMiscProject\rand1000.txt",
    "rand10000": r"C:\Users\patha\PyCharmMiscProject\rand10000.txt",
    "rand100000": r"C:\Users\patha\PyCharmMiscProject\rand100000.txt",
    "rand250000": r"C:\Users\patha\PyCharmMiscProject\rand250000.txt",
    "rand500000": r"C:\Users\patha\PyCharmMiscProject\rand500000.txt",
    "rand1000000": r"C:\Users\patha\PyCharmMiscProject\rand1000000.txt"
}

datasets = {}
for name, path in file_paths.items():
    try:
        with open(path, "r") as file:
            datasets[name] = np.array(list(map(int,file.read().split())))
    except Exception as e:
        print(f"Error reading {file}: {e}")

#Measure Execution time using the time eff function from Hw 1

results = []
for name, data in datasets.items():
    print(f"Running {name}...")

    #Measure Insertion Sort

    insertion_time = timeEfficiency(insertion_sort, data.copy())

    #Measure Merge sort
    merge_time = timeEfficiency(merge_sort, data.copy())

    results.append([name, len(data), insertion_time, merge_time])

#Display
df_results = pd.DataFrame(results, columns=["Dataset", "Size", "Insertion Sort time(s)", "Merge Sort Time(s)"])
print(df_results)
df_results.to_csv("sorting_results.csv", index=False)

#%%
#Question 2-2: Count the total number of comparisons for completion of each sorting algorithm
# And Question 2-3: Record execution time with each data size and display graphical results
#Updating Question 2-1 code
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
merge_comparisons = 0 #Global Var: Count comparisons in Merge Sort
#Modified Insertion Sort for Comparisons
def insertion_sort_comparison(arr):
    comparisons = 0 #Comparison Counter
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            comparisons += 1 #Increment each comparison
        arr[j+1] = key
        comparisons += 1  #Last comparison where while loop is
    return comparisons
#Modified Merge Sort for Comparisons
def merge_sort_comparison(arr):
    global merge_comparisons

    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_comparison(left_half)
        merge_sort_comparison(right_half)


        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            merge_comparisons += 1  #Counting Cmp
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr #Return sorted array

#Copy first from 2-1
results_with_comparisons = []
for name, data in datasets.items():
    print(f"Running {name}...")

    #Measure Insertion Sort only for small addresses
    
    insertion_comparisons = insertion_sort_comparison(data.copy()) #Number of comparisons
    insertion_time = timeEfficiency(insertion_sort, data.copy())

    #Measure Merge sort
    global merge_comparisons
    merge_comparisons = 0 #Reset counter
    merge_time = timeEfficiency(merge_sort_comparison, data.copy())

    results_with_comparisons.append([name, len(data), insertion_time, merge_time, insertion_comparisons, merge_comparisons])

#Display
df_comparisons = pd.DataFrame(results_with_comparisons, columns=["Dataset", "Size", "Insertion Sort time(s)", "Merge Sort Time(s)", "Insertion Sort Comparisons", "Merge Sort Comparisons"])
print(df_comparisons)
# Ensure column names match throughout the code
column_names = ["Dataset", "Size", "Insertion Sort Time (s)", "Merge Sort Time (s)",
                "Insertion Sort Comparisons", "Merge Sort Comparisons"]

# Ensure DataFrame uses correct column names
df_comparisons = pd.DataFrame(results_with_comparisons, columns=column_names)

# Convert "Too Slow" to None for graphing
df_comparisons.replace("Too Slow", None, inplace=True)

# Convert numerical columns to float (Matplotlib requires numeric data)
df_comparisons["Insertion Sort Time (s)"] = pd.to_numeric(df_comparisons["Insertion Sort Time (s)"], errors='coerce')
df_comparisons["Merge Sort Time (s)"] = pd.to_numeric(df_comparisons["Merge Sort Time (s)"], errors='coerce')
df_comparisons["Insertion Sort Comparisons"] = pd.to_numeric(df_comparisons["Insertion Sort Comparisons"], errors='coerce')
df_comparisons["Merge Sort Comparisons"] = pd.to_numeric(df_comparisons["Merge Sort Comparisons"], errors='coerce')
df_comparisons["Size (millions)"] = df_comparisons["Size"] / 1_000_000

#plot Execution Time Comparison

plt.figure(figsize=(10, 5))
plt.plot(df_comparisons["Size (millions)"], df_comparisons["Insertion Sort Time (s)"], label="Insertion Sort",
marker='o', linestyle='dashed', color='red')
plt.plot(df_comparisons["Size (millions)"], df_comparisons["Merge Sort Time (s)"], label="Merge Sort",
marker='o', linestyle='solid', color='blue')
plt.xlabel("Dataset Size (millions)")
plt.ylabel("Execution Time (seconds)")
plt.xticks(df_comparisons["Size (millions)"], rotation=45, fontsize=10)  # Rotate x-axis (visibility)
plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%.2f'))  # Format labels to two decimal places
plt.title("Sorting Algorithm Execution Time Comparison")
plt.legend()
plt.grid(True, linestyle='dotted', alpha=0.6)
plt.show()

#plot Comparison Count Comparison

plt.figure(figsize=(10, 5))
plt.plot(df_comparisons["Size (millions)"], df_comparisons["Insertion Sort Comparisons"],
label="Insertion Sort Comparisons", marker='o', linestyle='dashed', color='red')
plt.plot(df_comparisons["Size (millions)"], df_comparisons["Merge Sort Comparisons"],
label="Merge Sort Comparisons", marker='o', linestyle='solid', color='blue')
plt.xlabel("Dataset Size (millions)")
plt.ylabel("Number of Comparisons")
plt.xticks(df_comparisons["Size (millions)"], rotation=45, fontsize=10)  # Rotate x-axis (visibility)
plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%.2f'))  # Format labels to two decimal places
plt.title("Sorting Algorithm Comparison Count")
plt.legend()
plt.grid(True, linestyle='dotted', alpha=0.6)
plt.show()
