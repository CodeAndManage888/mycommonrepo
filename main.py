import itertools
import random

# Define possible first data options
first_data_options = ["H&PS", "PRD", "CMT", "RES", "FS"]

# Function to generate all possible distributions of 100% across `n` items with a given step size
def all_distributions(n, step):
    if n == 1:
        return [[100]]
    distributions = []
    for i in range(0, 101, step):
        for sub_distribution in all_distributions(n - 1, step):
            if sum(sub_distribution) + i <= 100:
                distributions.append([i] + sub_distribution)
    return distributions

# Generate distributions with a smaller step size to create more variety
distributions_025 = all_distributions(4, 10)  # Step size of 10 for more options
distributions_008_007_006 = all_distributions(14, 20)  # Larger step size for manageability

# Function to create test data ensuring each category is covered and creating at least 1000 records
def generate_test_data(min_records):
    samples = []
    # Randomly sample from the distributions to increase variety
    while len(samples) < min_records:
        for fd in first_data_options:
            for dist_025 in random.sample(distributions_025, min(len(distributions_025), 20)):  # Sample 20 distributions
                for dist_008_007_006 in random.sample(distributions_008_007_006, min(len(distributions_008_007_006), 5)):  # Sample 5 distributions
                    combined = f"{fd}/" + "/".join(map(lambda x: f"{x:03}", dist_025)) + "/" + "/".join(map(lambda x: f"{x:03}", dist_008_007_006))
                    samples.append(combined)
                    if len(samples) >= min_records:
                        return samples
    return samples

# Generate the test data
test_data = generate_test_data(1000)

# Optionally, print or save the generated data
for data in test_data[:5]:  # Printing first 5 for brevity
    print(data)

# Save the data to a file
with open('test_data.txt', 'w') as f:
    for data in test_data:
        f.write(data + '\n')
