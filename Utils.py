"""
Utils.py

It will be used to store helper functions that do not belong to any specific class, for both code organization and project documentation.
"""
def map_value (current_min, current_max, new_min, new_max, value):
    current_range = current_max - current_min
    new_range = new_max - new_min
    return new_min + new_range * ((value - current_min) / current_range)