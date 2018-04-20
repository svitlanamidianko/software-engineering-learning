# Kanban board

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
assignment!)  You should not be able to see other user's tasks.

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
