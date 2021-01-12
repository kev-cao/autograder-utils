# autograder-utils
Instructions and utilities for the autograder.

### [Link to Autograder](https://autograder.sice.indiana.edu/web/course_admin/18)

# Table of Contents
1. [Environment](#environment)
2. [Setting Up a Sample Assignment](#setting-up-a-sample-assignment)
    1. [Settings](#settings)
    2. [Instructor Files](#instructor-files)
    3. [Student Files](#student-files)
    4. [Test Cases](#test-cases)
        1. [Making a Test Suite](#making-a-test-suite)
        2. [Making a Test Case](#making-a-test-case)

## Environment
The autograder runs test cases in an environment that uses OpenJDK 15 and JUnit 5.7.0.

## Setting Up a Sample Assignment
At the top bar, click on the setting cog to the right of "CSCI-C 343 Spring 2021". Click on the "Projects" tab, create a name for the new assignment, and then click "Add Project".

You will see the new assignment pop up below - click on its setting cog.

&nbsp;

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

&nbsp;

### Instructor Files
This is where you will submit the JUnit test files. These should all have the `.java` extension.

![Preview](https://i.imgur.com/Jy2qhwn.png)

&nbsp;

### Student Files
Here, you set the expected student file uploads. All files that are located in the `src` directory of the starter code should be added here. For the sake of simplicity and avoiding user error, we will not be accepting `.zip` files. Choose "Exact Match" and type in all the expected files.

![Preview](https://i.imgur.com/DZzT9DR.png)

&nbsp;

### Test Cases
For simplicity's sake, we will structure the tests as such:

Inside of each test suite, we will have test cases.

Each test case will contain multiple commands. The first command will always compile the test files needed for that test case.

Each command thereafter will run a single test method or groups of test methods for points.

In other words, the test case represents the `.java` test file, and the commands represent the methods in the test file.

&nbsp;

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

&nbsp;

#### Making a Test Case
To create a test case, you will need one command to compile the test file, and a series of commands that each run a test method. These commands will follow the same structure from test case to test case, so I've created a Python script `parse-tests.py` that will assist in generating the commands. To run the script, simply do

```bash
$ python parse-tests.py [ARGS]
```

The script accepts multiple arguments, each of which can either be the relative or absolute path to a `.java` test file, or a directory containing several test files.

```bash
# The following command processes the test file MyTest.java
# and any tests inside of the my_tests directory.
$ python parse-tests.py MyTest.java my_tests/
```

After running the script, you should see some output like this:

```
Test Suite Setup Command:
mkdir classes && javac -d classes/ STUDENT_FILES_HERE

--------------------------
Processing PersonTest.java
--------------------------
Compile: javac -d classes -cp classes/:junit-jupiter-api-5.7.0.jar:apiguardian-api-1.1.1.jar PersonTest.java

Method: Person
Run: java -jar junit-platform-console-standalone-1.7.0.jar --fail-if-no-tests --disable-banner --details-theme=ascii --disable-ansi-colors -cp classes --select-method=PersonTest#Person

Method: Programmer
Run: java -jar junit-platform-console-standalone-1.7.0.jar --fail-if-no-tests --disable-banner --details-theme=ascii --disable-ansi-colors -cp classes --select-method=PersonTest#Programmer
```

For each `.java` file provided, the command for compiling the test file is given, and the command for running each @Test method in the test file is given. In the context of grading, each test method will be assigned some point value. In order to assign these point values in the Autograder, each of the methods are split up into separate commands which have individual point values.

&nbsp;

#### Compiling Test
To create the test case in the autograder, press the "+" button next to the suite. Give the test case a descriptive name - something like "Compiling PersonTest.java" is a good option. For the command, choose the "Compile: ..." command from script output. You should now see test case on the rightside view.

*Return Code*

- The expected return code should be set to "Zero". As this is just the compiling step, do not set any points for this.

*Feedback*

- For both "Normal" and "Final Graded", set the preset to "Pass/Fail + Output".

&nbsp;

#### Running Test
To set up the commands that will run the methods in the test file, select the ellipses next to the test case, and choose "Add command". Name the command something descriptive - "Running Method" with the method name will suffice. For the command, copy the "Run: ..." command correlating to that method from the script output. Do this for each test method.

*Return Code*

- The expected return code should be set to "Zero". Set the "Correct Return Code" point value to the desired value - leave the "Wrong Return Code" point value at 0.

*Feedback*

- For both "Normal" and "Final Graded", set the preset to "Pass/Fail + Output".

Note: You may want to go back up to the test case and rename it, as it will still have "Compiling" in the name.

![Preview](https://i.imgur.com/HTl7CYt.png)
