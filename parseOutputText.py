# Parses out the output file created by burst

# Open files
query_file = open("./query.fna", "r")
output_file = open("./output.txt", "r")

# Count how many queries were in the query.fna file (or you can just look at the stdout from running burst...)
query_count = 0
for line in query_file:
    if line.startswith(">"):
        query_count += 1

print("Total queries: " + str(query_count))

# Count how many queries have match greater than or equal to 97% and collect taxonomy info
query_above_ninety_seven = 0
species_dict = {}
for line in output_file:
    line = line.rstrip()
    line_item = line.split("\t")
    percent_match = float(line_item[2])
    taxonomy = line_item[12]
    # Count the queries with greater than or equal to 97% match
    if percent_match >= 97:
        query_above_ninety_seven += 1
    # Extract the species information out of taxonomy
    species = taxonomy.split(";")[6]
    # Make hash table of different species
    if species not in species_dict.keys():
        species_dict[species] = 1
    else:
        species_dict[species] += 1

print("Queries with greater than or equal to 97% match is: " + str(query_above_ninety_seven))

# Calculate the fraction of queries with greater than or equal to 97% match
fraction_about_ninety_seven = query_above_ninety_seven / query_count
print("Fraction of queries with greater than or above 97% match is: " + str(fraction_about_ninety_seven))

# Print out the results of species hash table
print(species_dict)

query_file.close()
output_file.close()
