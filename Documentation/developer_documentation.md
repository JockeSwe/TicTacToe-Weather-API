# Developer Documentation for Tic Tac Toe + Weather API integration
___

## Table of Contents
1. **[Introduction](#1-introduction)**
2. **[Technical Specifications and Design](#2-technical-specifications-and-design)**
3. **[Architectural Overview](#3-architectural-overview)**
    - 3.1. [Architectural Diagrams](#31-architectural-diagrams)
    - 3.2. [Main Components Overview](#32-main-components-overview)
    - 3.3. [Modules Folder Structure](#33-modules-folder-structure)
    - 3.4. [Utilities Folder Contents](#34-utilities-folder-contents)
4. **[Development Guidelines and Standards](#4-development-guidelines-and-standards)**
5. **[Testing Framework and Coverage](#5-testing-framework-and-coverage)**
    - 5.1. [Testing Strategy Outline](#51-testing-strategy-outline)
6. **[Versioning Information](#6-versioning-information)**
7. **[Performance Metrics and Optimization](#7-performance-metrics-and-optimization)**
8. **[Accessibility Considerations](#8-accessibility-considerations)**
9. **[Troubleshooting and FAQs](#9-troubleshooting-and-faqs)**
10. **[Best Practice Recommendations](#10-best-practice-recommendations)**
11. **[References and Further Reading](#11-references-and-further-reading)**
12. **[Feedback and Updates](#12-feedback-and-updates)**

---

#### 1. Introduction
The purpose of this project is to integrate a weather API into a game
The goal should be to have a simple yet functional integration that serves a purpose rather than just being a random unrelated feature.

---

#### 2. Technical Specifications and Design

Some technologies that are employed into the project are openweathermap's API and pygame.
Both these technologies allow the program to both be visually pleasing but also make it work.
The program also includes random which is used to randomize and give the opponent somewhat of it's own mind and creates a more engaging challange as the matches are random.  

---

#### 3. Architectural Overview
- **3.1. Architectural Diagrams**  
  [WeatherApi flowchart](./flowchart_weatherapi.PNG)  
  [Main flowchart](./flowchart_main.PNG)  
  [pygameCode flowchart](./flowchart_pygamecode.PNG)  
  
- **3.2. Main Components Overview**  
  `main.py`: runs the whole game and brings everything together, including inputs, checking available moves, player and bot moves, and checking win condition  
  `pygameCode.py`: Handles everything graphically including loading background image from weatherApi, drawing Tic Tac Toe board, and putting player's and the bot's pieces on the screen.  
  `weatherApi.py`: sends requests and converts weather API and checks which image to use as background in pygame.  
  
- **3.3. Modules Folder Structure**
- 
  `random`: Brings randomness into the game by giving randomized and unique ouputs which makes the bots more interesting to play  
  `pygame`: Brings graphics into the game by adding pictures and drawing a board  
  `requests`: Sends http requests to API's or and web servers to integrate real time weather data into the game  
  `json`: Used to format API requests which is data that is more easily readable by humans  
  
- **3.4. Utilities Folder Contents**  
  `random.randint(a,b)`: Returns a random integer between a and b  
  `print()`: Prints into console, useful for debugging  
  `input()`: Asks the user for input which is then used to give user tailored experiences  
  `pygame.init()`: Initializes pygame modules so it works  
  `pygame.display.flip()`: Updates pygame display to show things that has been drawn/ added to the screen  
  `int() / str()`: Converts a given value to an integer/ string  

---

#### 4. Development Guidelines and Standards
The program should be a smooth experience for the user, use Object Oriented Programming as focus and integrate API into the project.

---

#### 5. Testing Framework and Coverage
- **5.1. Testing Strategy Outline**  
  Much of the testing was to print out something inside of a function to see if the function worked, if it did you could go deeper and see why a specific line doesn't work, if something didnt print when it should have it could be something above it for example a variable used in an if statement has a wrong number which is why the code won't run.
  A lot of the initial testing stage was just to see if it would even run which also used a lot of print(), after the control structure looks to be working more work could be done and when a new control strucutre arise i test to see if it works by cheating the code to quickly get me to the function/ loop or if statements for example.   

---

#### 6. Versioning Information  
Project is not finished yet, it does currently not have a version   

---

#### 7. Performance Metrics and Optimization  
Using loops and functions to save on time and computer memory and tried to avoid unncesessary computer calculation  

---

#### 8. Accessibility Considerations  
Accessibility has not been in a big focus in this project but accessibility has been considered in areas where the user has to input, it gives clear guidelines on what the program asks of the user  

---

#### 9. Troubleshooting and FAQs
N/A

---

#### 10. Best Practice Recommendations
Keep the code clean and add comments to ensure other developers can understand it

---

#### 11. References and Further Reading
N/A

---

#### 12. Feedback and Updates
Join our Discord server where you can create a ticket and submit your feedback and get updates.