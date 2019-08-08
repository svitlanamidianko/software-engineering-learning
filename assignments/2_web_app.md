# Kanban board

## Description

A Kanban board is a simple form of task management. Every task that you add can
be in one of three states:

1. To do
2. Doing
3. Done

Your assignment is to write a flask application which provides the functionality
associated with a personal kanban board. This includes:
1. Registering a new user
2. Authenticating as a user
3. Creating a new task
4. Moving tasks to different states
5. Deleting tasks
6. Logging out

Please find a few example kanban board websites and use them so that you have a
clear idea of what is needed. (Note that the professional versions look much
nicer and have many more bells and whistles than are asked for in this
assignment!)  

You also should not be able to see other user's tasks.

### Submission:
Your primary submission must be a pdf listing of your python code, but you must
also include a zip file containing all the code and documentation. Your readme
must include a short description of the structure of the project. Be sure to
highlight any extra features that you’ve implemented.

### Installation:
As part of your submission you must include a zip file with all the necessary
code and html, a requirements.txt file, and a `README.md` file. To get your
application to run should only require the following steps:

```python3
python3.6 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

### Testing:
The project must also include appropriate unit tests. These unit tests should be
run using the following command (while in the project’s root directory):

```python3
python3 -m unittest discover test
```

## Alternative Assignment
If your contribution to the final project has involved a significant aspect of
web programming then you can submit a pdf containing links to pull requests
where you have used similar techniques and technology as is asked for in the
above assignment. As always your code should include a significant amount of
unit tests and be well documented.

## Submission Information

**Due:** Week 9, Friday

**Weight:** x 5

## Focused Outcomes Added

- **[#cs162-communication](https://seminar.minerva.kgi.edu/app/outcome-index/cs162-communication?course_id=153)**: Ensure that all code, documentation and commit messages are clearly written with explanations where appropriate.
- **[#cs162-separationofconcerns](https://seminar.minerva.kgi.edu/app/outcome-index/cs162-separationofconcerns?course_id=153)**: Design systems such that any task is handled by exactly one component and each component handles conceptually similar tasks.
- **[#cs162-testing](https://seminar.minerva.kgi.edu/app/outcome-index/cs162-testing?course_id=153)**: Write comprehensive and meaningful testing code for the system.
- **[#cs162-webstandards](https://seminar.minerva.kgi.edu/app/outcome-index/cs162-webstandards?course_id=153)**: Build systems that correctly use the standard web technologies (e.g. http, html)