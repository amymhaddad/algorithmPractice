"""
https://www.algoexpert.io/questions/Class%20Photos
"""

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if len(redShirtHeights) != len(blueShirtHeights):
        return False

    taller_student = max(redShirtHeights[0], blueShirtHeights[0])
    if taller_student in blueShirtHeights:
        back_row = blueShirtHeights
        front_row = redShirtHeights
    else:
        back_row = redShirtHeights
        front_row = blueShirtHeights

    #import pdb; pdb.set_trace()
    for i, height in enumerate(back_row):
        invalid_height = back_row[i] <= front_row[i]

        if invalid_height:
            return False
    return True

redShirtHeights = [6, 9, 2, 4, 5, 1]
blueShirtHeights = [5, 8, 1, 3, 4, 9]

print(classPhotos(redShirtHeights, blueShirtHeights))
