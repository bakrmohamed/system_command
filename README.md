# Local Command Runner

A small Python exercise in subprocess arguments, exit codes and error handling. Importing the module does not start the input loop.

```bash
python system_command.py
python -m unittest -v
```

Enter a local executable with arguments, or `exit`. On POSIX, quoted arguments are parsed with shlex. On Windows, the command string is passed to the native process API. Shell features such as pipes, redirection, variable expansion and built-in commands are not supported.

This is not a sandbox. Commands have your account's permissions and can read, modify or delete your files. Run only commands you understand. There is no remote input, privilege isolation or automatic timeout.

Five offline tests check argument parsing, no-shell execution, exit-code propagation, exit and EOF handling. Process execution is mocked. Windows interactive behavior has not been tested.
