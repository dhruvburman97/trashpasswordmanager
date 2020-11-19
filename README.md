# Password Manager

This is a (somewhat) secure password management system written in Python. Although the system is relatively secure, I am by no means a security professional so I would be careful when using this is software.


No encrytion, just hashing. No user ID, just website name and password created randomly.

THe master password is saved within the source code (lol).

The RDBMS I'm using is SQLite3.

THe service name and Master password are appended and then hashed using SHA256 and then saved as hexdigest().

Change MASTERPW to the password of your liking and then save the source code as compiled Python byte code using:

import py_compile
py_compile.compile("filename.py")

*This project is designed as a proof of concept. I would be careful when using this in high-security environments.
