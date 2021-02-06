import requests
import os

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

    def get_students(self, course_id):
        """
        Gets all students enrolled in a course.

        Params:
            course_id (String) : the course id.

        Returns:
            [json]: List of JSON objects representing students.
        """
        with requests.Session() as s:
            self._set_headers(s)
            response = s.get(f'{self.url}courses/${course_id}/students')

        return response.json()
