# Eins-backend
 A repository for buiding the backend API for project Eins
 This repository is going to be developed using Python, FastAPI
 The frontend will be a ReactJS code
 The database will be in PostgreSQL
 The project backlog is tracked in the project named  [Project-Eins](https://github.com/users/arviCV/projects/1) and the work will be in Agile framework while using a Kanban board for tracking the progress in the  issues


 It includes backend endpoints for user signup and login and implementation of using Node.JS, MangoDB, JWT.
 The user sign up with hashed passwords and login with JWT token generation. 
 MangoDB for user data persistence
 clone the repository  [Project-Eins](https://github.com/users/arviCV/projects/1) using git bash 
 Deploying the application is still out of context in terms of this project-Eins

A repository to set up the developer laptop for easy and quick software development of the backend for project Eins.
This repository is used to developed  using python, FastAPI 
The frontend will be ReactJS code
The database will  be in MangoDB ,PostgreSQL
To set up a Unix-based OS  or Ubuntu/macOS recommended for backend development.
clone the repository using git bash
we have to install the necessary libraries for backend login dependencies.
Install the testing tools and configure package Json.

A repository to implement the login or signup backend end-point for project Eins
Implements basic user authentication using python, FastApi
The frontend wil be ReactJS code
The database  will be in PostgreSQL
This issue implements a complete authentication flow using FastAPI and create the endpoints user signup, login, and logout, with session-based authentication via secure HTTP-only cookies. 
The /signup endpoint allows a new user to register by providing a username and password through a form. The password is hashed using passlib with bcrypt to ensure secure storage.
 After registered, users can authenticate using the /login endpoint, where their credentials are verified against stored data.
 Upon successful authentication, a session cookie named session is set in the user's browser to maintain login state.
 This cookie is marked as HTTP-only to prevent client-side access and protect against XSS attacks.
 The /logout endpoint handles session termination by deleting the session cookie, ensuring the user is logged out.
 Protected routes  are secured using FastAPI's dependency  which checks the validity of the session cookie before granting access. 
 we have to create the code in fastapi main.py and connected to the database using PostgreSQL
 It returns the current logged-in user information and here the explanation for login and logout process

Design and documentation for Login process
       1.The login functionality in this FastAPI application is implemented using a secure and lightweight session-based authentication system.
       2.Users submit their login credentials—username and password—through a POST request to the /login endpoint.
       3. The backend will receives the login request and check if user already exist in the database
       4. After receiving the request, the server validates the username and verifies the password using bcrypt hashing via the passlib library.
       5. If login is successful, the server sets a secure HTTP-only cookie (session) containing the username. 
       6.This cookie is used to identify the authenticated user in subsequent requests to protected routes.
       7. The use of HTTP-only cookies enhances security by preventing client-side JavaScript access, thereby reducing the risk of XSS attacks. 
       8.The login design ensures that only valid users can initiate authenticated sessions, and integrates cleanly with frontend clients using the credentials include option in requests.
       8.It will return the successful  response

Design and documentation for logout process
       1.The logout functionality in this FastAPI application is designed to securely terminate a user’s authenticated session and logout to delete the session cookie
       2. If the user clicks a logout button on the frontend it sends a POST request to the logout endpoint. 
       3. Authentication is verified using a dependency that checks the presence of a valid session cookie.
       4. If the session is valid, the server clears the authentication cookie using response.delete_cookie("session"), effectively logging the user out.
       5.If no session cookie is found or is invalid it returns 401 unauthorized    
       6.By removing the session cookie from the client’s browser, any subsequent access to protected endpoints will be denied until the user logs in again and logging the user out
       7.After deleting the cookie  return a successful response message
