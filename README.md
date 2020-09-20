# Task manager

### A small program to orgranise and arrange your tasks

> The program has two text files to start with user.txt and tasks.txt

> user.txt - stores the username and password

| Username      | Password             |
| ------------- |:-------------:       |
| usernmae1     | password1            |
| usernmae2     | password2            |
| usernmae3     | password3            |

> tasks.txt - stores the tasks assigned to a user

| username task assigned to      | title of task             | description of task             | Due date of the task            |
| -------------                  | :-------------:            | :-------------:                 | :-------------:                 |

Menu example:
![menu example][logo]

[logo]: menu_sample.png "menu sample"

>libraries used

```python
from datetime import date, datetime
import sys
import os
```

> instructions:

1. Login in using username and password (Admin is a super user with a different menu)
2. Choose options from the menu
3. Have fun playing around
