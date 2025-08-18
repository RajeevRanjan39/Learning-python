def get_roll_nos(data:list, criteria=None):
    '''
    Filter roll numbers based on criteria.

    Args:
        data (list): List of tuples with roll number and marks.
        criteria (str, optional): The criteria for filtering.

    Returns:
        list: List of roll numbers matching the criteria or None if invalid criteria.
    '''
    if criteria is None:
        return [rollno for rollno, _ in data]
    elif criteria == "above_average":
        average = sum(marks for rollno, marks in data)/len(data)
        return [rollno for rollno, marks in data if marks >= average]
    elif criteria == "below_average":
        average = sum(marks for rollno, marks in data)/len(data)
        return [rollno for rollno, marks in data if marks < average]
    elif criteria == "fail":
        return [rollno for rollno, marks in data if marks < 40]
    elif criteria == "toppers":
        return [rollno for rollno, marks in data if marks >= 90]
    else:
        return None