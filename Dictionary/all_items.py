# 1.Use a for loop to iterate through the items of pct_women_in_occupation. For each key : value pair, print out a string that looks like:
# Women make up [value] percent of [key]s.

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9,
                           "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, value in pct_women_in_occupation.items():
    print("Women make up "+str(value)+" percent of "+occupation+"s.")
