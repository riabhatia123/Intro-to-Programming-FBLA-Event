# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 16:54:37 2024

@author: Ria Bhatia
"""
#function to return GPA points based on the grade that user inputs
def gpa_dict_number(grade):
    #Assign GPA points based on the input grade
    if "A+" == grade:
        return 4.0
    if "A" == grade:
        return 3.8
    if "A-" == grade:
        return 3.6
    if "B+" == grade:
        return 3.4
    if "B" == grade:
        return 3.2
    if "B-" == grade:
        return 3.0
    if "C+" == grade:
        return 2.7
    if "C" == grade:
        return 2.4
    if "C-" == grade:
        return 2.0
    if "D+" == grade:
        return 1.7
    if "D" == grade:
        return 1.4
    if "F" == grade:
        return 0
    if "I" == grade:
        return 0
    if "P" == grade:
        return 0
        
    
#Function to calculate unweighted GPA
def calculate_unweighted_gpa(num_classes):
    #Initialize total GPA points 
    total_points = 0
    
    #Will ask for each class grade for the amount of classes given
    for _ in range(num_classes):
        #Prompts the user to input letter grade for unweighted calculation
        grade = input("Enter your letter grade for unweighted calculation: ")
        #Add GPA points based on the grade
        total_points += gpa_dict_number(grade)
   #calculate unweighted GPA by dividing total points by number of classes
    return total_points / num_classes

#Function to calculate weighted GPA
def calculate_weighted_gpa(num_classes):
   #initalize total weighted points and total GPA points
    total_weighted_points = 0
    total_weight = 0
    for _ in range(num_classes):
       #prompt user to input letter grade and class weight for weighted calculation
        grade = input("Enter your letter for weighted calculation: ")
        weight = float(input("Enter the class weight (e.g., 1.4 for AP, 1.0 for full regular year course and 0.5 for half year/phys. ed/health): "))
       #Find weighted GPA points by muliplying grade points with weight
        total_weighted_points += gpa_dict_number(grade) * weight
        total_weight += weight
        #Calculate weighted GPA by dividing total weighted grade points by total weight points
    return total_weighted_points / total_weight

def main():
    #Ask user for the number of classes and type of GPA calculations
    num_classes = int(input("Hello, welcome to your personal GPA calculator. How many classes are you taking?: "))
    choice = input("Do you want to calculate 'weighted', 'unweighted', or 'both' GPAs?: ").lower()
    
  #Perform selected type of GPA Calculation based off user input
    if choice == 'weighted':
        weighted_gpa = calculate_weighted_gpa(num_classes)
        print(f"Your weighted GPA is: {weighted_gpa:.2f}")
    elif choice == 'unweighted':
        unweighted_gpa = calculate_unweighted_gpa(num_classes)
        print(f"Your unweighted GPA is: {unweighted_gpa:.2f}")
    #Calculate both unweighted and weighted GPAS
    elif choice == 'both':
        unweighted_gpa = calculate_unweighted_gpa(num_classes)
        print(f"Your unweighted GPA is: {unweighted_gpa:.2f}")
        weighted_gpa = calculate_weighted_gpa(num_classes)
        print(f"Your weighted GPA is: {weighted_gpa:.2f}")
    #Handle invalid input
    else:
        print("Invalid choice. Please restart the program and choose either 'weighted', 'unweighted', or 'both'.")

if __name__ == "__main__":
    main()

