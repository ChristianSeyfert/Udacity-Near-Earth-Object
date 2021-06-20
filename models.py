
from helpers import cd_to_datetime, datetime_to_str
import datetime


class NearEarthObject:

    """ Names have been changed"""
    
    def __init__(self, designation, name, is_neo, hazardous, diameter):
    
 
        self.name = name

        self.designation = designation
        assert isinstance(self.designation, str)
        if is_neo == 'Y':
            self.is_neo = True
        else:
            self.is_neo = False
        
        if hazardous == 'Y':
            self.hazardous = True
        else:
            self.hazardous = False
        
        if diameter != None:
            self.diameter = float(diameter)
        else:
            self.diameter = float("nan")
        assert isinstance(self.diameter, float)
        
        self.approaches = []

    @property
    def fullname(self):
        self.fullname = str(self.designation) + self.name
        return ''

    def __str__(self):
        return f"The object {self.name} has a diameter of {self.diameter} km and is hazardous = {self.hazardous}."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
  
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation, time_of_close_approach, nominal_approach_distance, v_rel):
        """Names have been changed"""

 
        self._designation = designation
        assert isinstance(self._designation, str)
        self.time = cd_to_datetime(time_of_close_approach)
        assert isinstance(self.time, datetime.datetime)
        self.distance = float(nominal_approach_distance)
        assert isinstance(self.distance, float)
        self.velocity = float(v_rel)
        assert isinstance(self.velocity, float)
        
        """What to do here?"""
        self.neo = None

    @property
    def time_str(self):
        return datetime_to_str(self.time)
    
    @property
    def designation(self):
        return self._designation
    
    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        return f"The object {self._designation} passed Earth on {self.time} with {self.velocity} km/s at a distance of {self.distance} km."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
