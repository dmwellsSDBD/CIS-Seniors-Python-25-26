'''
File Name: college_tracker.py
Author: Elijah Snyder
Date: 10/24/2025
'''
# Import statemenets
import math

# Constants
APPLICATION_FEE = 75.00
AVG_ACCEPTANCE_RATE = 55.0
MAX_IDEAL_DISTANCE = 500

# Lists
colleges = []
locations = []
annual_tuitions = []
distances = []
acceptance_rates = []
classifications = []

# Welcome message
print("=" * 30)
print("COLLEGE APPLICATION TRACKER")
print("=" * 30)
print("Track your college applications and analyze your options!")
print("=" * 30)
print("")


# Inputs
person = str(input("What is your name? "))
print(f"\nWelcome, {person}! Let's track your college applications.")
print("")

print("Please enter information for 3 colleges you're considering:")
print("")

# College 1 Inputs
print("--- College #1 ---")
college = input("College Name: ")
location = input("Location (City, State): ")
annual_tuition = float(input("Anuual Tuition ($): "))
distance = int(input("Distance from home (miles): "))
acceptance_rate = float(input("Acceptance Rate (%): "))

if acceptance_rate >= AVG_ACCEPTANCE_RATE:
    classification = "safety"

elif acceptance_rate < AVG_ACCEPTANCE_RATE and acceptance_rate > 50.0:
    classification = "match"

elif acceptance_rate < AVG_ACCEPTANCE_RATE:
    classification = "Reach"

print("")

# Appending to lists
colleges.append(college)
locations.append(location)
annual_tuitions.append(annual_tuition)
distances.append(distance)
acceptance_rates.append(acceptance_rates)
classifications.append(classification)

# College 2 Inputs
print("\n--- College #2 ---")
college = input("College Name: ")
location = input("Location (City, State): ")
annual_tuition = float(input("Anuual Tuition ($): "))
distance = int(input("Distance from home (miles): "))
acceptance_rate = float(input("Acceptance Rate (%): "))

if acceptance_rate >= AVG_ACCEPTANCE_RATE:
    classification = "safety"

elif acceptance_rate < AVG_ACCEPTANCE_RATE and acceptance_rate > 50.0:
    classification = "match"

elif acceptance_rate < AVG_ACCEPTANCE_RATE:
    classification = "Reach"

colleges.append(college)
locations.append(location)
annual_tuitions.append(annual_tuition)
distances.append(distance)
acceptance_rates.append(acceptance_rate)
classifications.append(classification)

# College 3 Inputs
print("\n--- College #3 ---")
college = input("College Name: ")
location = input("Location (City, State): ")
annual_tuition = float(input("Anuual Tuition ($): "))
distance = int(input("Distance from home (miles): "))
acceptance_rate = float(input("Acceptance Rate (%): "))

if acceptance_rate >= AVG_ACCEPTANCE_RATE:
    classification = "safety"

elif acceptance_rate < AVG_ACCEPTANCE_RATE and acceptance_rate > 50.0:
    classification = "match"

elif acceptance_rate < AVG_ACCEPTANCE_RATE:
    classification = "Reach"

colleges.append(college)
locations.append(location)
annual_tuitions.append(annual_tuition)
distances.append(distance)
acceptance_rates.append(acceptance_rate)
classifications.append(classification)


# College Application Summary
print("\n\n")
print("=" * 30)
print("YOUR COLLEGE APPLICATION SUMMARY")
print("=" * 30)
print("")

print(f"College1: {colleges[0]}")
print(f"Location: {locations[0]}")
print(f"Annual Tuition: {annual_tuitions[0]:.2f}")
print(f"Classification: {classifications[0]}")
four_year_total = annual_tuition[0] * 4
print(f"4-Year Total Cost: ${four_year_total:.2f}")
print("")

print(f"College1: {colleges[1]}")
print(f"Location: {locations[1]}")
print(f"Annual Tuition: {annual_tuitions[1]:.2f}")
print(f"Classification: {classifications[1]}")
four_year_total = annual_tuitions[1] * 4
print(f"4-Year Total Cost: ${four_year_total:.2f}")
print("")

print(f"College1: {colleges[2]}")
print(f"Location: {locations[2]}")
print(f"Annual Tuition: {annual_tuitions[2]:.2f}")
print(f"Classification: {classifications[2]}")
four_year_total = annual_tuitions[2] * 4
print(f"4-Year Total Cost: ${four_year_total:.2f}")