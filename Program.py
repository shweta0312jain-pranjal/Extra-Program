import numpy as np

np.random.seed(42)

minutes = int(input("Enter the total no. of minutes observed: "))
traffic_prob = float(input("Enter the probability of car passing in a minute (between 0 and 1): "))
sample_size = int(input("Enter the number of samples to generate: "))

traffic = np.random.choice([0, 1], minutes, p=[1 - traffic_prob, traffic_prob])

print("\nActual traffic density:", traffic.mean())

samples = np.array([np.random.choice(traffic, sample_size).mean() for _ in range(5000)])
print("Estimated traffic density from samples:", samples.mean())
print("Standard deviation of the estimates:", samples.std())

cars_per_hour = samples.mean() * 60
print("Estimated Cars per hour:", int(cars_per_hour))