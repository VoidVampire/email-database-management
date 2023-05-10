# Email Database Management

Email Database Management is a Python-based project that allows users to create an account, send, and receive emails using a local MySQL database. This project aims to provide a practical learning experience in MySQL and Python programming.

Please note that this project does not connect to the internet. All email data and account information are stored locally in a project folder on the desktop.

## Features

- **Account Creation**: Users can create a new account by providing their desired username, password, and other relevant details.

- **Compose**: Users can compose and send emails to other users within the system. They can specify the recipient(s), subject, and the content of the email.

- **Inbox**: Users can view the emails they have received from other users. The inbox displays the sender's name, subject, and the date of receipt.

- **Sent**: Users can check the emails they have sent. The sent folder shows the recipient's name, subject, and the date the email was sent.

- **Drafts**: Users can save email drafts to work on later. Drafts can be edited, deleted, or sent at a later time.

- **Trash**: Users can move emails to the trash folder to delete them. Emails in the trash folder can be permanently deleted or restored to the inbox.

## Requirements

- Python (version 3.X or later)
- MySQL

## Installation

1. Clone the repository to your local machine. 
`git clone https://github.com/your_username/email-database-management.git`
2. Install the required dependencies. You can use pip to install the necessary packages.
`pip install mysql-connector-python`
3. Set up the MySQL database:
- Create a new database named `email_db`.
- Import the `email_db.sql` file located in the project's folder to set up the necessary tables.

4. Open the `config.py` file and update the MySQL database connection details. Modify the `host`, `user`, `password`, and `database` variables to match your local MySQL configuration.

5. Run the main script to start the application.


## Usage

- After running the application, you will be prompted with a menu to sign in or create a new account.
- Follow the instructions on the screen to navigate through the different features of the email management system.
- Use the provided commands or menu options to compose, view, and manage emails.

## Contributing

Contributions to this project are welcome. If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [MySQL](https://www.mysql.com/) - The open-source relational database management system.
- [Python](https://www.python.org/) - A powerful and versatile programming language.
