# Small Project Setup

1. Create a Virtual Machine on Azure with login credentials Username: Cohort6 and Password: Cohort6_AI2C_2975
2. Note the IP address of the virtual machine, and change the IP address in the Small Project Intro slideshow.
3. On the home directory of the VM, create a file that will encourage people to click on it (I named it "the_answers.txt").  Paste the following in the file.
```
Whew -- you finally got logged in to Mission Control's main system.

You quickly notice that the solar flare has scrambled the file system. You need to get creative to find the
telemetry file, the resource file, and the emergency launch file.

You glance up and see a poem that reminds you to remain calm in situations like this.

“I never saw a wild thing sorry for itself.
A small bird will drop frozen dead from a bough
without ever having felt sorry for itself.”
- D.H. Lawrence

You decide to move to Folder1 to poke around and try to find the files you need to fix.
```
4. Create a folder on the home directory (I named it Folder1). 

5. Inside the folder, create a file (I named it crumpled_paper.).  Add the following text.

```
As you clear of your desk and get prepared to work, you notice an old crumpled piece of paper.  The paper has a few diagrams, and the words

Disk Usage
Directory with telemetry_python_problem1.txt     8.0k
Directory with resource_pythonProblem2.txt       8.0k
empty_directory                                  4.0k

FIND, DU
```

6. Also inside of Folder1, create an elaborate file system.  (I created 100 folders inside of 100 folders using: `mkdir -p Folder{1..100}/Folder{1..100})`

7.  Navigate to the end of two directories (I used Folder22/Folder26 and Folder37/Folder86).  In the first directory create a file named `telemetry_python_problem1.txt`.  Add the following text:
```
Okay, great.  You found the telemetry file.

As the colonists approach Mars, you need to help them calculate their telemetry data.  To do this, you are going to
write a python program.  The program should ask the user if they would like to input either "Miles above Mars" or
"Kilometers above Mars".  If they choose "Miles above Mars", the program should then prompt them to enter the number
of miles.  Then the program should display the number of yards, feet, and inches that are in that many miles.
If the user chooses "Kilometers above Mars", the program should then prompt them to enter the number of kilometers.
Then the program should display the number of meters, centimeters, and millimeters that are in that many kilometers.

Once you solve this problem, proceed to find the resource file in the file system.
```

In the second directory, create a file named `resource_pythonProblem2.txt` and add the text: 
```
You find the resource file, and you are somewhat surprised to see that the problem that needs to be solved deals with
food.

Here's some backgroudn information.  Martian colonists have simple joys — and pizza is one of them. Due to supply shortages, thin-atmosphere baking challenges, and incoming new colonists every meal must be optimized.

You have been sent to Mars with three Automatrons that were designed specifically for making pizza.  The problem is
that no one has taken the time to figure out which Automatron is most efficient (produces the most pizza with the least
amount of dough).

The first Automatron produces 2 circular pizzas (15 inch diameter) that require 20 units of dough.
The second Automatron makes a larger, equilateral triangle pizza, side length 20, that also requires 20 units of dough.
The third Automatron creates a square pizza with side length 18, that only requires 18 units of dough.

As the Chief Engineer, you decide to write a Python Script to figure out which Automatron is most efficient.  Once we avert total disaster and save all 1000 lives on board of the incoming shuttle,
we will want to welcome them with some warm, Martian pizza after all.

Write a Python Script to determine which of these are the best deal.  Use functions to calculate the areas of the pizzas.

Once you have completed this, navigate to root directory to find Problem 3.
```

8. Go to the root directory `/`
9. Create a directory (I named it Problem3)
10. Create a file named `problem3_statement.txt` and add the text (**Note:** You'll need to create a public GitHub repository and change the link in the write-up below.)
```
Our inbound colonists rapidly approach Mars atmosphere, but we still do not have reliable comms with them.
We must rapidly launch our spare rocket to establish comms and share the correct telemetry data with them before they smash into Mars!

There's no time to unload the modules that are on the rocket, and we must begin fueling right away.
The problem is, we do not know how much fuel we need.

As you rush to the rocket, you notice a list of all of the modules' mass on board (your python file input).

Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.

As the Chief Engineer, you need to calculate the total fuel requirement.
To find the total fuel requirement, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?

Once you solve this problem, issue a pull request with all three of your solutions to the International Space Station (https://github.com/Ryan-L-N/Cohort6_Final_PE.git).
To keep the International Space Station's file system clean, your solutions should be inside of a folder with your last name.

Finally, create a broadcast beacon with Earth to state that the crisis was averted.
To do this, create a VM, host a website with a picture of your choice on the VM, and share the public IP address of your website with the International Space Station.
```
11. Add input.txt (found with lesson materials.)

**Note** This completes setting up the VM.  It would be wise to protect the filesystem and files from students by creating an instructor user that has read/write access, and remove the write access from the Cohort6 user.  To do this, follow the steps below.

12. Create a new linux user for the instructor `sudo useradd instructor` and set the password `sudo passwd instructor`.  Don't forget the password.

13. Create a group using `sudo addgroup <groupname>`.  Add the instructor user to this group.  `sudo usermod -a -G <groupname> <username>`

14. Change file permissions to only accept the instructor group. `sudo chgrp <groupname> <Filename>

15. Remove the Cohort6 user from the sudo group `sudo deluser Cohort6 sudo`

