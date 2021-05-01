"""
https://www.algoexpert.io/questions/Class%20Photos
"""


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if len(redShirtHeights) != len(blueShirtHeights):
        return False

    first_tallest_student = max(redShirtHeights[0], blueShirtHeights[0])
    students = arrange_students_in_rows(
        redShirtHeights, blueShirtHeights, first_tallest_student
    )
    back_row, front_row = students[0], students[1]

    for i, height in enumerate(back_row):
        invalid_height = back_row[i] <= front_row[i]

        if invalid_height:
            return False
    return True


def arrange_students_in_rows(redShirtHeights, blueShirtHeights, first_tallest_student):
    first_tallest_student = max(redShirtHeights[0], blueShirtHeights[0])
    if first_tallest_student == blueShirtHeights[0]:
        back_row = blueShirtHeights
        front_row = redShirtHeights
    else:
        back_row = redShirtHeights
        front_row = blueShirtHeights
    return back_row, front_row
