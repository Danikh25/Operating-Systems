# Operating-Systems

## **CLI**:
A Command Line Interpreter
• Echo param: prints the parameter given as argument to appropriate streams (file, shell screen).
• Exit: to exit the program.
• Command -> filename: redirects the output of command to a file named filename. If a file with the
same name already exists it deletes it and creates a new one.
• Command ->> filename: appends the output of command to a file with name filename. If the file does not already exist, it creates it

## **Fair Share Scheduler**:

Implementing the simulation of a process scheduler that is responsible for scheduling a given list of processes that belongs to a given list of users running on one CPU. The scheduling runs in a fair-share scheduling and works as follow:

• Several users may exist in the system and each user may own several processes
• The first scheduler cycle will start at second “1”, it works in a cyclic manner
• the scheduler distributes each user’s time share equally between processes that belong to that user
• there is no priority on users and processes

## **Virtuak Memory Management**:

• *Store* (any variable): This instruction stores the given variable id and its value in the first unassigned spot in the memory.

• *Release* (string variableId): This instruction removes the variable id and its value from the memory so the page becomes available inn the memory

• *Lookup* (string variableId): This instruction checks if the given variableId is stored in the memory and returns its value or -1 if it does not exist. If the Id does exist it returns its value. If a page fault occurs, then it should move this variable into the memory and release the assigned page in the virtual memory. If no spot is available in the memory, program needs to swap this variable with the variable with smallest Last Access time, in the main memory.
