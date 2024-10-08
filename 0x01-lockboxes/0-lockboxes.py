#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list where each index represents a box,
                                     and the value at that index is a list of keys
                                     available inside that box.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    
    The function starts with the first box (index 0) being unlocked.
    It then uses the keys inside that box to try and unlock other boxes.
    The process continues by collecting keys from newly unlocked boxes until
    all boxes are either unlocked or no more keys are available.
    """
    # Start with all boxes locked, except for the first box
    unlocked = [False] * len(boxes)
    unlocked[0] = True  # Box 0 is always unlocked
    
    # List of keys we currently possess (initially keys from box 0)
    keys = boxes[0]
    
    # Set to keep track of opened boxes (initially only box 0 is opened)
    opened = set([0])
    
    # Continue unlocking boxes while there are keys to try
    while keys:
        key = keys.pop(0)
        if key < len(boxes) and key not in opened:
            unlocked[key] = True  # Mark the box as unlocked
            opened.add(key)  # Add this box to the set of opened boxes
            # Add keys from the newly unlocked box to the list of keys
            keys.extend(boxes[key])
    
    # Return True if all boxes are unlocked, otherwise False
    return all(unlocked)
