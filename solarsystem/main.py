#!/usr/bin/python

import glob
import numpy as np
import ipdb
import scipy.spatial.distance as ssd

import parser


class Universe:

    G = 6.67408e-11

    def __init__(self, positions, velocities, masses):
        self.positions = positions
        self.velocities = velocities
        self.accelerations = np.zeros(self.velocities.shape)
        self.accelerations_new = np.zeros(self.velocities.shape)
        self.masses = masses
        self.counter = 0

    def verlet(self, dt):
        self.positions += self.velocities*dt + 0.5*acc*dt*dt
        self.get_forces(self.positions, self.accelerations_new)
        self.velocities += (self.accelerations+self.accelerations_new)/2*dt
        self.accelerations = self.accelerations_new
        
    def get_forces(self, positions, accelerations):
        for i in xrange(accmat.shape[0]):
            for j in xrange(accmat.shape[0]):
                diffvec = self.positions[i]-self.positions[j]
                accelerations[i] += G * self.masses[i] * self.masses[j] / np.dot(diffvec, diffvec)**1.5 * diffvec
                
    def print_positions(self):
        print self.positions.shape[0]
        print "Counter:", counter
        for pos in positions:
            print " ".join(map(str, pos))
            

def main(*args):
    fnames = glob.glob("SolSysDyn/*.txt")
    positions, velocities, masses = [], [], []
    for fname in fnames:
        print fname
        pos, vel = parser.get_coordinates_velocities(fname)
        positions.append(pos)
        velocities.append(vel)
        masses.append(parser.get_masses(fname))
    positions = np.array(positions)
    velocities = np.array(velocities)
    ipdb.set_trace()
    masses = np.array(masses)
    universe = Universe(positions, velocities, masses)
    universe.get_forces(universe.positions)
     
if __name__ == "__main__":
    main()
