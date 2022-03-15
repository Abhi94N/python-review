# logging

- **DEBUG** - Detailed information, typically of interest only when diagnosing problems
- **INFO** - Confirmation that things are working as expected
- **WARNING** - An indication that something unexpected happened, or indicative of some problem in the near future
- **ERROR** - Due to more serious problem, software not able to perform some function
- **CRITICAL** - A serious error, indicating that the program itself may be unable to run

- default format of output
  - 'LOGLEVEL:LOGGER:LOGSTRING'
    - root logger is used by default
    - keep seperate loggers so logs are not shared by the same logger
  - [logging docs](https://docs.python.org/3/library/logging.html#logrecord-attributes)
- loggers are inherited in OOP
- can create custom logs. see employee.py to create filehandler which outputs to file, formatter, and logger
- stream handler outputs info to console