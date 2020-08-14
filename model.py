from pomegranate import *

# Defining the knowledge that we already know
start = DiscreteDistribution({
    'sun': 0.5,  # Probability of being sunny is 0.5
    'rain': 0.5  # probability of rain is 0.5
})

# Defining transitions
transitions = ConditionalProbabilityTable([
    ['sun', 'sun', 0.8],
    ['sun', 'rain', 0.2],
    ['rain', 'sun', 0.3],
    ['rain', 'rain', 0.7]
], [start])

# Creating the model
model = MarkovChain([start, transitions])

# Sampling the model and then printing
print(model.sample(50))
