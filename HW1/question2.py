def compare_subjects_within_student(
    subj1_all_students,
    subj2_all_students
):
    """Compare the two subjects with their students and print out the higher-graded subject for each student.
    Single-subject students shouldn't be printed.
    Parameters
    ----------
    subj1_all_students, subj2_all_students
        Data structures which contain the grades of all students in a given subject.
    Notes
    -----
    Choice for the data structure of the function's arguments is up to you.
    Returns
    -------
    A data structure with the name of the student and the corresponding subject.
    """
    # Your code goes here...
    table={}
    for x in subj1_all_students.keys():
        if x=='name':
            continue
        for y in subj2_all_students.keys():
            if y=='name':
                continue
            if x==y:
                if (max(subj1_all_students[x][1],subj1_all_students[x][2])>max(subj2_all_students[y][1],subj2_all_students[y][2])):
                    table[x]=(subj1_all_students["name"])
                else:
                    table[y]=(subj2_all_students["name"])

    return table
 

History = {
        'name': 'History',
        'efrat': {1 : 85, 2: 90}, 
        'yotam': {1: 70, 2: 50},
        'yael': {1:50, 2:100},
        'yam': {1:90, 2:30}
}
Math= {
        'name': 'Math',
        'yotam': {1 : 70, 2: 50}, 
        'efrat': {1: 50, 2: 100},
        'yael': {1:85, 2:90},
        'gal': {1:75, 2:80}
}
print(compare_subjects_within_student(History,Math))
