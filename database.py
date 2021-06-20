import datetime

class NEODatabase:

    def __init__(self, neos, approaches):
  
   
        self.approaches = approaches

        self._neos = {neo.designation: neo for neo in neos}
        self._name_to_des = {neo.name: neo.designation for neo in neos}
        self._approaches = {}
        for approach in approaches:
            if self._approaches.get(approach.designation, None):
                self._approaches[approach.designation].append(approach)
            else:
                self._approaches[approach.designation] = [approach]
            for a in self._approaches[approach.designation]:
                a.neo = self._neos[approach.designation]
            self._neos[approach.designation].approaches.append(approach) 
        
        
        #self._neos = neos
        #self._approaches = approaches
        #for neo in self._neos:
            #for approach in self._approaches: # going through all instances
                #if neo.designation == approach._designation: # linking neos to approachs via their designation
                    #neo.approaches.append(approach) # adding the approach information to the list of the neo instance, for every neo there might be more than one close approach, therefore it is a list
                    
                    #approach.neo = neo.name # adding the neo information to the approach instance
                    #print(approach.neo)              

    def get_neo_by_designation(self, designation):
     
        return self._neos.get(designation.upper(), None)       

    
    def get_neo_by_name(self, name):
      
        designation = self._name_to_des.get(name.capitalize(), None)
        if designation:
            return self.get_neo_by_designation(designation)
        return None

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaninfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        # TODO: Generate `CloseApproach` objects that match all of the filters.
        for approach in self._approaches:
            if approach.time.date() == filters['date']:
                continue
            if approach.time.date() <= filters['end_date']:
                continue
            if approach.time.date() >= filters['start_date']:
                continue
            if approach.distance >= filters['distance_min']:
                continue
            if approach.distance <= filters['distance_max']:
                continue
            if approach.velocity <= filters['velocity_max']:
                continue
            if approach.velocity >= filters['velocity_min']:
                continue
            if approach.neo.hazardous == filters['hazardous']:
                continue
            yield approach
