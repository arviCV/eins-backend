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


## Design and documentation for Login process
       1.The login functionality in this FastAPI application is implemented using a secure and lightweight session-based authentication system.

       2.Users submit their login credentials—username and password—through a POST request to the /login endpoint.

       3.To create a new user and password in fastapi Json response we have to install password hasher passlib[bcrypt], bcrypt is a secure, slow hashing algorithm designed specifically for passwords and strong password hashing algorithm and it is mostly used for signup and login for verifying passwords

       5.we have to code for signup endpoint in main.py and create the example like this curl -X POST -F "username=ragavi" -F "password=mysecret" http://localhost:8000/signup

       6.After we use Swagger UI to test it and run the app uvicorn main:app --reload

       7.To open and visit http://localhost:8000/docs and try the signup endpoint with a username and password

       8.you can get the database using PostgreSQL

       9. The backend will receives the login request and check if user already exist in the database

       10.To protect a website after login we create the session cookie and protect from javascript xss 

       11.This cookie will be stored in the browser and sent automatically  with every request

       12.Use a dependency to check session cookie and after creating the dependency can be added to any protected route

       13.The @app.get("/dashboard") this ensures that only logged in users can access dashboard

       14. If login is successful, the server sets a secure HTTP-only cookie (session) containing the username. 

       15..This cookie is used to identify the authenticated user in subsequent requests to protected routes.

       16.. The use of HTTP-only cookies enhances security by preventing client-side JavaScript access, thereby reducing the risk of XSS attacks. XSS Stands for Cross Site Scripting and It is a type of security vulnerability where an attacker injects malicious JavaScript into a trusted website or web application. This script then runs in the browser of other users who visit that site. It is a client side attack often targets cookies, forms and user data

       19.The login design ensures that only valid users can initiate authenticated sessions, and integrates cleanly with frontend clients using the credentials include option in requests.

       20.It will return the successful  response

## Design and documentation for logout process
       1.The logout functionality in this FastAPI application is designed to securely terminate a user’s authenticated session and logout to delete the session cookie

       2. If the user clicks a logout button on the frontend it sends a POST request to the logout endpoint. 

       3. Authentication is verified using a dependency that checks the presence of a valid session cookie.

       4. If the session is valid, the server clears the authentication cookie using response.delete_cookie("session"), effectively logging the user out.

       5.If no session cookie is found or is invalid it returns 401 unauthorized

       6.The 401 unauthorized defines the user is not logged in or user's session is missing,expired or invalid

       7.To fix the 401 error login first and store the session    

       8.By removing the session cookie from the client’s browser, any subsequent access to protected endpoints will be denied until the user logs in again and logging the user out

       9.After deleting the cookie  return a successful response message

