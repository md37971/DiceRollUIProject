# Dice Roll UI Project - (Java & Python)
<ul>
<li>Developed By: Michael Delgado</li>
<li>GitHub Link: github.com/md37971</li>
<li>Core Mechanics & logic: Java using Apache NetBean's IDE</li>
<li>CSV Displayer: Programmed in Python using Matplotlib library.</li>
<li>Summary: Takes the randomized sum of three dices using Java's random library for the purpose of measuring which sum has the most frequent occurances with additional features including file reading/writing for data collecting purposes.</li>
<li>Some bugs may occur since this project is in its early versions.</li>
</ul>
<hr>
<h2>Project Description</h2>
<p>A project developed for the purpose of measuring frequency of the sum of three dices per iteration, where each dice rolls (1-6).</p>
<p>This project was based on one of my old physics assignments that was given to me in my senior year of high school, where we had to measure the frequency of the sum of three dices by either rolling them or programming it.
I decided to challenge myself to program the dice frequency rather than do it physically. The original program I programmed in high school was a small program I coded in Python using the same library for this project as well.
This project is an advanced version of my old program with more features such as displaying/clearing tables, file reading/writing in CSV & TXT, displaying visual data of results, etc. This project contains files both programmed in Java and Python, showcasing cross-integration of two programming languages in one project.
</p> 

<p>There are two components of this project that includes the Java UI (for core mechanics & logic) and an add-on program coded in Python for displaying data using the Matplotlib library. 
  Further information about these two components are explained below.</p>
<hr>
<h2>DiceRollUI - Programmed in Java using Apache NetBeans</h2>

![diceroll](https://github.com/user-attachments/assets/45aad21e-f21e-4e17-b7e7-cbba1c32b14b)

<p>This portion of the project contains all of the main UI components and logic, where Java will take the sum of three dices randomly for a number of iterations of the user's choice to display on the table.
The user can interact with the UI to modify the table or save their results in a file to collect data in their respective directory.
</p>
<h3>Core Features</h3>
<ul>
<li>Conducts the sum of three dice rolls per user's preferred iterations to measure frequency.</li>
<li>Tables that displays results from the three dice.</li>
<li>Interacting with the tables in the UI.</li>
<li>Saving results in CSV & TXT files in a directory.</li>
<li>Ability for a user to login or logout to access a directory, where ceredentials are stored in the logininfo folder.</li>
</ul>
<br>

> [!NOTE]
> Sample files including username folders, CSV files, TXT files, etc. have been included within this repository for experimenting when testing the application.


<hr>
<h2>csvDisplay - Programmed in Python using Matplotlib Library</h2>

![Screenshot 2025-05-21 151445](https://github.com/user-attachments/assets/dec0bbe4-af2c-4670-b46d-8afe253fecb7)

<p>A simple add-on program developed in Python included with Java UI program using the Matplotlib library with the purpose to display visual data by reading CSV files in a directory of the user's choosing from collected data from the Java program.</p>
<h3>Core Features</h3>
<ul>
  <li>Displays results by reading CSV files.</li>
  <li>List all directories from fileDirectories folder set in the login credentials file.</li>
  <li>Matplotlib features to interact while data window is open.</li>
</ul>
<br>

> [!CAUTION]
> DO NOT MODIFY THE LOCATION OF THE PYTHON FILE OR ADD FOLDERS/DIRECTORIES THAT AREN'T INCLUDED IN THE LOGIN CREDENTIALS TEXT FILE AS THIS MAY RESULT IN FILE ERRORS TO OCCUR IN THE PROGRAM.

