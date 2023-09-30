

def paste_component(entity):
    """
    This method returns a component with a direct copy of an entity
    Input:
        - entity: list with the entity
    Return:
        - output: string with entity inside
    """
    output = "\n"
    for i in entity:
        output += i + "\n"
    
    return output


def max_length( input, split="True", ftext="", etext="", pos=0):
        """
        This method calculates the length of a list
        Input:
            - input: list of list values
            - split: flag with split option
            - ftext: previous string
            - etext: forward string
        Return:
            - lon_max: integer with the maximum length
        """
        lon_max = 0
        for var in input:
            lon = 0
            if type(var[pos]) is list:   # if list is nested
                cont = 1
                for nested in var[pos]:
                    if split == "True":
                        lon = len(nested) + len(ftext) + len(etext)
                        lon_max = max(lon, lon_max)
                    else:
                        lon += len(nested) + len(ftext) + len(etext)
                        if cont != len(var[pos]):
                            lon += 2
                        cont += 1
            else:
                lon = len(var[pos]) + len(ftext) + len(etext)
            
            lon_max = max(lon, lon_max)

        return lon_max