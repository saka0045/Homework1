"""
This script parses the output file created by burst.
The script requires the output.txt and query.fna to be in the same directory as this script.

Discussed homework with Jeannette Rustin
"""

__author__ = "Yuta Sakai"

# Open files, make sure the following files are in the same directory as this script
query_file = open("./query.fna", "r")
output_file = open("./output.txt", "r")

# Count how many queries were in the query.fna file (or you can just look at the stdout from running burst...)
query_count = 0
for line in query_file:
    if line.startswith(">"):
        query_count += 1

print("Total queries: " + str(query_count))

# Parse out the output.txt file
total_percent = 0
line_count = 0
query_above_ninety_seven = 0
species_dict = {}
for line in output_file:
    line = line.rstrip()
    line_item = line.split("\t")
    percent_match = float(line_item[2])
    # Keep track of the total percent to calculate the average percent similarity
    total_percent += percent_match
    line_count += 1
    taxonomy = line_item[12]
    # Count the queries with greater than or equal to 97% match
    if percent_match >= 97:
        query_above_ninety_seven += 1
    # Extract the species information out of taxonomy
    species = taxonomy.split(";")[6]
    # Skip if species information is empty
    if species == "s__":
        continue
    else:
        # Make hash table of different species
        if species not in species_dict.keys():
            species_dict[species] = 1
        else:
            species_dict[species] += 1

print("Queries with greater than or equal to 97% match is: " + str(query_above_ninety_seven))

# Calculate the fraction of queries with greater than or equal to 97% match
fraction_about_ninety_seven = query_above_ninety_seven / query_count
print("Fraction of queries with greater than or above 97% match is: " + str(fraction_about_ninety_seven))

# Print out the results of species hash table and the most common species
print(species_dict)
most_common_species = max(species_dict, key=species_dict.get)
print("The most common bacterial species in the query set is: " + most_common_species[3:] \
      + " at " + str(species_dict[most_common_species]) + " hits")

# Calculate the average percent similarity
average_percent_similarity = total_percent / line_count
print("Average percent similarity is: " + str(average_percent_similarity))

query_file.close()
output_file.close()
