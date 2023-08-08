#You are given a list of students, each represented as a
#dictionary with the following attributes: name, age, and gpa.
#Your task is to sort the list of students based on their GPA
#in descending order using the Insertion Sort algorithm.

#Example of a student dictionary:

#students = [

#{"name": "Alice", "age": 20, "gpa": 3.9},

#{"name": "Bob", "age": 22, "gpa": 3.7},

#{"name": "Charlie", "age": 21, "gpa": 4.0},

#{"name": "David", "age": 19, "gpa": 3.5},

#]

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key["gpa"] < arr[j]["gpa"]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        
#test
        
def main():
    
    
    students = [
        
        {"name": "Alice", "age": 20, "gpa": 3.9},

        {"name": "Bob", "age": 22, "gpa": 3.7},

        {"name": "Charlie", "age": 21, "gpa": 4.0},

        {"name": "David", "age": 19, "gpa": 3.5},

               ]
    print("Original students:")
    for i in students:
        print(i)
    print("__________________________________________")
        
    print("Sorted students:")
    for i in students:
        print(i)
        insertion_sort(students)
        
    
main()
    

    
    
