#!/usr/bin/python

import glob
import numpy as np
import ipdb

import parser


def verlet(pos, vel, acc, acc_new, dt):
    pos += vel*dt + 0.5*acc*dt*dt
    vel += (acc_old+acc_new)/2*dt

def main(*args):
    fnames = glob.glob("SolSysDyn/*.txt")
    positions, velocities = [], []
    for fname in fnames:
        print fname
        pos, vel = parser.get_coordinates_velocities(fname)
        positions.append(pos)
        velocities.append(vel)
    positions = np.array(positions)
    velocities = np.array(velocities)
    ipdb.set_trace()
    
if __name__ == "__main__":
    main()
