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

### Instructor Files

This is where you will submit the JUnit test files. These should all have the `.java` extension.

![Preview](https://i.imgur.com/Jy2qhwn.png)

### Student Files

Here, you set the expected student file uploads. All files that are located in the `src` directory of the starter code should be added here. For the sake of simplicity and avoiding user error, we will not be accepting `.zip` files. Choose "Exact Match" and type in all the expected files.

![Preview](https://i.imgur.com/zDXHxu8.png)

### Test Cases
