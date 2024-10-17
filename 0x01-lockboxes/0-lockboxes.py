<<<<<<< HEAD
#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ LockBoxes Function """
    T = []
    for i in range(1, len(boxes)):
        order = [T.extend(x) for x in boxes[:i] + boxes[i + 1:]]
        if i in T:
            T = []
        else:
            return False
    return True
=======
#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
>>>>>>> 40f5566b860acef23723adbac39a19b796dcad84
