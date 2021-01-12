# autograder-utils
Instructions and utilities for the autograder.

### [Link to Autograder](https://autograder.sice.indiana.edu/web/course_admin/18)

## Environment
The autograder runs test cases in an environment that uses OpenJDK 15 and JUnit 5.7.0.

## Setting Up a Sample Assignment
At the top bar, click on the setting cog to the right of "CSCI-C 343 Spring 2021". Click on the "Projects" tab, create a name for the new assignment, and then click "Add Project".

You will see the new assignment pop up below - click on its setting cog.

### Settings 
*Project Deadline*

- As there are no late submissions in this class, the soft deadline and hard deadline should be set to the same time (Wednesday @ 11:59 PM).

*Access*

- While setting up the assignment, leave all boxes unchecked. After setting up the assignment, check "Publish project".

*Grading Policy*

- Select "Best score".

*Submission Limits*

- TBD.

**Make sure to hit "Save" at the bottom of the page or else the changes will be discarded without warning.**

### Instructor Files
This is where you will submit the JUnit test files. These should all have the `.java` extension.

![Preview](https://i.imgur.com/Jy2qhwn.png)

### Student Files
Here, you set the expected student file uploads. All files that are located in the `src` directory of the starter code should be added here. For the sake of simplicity and avoiding user error, we will not be accepting `.zip` files. Choose "Exact Match" and type in all the expected files.

![Preview](https://i.imgur.com/zDXHxu8.png)

### Test Cases
#### Making a Test Suite
Each test suite is run in a clean environment, and each test suite can have multiple test cases. Depending on the assignment, it may be beneficial to have multiple test suites, but having one test suite containing all of the test cases works perfectly fine as well.

Select "Add Suite" and provide a name for the suite.

*Grading Environment*

- Set the sandbox environment to be "JDK15/JUnit 5.7.0 Image"

*Instructor Files*

- Add all instructor files that will be used in this test suite. For most use cases, this will likely be all of the files.

*Student Files*

- Select all student files that will be used in this test suite. For most use cases, this will likely be all of the files.

*Setup*

- This is where we will compile the students' code. For the command label, put something descriptive, like "Compiling Student Code".

- The setup command will be
    ```bash
    mkdir classes && javac -d classes/ STUDENT_FILES_HERE
    ```
    where you should replace `STUDENT_FILES_HERE` with all of the student files used in the *Student Files* section, separated by spaces.
    
- Make sure to also check "Reject submission if setup fails".

**Make sure to hit "Save" at the bottom of the page or else the changes will be discarded without warning.**

#### Making a Test Case
To create a test case, you will need two commands per test case. One command to compile the tests, and another command to run the tests. These commands will follow the same structure from test case to test case, so I've created a Python script `parse-tests.py` that will assist in generating the commands. To run the script, simply do

```bash
$ python parse-tests.py [ARGS]
```

The script can accept multiple arguments, each of which can either be the path to a `.java` test file, or a directory containing several test files.

```bash
# The following command processes the test file MyTest.java and any tests inside of the my_tests directory.
$ python parse-tests.py MyTest.java my_tests/
```
