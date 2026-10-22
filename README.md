SJF Scheduling Algorithm in Python

📌 About the Project

This project implements the Shortest Job First (SJF) CPU scheduling algorithm using Python.

SJF is a CPU scheduling algorithm that selects the process with the shortest CPU burst time for execution. The main goal of this algorithm is to minimize the average waiting time of processes.

🎯 Project Objectives

- Understand the concept of the SJF scheduling algorithm.
- Implement CPU scheduling logic using Python.
- Calculate the waiting time and turnaround time of processes.
- Calculate the average waiting time and average turnaround time.

⚙️ Features

- Process scheduling based on burst time.
- Calculation of waiting time for each process.
- Calculation of turnaround time for each process.
- Calculation of average waiting time and turnaround time.
- Simple and readable Python implementation.

🧠 How SJF Works

The Shortest Job First algorithm selects the process with the shortest burst time among the available processes.

In the Non-Preemptive SJF approach, once a process starts execution, it continues until completion.

The main steps are:

1. Receive the processes and their burst times.
2. Select the available process with the shortest burst time.
3. Execute the selected process.
4. Calculate its waiting time and turnaround time.
5. Repeat until all processes have been executed.

📐 Formulas

Turnaround Time:

"Turnaround Time = Waiting Time + Burst Time"

Average Waiting Time:

"Average Waiting Time = Total Waiting Time / Number of Processes"

Average Turnaround Time:

"Average Turnaround Time = Total Turnaround Time / Number of Processes"

🛠️ Technologies Used

- Programming Language: Python 3
- Algorithm: Shortest Job First (SJF)
- Topic: Operating Systems — CPU Scheduling

▶️ How to Run

1. Clone the repository:
   
   git clone <repository-url>

2. Navigate to the project directory:
   
   cd <project-directory>

3. Run the Python file:
   
   python main.py
   
   Replace "main.py" with the actual Python filename if it is different.

📚 Educational Purpose

This project is developed for educational purposes to demonstrate the SJF CPU scheduling algorithm and its role in operating systems.

👨‍💻 Author

Created as a Python programming and Operating Systems project.
