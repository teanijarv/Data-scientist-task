import random
from math import sqrt

random.seed(1)  # Setting random number generator seed for repeatability
NUM_NEURONS = 10000
NERVE_SIZE = 128000  # nanometers
CONFLICT_RADIUS = 500  # nanometers


def check_for_conflicts(nerves, conflict_radius):
    conflicted_neurons = []
    # Loop that goes through each neuron
    for i in range(NUM_NEURONS):
        print("Inspecting neuron", str(i), "of", str(NUM_NEURONS))
        # Calculating Euclidean distance for that neuron with all the other neurons
        euc_dis = [sqrt((nerves[i][0] - nerves[j][0]) ** 2 + (nerves[i][1] - nerves[j][1]) ** 2) for j in range(NUM_NEURONS)]
        # Check all the distances, find the ones which are too close and add them to conflicted neurons list
        for idx in range(0, NUM_NEURONS):
            if 0 < euc_dis[idx] <= conflict_radius:
                conflicted_neurons.append(idx)
                print("Neuron", str(i), "has a conflict with neuron", str(idx))
    # Find only unique values from the list, thereby removing duplicates
    conflicted_neurons = len(list(set(conflicted_neurons)))
    return conflicted_neurons


def gen_coord():
    # DO NOT MODIFY THIS FUNCTION
    return int(random.random() * NERVE_SIZE)


if __name__ == '__main__':
    neuron_positions = [[gen_coord(), gen_coord()] for i in range(NUM_NEURONS)]
    n_conflicts = check_for_conflicts(neuron_positions, CONFLICT_RADIUS)
    print("Neurons in conflict : {}".format(n_conflicts))

