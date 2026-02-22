def get_top_student(classroom):
    if not classroom.students:
        return None
    return max(classroom.students, key=lambda s: s.average())


def get_low_student(classroom):
    if not classroom.students:
        return None
    return min(classroom.students, key=lambda s: s.average())


def get_ranking(classroom):
    return sorted(classroom.students, key=lambda s: s.average(), reverse=True)


def get_grade_count(classroom):
    result = {}
    for s in classroom.students:
        cat = s.grade_category()
        if cat not in result:
            result[cat] = 0
        result[cat] += 1
    return result