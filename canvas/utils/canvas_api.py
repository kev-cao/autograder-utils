import requests

class CanvasAPI:
    """
    Canvas object that handles all the interactions with the Canvas API.
    """

    def __init__(self, url, token):
        self.url = url
        self.token = token

    def _set_headers(self, session):
        """
        Adds authorization headers to requests Session.

        Params:
            session (Session) : requests Session object.
        """
        session.headers.update({'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'})

    def get_course(self, course_id):
        """
        Gets the course from Canvas.

        Params:
            course_id (String) : the course id.

        Returns:
            json : the response from the API call.
        """
        with requests.Session() as session:
            self._set_headers(session)
            response = session.get(f'{self.url}courses/{course_id}')

        return self.process_response(response.json())

    def get_students(self, course_id):
        """
        Gets all students enrolled in a course.

        Params:
            course_id (String) : the course id.

        Returns:
            (dict of str: json) : a mapping from student usernames to their student JSON objects.
        """
        with requests.Session() as session:
            self._set_headers(session)
            response = session.get(f'{self.url}courses/{course_id}/students')

        students = response.json()
        
        self.process_response(students)
        return {s['login_id']:s for s in students}

    def get_assignment(self, course_id, assignment_id):
        """
        Gets a single assignment.

        Params:
            course_id (String) : the course id.
            assignment_id (String) : the assignment id.

        Returns:
            json : the response from the API call.
        """
        with requests.Session() as session:
            self._set_headers(session)
            response = session.get(f'{self.url}courses/{course_id}/assignments/{assignment_id}')

        return self.process_response(response.json())

    def grade_assignment(self, course_id, assignment_id, student_id, grade, comment=None):
        """
        Grades a student's assignment.

        Params:
            course_id (String) : the course id.
            assignment_id (String) : the assignment id.
            student_id (String|int) : the student's id.
            grade (String) : the grade to give.
            comment (String) : the comment to add with the grade.

        Returns:
            json: the response from the API call.
        """
        with requests.Session() as session:
            self._set_headers(session)

            data = {'submission[posted_grade]': grade,
                    'comment[text_comment]': comment}
            response = session.put(f'{self.url}courses/{course_id}/assignments/{assignment_id}/submissions/{student_id}', params=data)

        return self.process_response(response.json())

    def process_response(self, res):
        """
        Raises an exception if there exists one in the JSON response object, otherwise returns the object.

        Params:
            res (json) : The response object.

        Returns:
            json : The response object.
        """
        if 'errors' in res:
            raise Exception(f'ERROR: {res["errors"][0]["message"]}')
        return res
