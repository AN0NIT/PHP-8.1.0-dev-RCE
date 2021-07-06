# PHP 8.1.0-dev RCE:
- A backdoor placed in the PHP 8.1.0-dev lets an attacker to run arbitrary system command by setting the ``User-Agentt`` header and passing system commands to ``zerodiumsystem`` parameter.

- This script takes in the IP address of the victim computer and runs a loop to achieve an interactive basic shell.

