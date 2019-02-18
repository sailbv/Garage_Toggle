''' 
garage_toggle.py

        Garage Toggle manages automatic closing of a garage given certain conditions
        The main problem it's to solve is when a garage is left open.
        A first goal is to have the system use TIME to determine if the garage should be closed and 
        sends signals to close it
'''
from gpiozero import *


class Garage:
	''' Defines a garage and it's own options-- how long to remain open can be individualized
 and also holds which pins are defined for inputs and outputs '''
	def __init__(self, input, options, **kwargs):
		self.inputs = inputs
		self.time_open = kwargs[time_open]
		self.options = options


def GarageState(*state):
        ''' maintains state on garage Open or Close'''
        return GarageState

def closeGarage(garage):
        ''' sends signals to close garage'''
        if GARAGE_IS_OPEN and toggleState():
                return GARAGE_CLOSE
        else:
                return GARAGESTATE
