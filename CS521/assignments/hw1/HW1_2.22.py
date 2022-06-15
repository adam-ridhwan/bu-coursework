# user_input is defined to ask user to input number of years
user_input = input("Enter the number of years: ")

# seconds_in_a_year is defined to calculate the number of seconds in a year
seconds_in_a_year = 365 * 24 * 60 * 60

# current_population is defined with given number
current_population = 312032486

# births_per_year is defined to calculate the births per year
births_per_year = seconds_in_a_year / 7 

# deaths_per_year is defined to calculate the deaths per year
deaths_per_year = seconds_in_a_year / 13

# immigrants_per_year is defined to calculate the immigrants per year
immigrants_per_year = seconds_in_a_year / 45 

# rate_per_year is defined to calculated the rate per year with results from births_per_year, deaths_per_year & immigrants_per_year
rate_per_year = births_per_year - deaths_per_year + immigrants_per_year 

# five_years is defined to calculate the number result after 5 years
five_years = str(int(current_population) + (int(user_input) * rate_per_year)) 

# five_years_rounded is defined to round to a whole number
five_years_rounded = round(float(five_years))

# prints result
print("The population in " + user_input + " years is " + str(five_years_rounded))