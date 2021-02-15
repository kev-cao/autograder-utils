from utils.canvas_api import CanvasAPI
from utils.config import load_config
from utils.scores_reader import ScoresReader

if __name__ == '__main__':
    try:
        config = load_config('utils')
    except FileNotFoundError:
        raise Exception('There is no config file. Please run init.py before running the program to set up for the Canvas API.')

    try:
        scores_reader = ScoresReader('scores.csv')
    except FileNotFoundError:
        raise Exception('FileNotFoundError: Please name the scores file as scores.csv and place it in the same directory as run.py!')

    #######################################
    # Setting up Canvas API Access
    #######################################
    canvas = CanvasAPI(config['canvas_url'], config['canvas_key'])
    course_id = config['course_id']


    #######################################
    # Checking Course
    #######################################
    print(f'The set course is "{canvas.get_course(course_id)["name"]}".')


    #######################################
    # Getting Assignment
    #######################################
    print('Please provide the assignment ID:')
    print('(you can find this in the URL of the assignment *.instructure.com/courses/:course_id/assignments/:assignment_id_here)')
    assignment_id = input()
    print(f'You have chosen Assignment "{canvas.get_assignment(course_id, assignment_id)["name"]}".')


    #######################################
    # Getting and Scaling Scores
    #######################################
    scale = float(input('What should scores be scaled down to (decimal value)? '))
    scores_reader.scale_scores(scale)


    #######################################
    # Getting Students
    #######################################
    students = canvas.get_students(course_id)


    #######################################
    # Uploading Grades
    #######################################
    for score in scores_reader.scores:
        try:
            student_id = students[score['username']]['id']
            canvas.grade_assignment(course_id, assignment_id, student_id, str(score['score']), f'Autograder: {score["score"]}/{score["total"]}')
        except Exception:
            print(f'Could not upload score for {score["username"]}.')
