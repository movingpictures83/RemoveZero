# RemoveZero
# Language: Python
# Input: CSV 
# Output: CSV
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin to take a CSV file (rows samples, columns entities)
and remove all entities that have zero abundances in all samples.

The input CSV file is assumed to be in matrix format, with element (i, j)
corresponding to the abundance of element j in sample i.

Output CSV will be in this same format.
