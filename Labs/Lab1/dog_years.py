# dog_years.py

# Lab1: This python script converts human years into dog years

# Author: Anders Grahn
# Date: 2024-01-19

# Adds dog years for each human year
def calculate_dog_years(human_years):

    # Dog specific years
    first_two_dog_years_equals = 10.5
    adult_dog_years = 4

    # Keep track of how many dog years
    dog_years = 0;
    year_index = 1;

    # Go throught all the years and add dog years to each year
    while year_index <= human_years:
        # First we check if the dog is in its first two young years
        if(year_index <=2):
            dog_years = dog_years + first_two_dog_years_equals
        # The dog has reached adulthood so add ordinary dog years
        else:
            dog_years = dog_years + adult_dog_years

        year_index += 1

    return dog_years
