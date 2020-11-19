# Password Manager - This project was not made to be used as anything more than a indicator of functionality. Do NOT consider it as anything more.

This is a (somewhat) secure password management system written in Python. Although the system is relatively secure, I am by no means a security professional so I would be careful when using this is software.


No encrytion, just hashing. No user ID, just website name(service) and password created randomly.

The RDBMS I'm using is SQLite3.

The Service_Name and MasterPassword are appended and then hashed using SHA256 and then saved as hexdigest().
The master password is saved within the source code (lol) and so I recommend saving it as precompiled byte code.

Change MASTERPW to the password of your liking and then save the source code as compiled Python byte code using:

```
import py_compile
```

```
py_compile.compile("filename.py")
```

Run with 
```
python filename.pyc
```
*This project is designed as a proof of concept. I would be careful when using this in high-security environments.


