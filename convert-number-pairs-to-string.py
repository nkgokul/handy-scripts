# Input list of pairs
pairs = [
    (1, 3),
    (2, 3),
    (3, 5),
    (3, 6),
    (3, 7),
    (3, 8),
    (3, 9),
    (3, 10),
    (3, 11),
    (3, 12)
]

# Convert each pair to the sXpY format
formatted = [f"s{a}p{b}" for a, b in pairs]

# Join them into a comma-separated string
result = ",".join(formatted)

# Output the result
print(result)
