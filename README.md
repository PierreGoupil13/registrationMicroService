
**Password Manager Microservice Project Summary:**

**Technologies:**
- Programming Language: Python
- Database: MariaDB (Docker image)
- Encryption: bcrypt for password hashing
- CLI Interface: Command-line interaction for user registration and login

**User Stories:**

1. **User Registration:**
   - As a new user, I want to create an account, so I can securely store and manage my passwords.
   - As a user, I want to provide a unique username and a strong password during registration, so my account remains secure.
   - As a user, I want to receive feedback if I enter a username that already exists, so I can choose a different one.
   - As a user, I want to see a confirmation message after successfully registering, so I know my account was created.

2. **User Login:**
   - As a registered user, I want to log in with my username and password, so I can access my stored passwords.
   - As a user, I want to receive an error message if I enter an incorrect username or password during login, so I can correct my input.
   - As a user, I want to securely log out of my account, ensuring that no one else can access my passwords.
   - As a user, I want to see a welcome message after successfully logging in, so I know I've accessed my account.
   - As a user, I want the system to remember my login session, so I don't have to log in every time I use the password manager.

**Steps for User Registration:**

1. Display a prompt: "Please enter a username:"
2. Capture user input for the username.
3. Display a prompt: "Please enter a password:"
4. Capture user input for the password.
5. Hash the password using bcrypt.
6. Store the username and hashed password in the database.

**Steps for User Login:**

1. Display a prompt: "Please enter your username:"
2. Capture user input for the username.
3. Display a prompt: "Please enter your password:"
4. Capture user input for the password.
5. Retrieve the hashed password from the database based on the entered username.
6. Compare the entered password (after hashing) with the stored hashed password.
7. If the passwords match, provide access to the user's account.

**Additional Considerations:**

- Organize your code using a modular directory structure.
- Separate concerns by using a separate `models/` directory for database models.
- Handle errors and validate user input for enhanced user experience.
- Ensure secure password hashing using bcrypt.
- Document your project, including installation instructions and usage examples.

By following these steps and considering these aspects, you'll be able to build a secure and functional user registration and login microservice for your password manager project. Good luck, and enjoy the process of building and learning!