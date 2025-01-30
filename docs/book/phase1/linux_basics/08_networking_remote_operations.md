# Networking and Remote Operations

This section will cover networking tools and techniques for remote operations, such as SSH and SCP.

## Concept Explanation
Networking and remote operations involve technologies for managing and accessing remote computer resources over a network.

## Parameter Explanation
- **`ssh`**: Secure Shell protocol, used for secure login to remote computers.
  - `-p`: Specifies the port.
- **`scp`**: Secure Copy protocol, used for secure file transfer between computers.
  - `-r`: Recursive copy of directories.
- **`rsync`**: Used for efficient file transfer and synchronization.
  - `-a`: Archive mode, preserves file permissions.

## Practical Examples
1. Use `ssh user@host` to log in to a remote server.
2. Use `scp file.txt user@host:/path` to transfer a file to a remote server.
3. Use `rsync -avz /source user@host:/destination` to synchronize a folder.

## Test Questions
1. How do you use `ssh` to log in to a remote server?
2. Which command can be used to recursively copy directories?
3. How do you synchronize local and remote directories?
