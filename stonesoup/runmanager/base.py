
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

from ..base import Base
from stonesoup.types.array import StateVector
from stonesoup.platform import base
from stonesoup.tracker.base import Tracker
from stonesoup.platform.base import Platform
from typing import Sequence

class RunManager(Base):
    "Base run manager class"


    platforms: Sequence[Platform]
    platforms_min_range: Sequence[Platform]
    platforms_max_range: Sequence[Platform]
    platforms_step: Sequence[Platform]

    def __init__(self):
        #Tracker
        self.tracker:Tracker
        self.tracker_min:Tracker
        self.tracker_max:Tracker
        self.tracker_step:Tracker
        
        self.state_vectors=[]
        self.state_vector_min_range=[]
        self.state_vector_max_range=[]
        self.state_vector_step=[]
        
        self.covar=[]
        self.covar_min_range=[]
        self.covar_max_range=[]
        self.covar_step=[]

        self.number_particles=[]
        self.number_particles_min_range=0
        self.number_particles_max_range=0
        self.number_particles_step=0

        #Deleter
        self.time_steps_since_update=[]
        self.time_steps_since_update_min_range=0
        self.time_steps_since_update_max_range=0
        self.time_steps_since_update_step=0

       