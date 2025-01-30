# Introduction to Linux File Permissions

Understanding file permissions is crucial for managing a Linux system securely and effectively. This guide introduces the fundamental concepts, commands, practical examples, exercises with answers, and references to help beginners grasp Linux file permissions.

## Basic Concepts

In Linux, each file and directory has an associated set of permissions that determine who can read, write, or execute them. These permissions are defined for three categories:

- **User (u)**: The owner of the file.
- **Group (g)**: A set of users who share access rights.
- **Others (o)**: All other users.

The permissions are represented as a string of 10 characters, for example: `-rwxr-xr--`. Here's a breakdown:

- The first character indicates the type:
  - `-`: Regular file
  - `d`: Directory
  - `l`: Symbolic link
- The next nine characters are divided into three sets of three:
  - **User permissions**: `rwx` (read, write, execute)
  - **Group permissions**: `r-x` (read, execute)
  - **Others permissions**: `r--` (read)

Each permission is represented by a character:
- `r`: Read permission
- `w`: Write permission
- `x`: Execute permission
- `-`: No permission

## Viewing Permissions

To view the permissions of files and directories, use the `ls -l` command:

```bash
ls -l
```
This command lists files and directories in the current directory along with their permissions, ownership, and other details.

Output looks like:

```
total 24
-rwxrwxrwx 1 1025 users 11357 Dec  9 23:21  LICENSE
-rw-r--r-- 1 1025 users  1841 Jan 30 21:15 'LICENSE copy'
-rwxrwxrwx 1 1025 users  4084 Jan 30 22:34  README.md
drwxrwxrwx 1 1025 users   102 Jan 30 22:15  docs
drwxrwxrwx 1 1025 users   140 Jan 30 20:26  experiment
-rw-r--r-- 1 1025 users  3699 Jan 30 22:26  mkdocs.yml
drwxrwxrwx 1 1025 users   174 Jan 30 22:31  site
```


## Changing Permissions
The `chmod` (change mode) command is used to modify file and directory permissions. There are two methods to specify permissions: symbolic and numeric.
### Symbolic Method

The symbolic method uses letters to represent permissions and operations:

- `u`: User

- `g`: Group

- `o`: Others

- `a`: All (user, group, and others)

Operations:

- `+`: Add permission

- `-`: Remove permission

- `=`: Set exact permission

Examples:

- Add execute permission for the user:


```bash
chmod u+x filename
```

- Remove write permission for the group:


```bash
chmod g-w filename
```

- Set read and write permissions for all:


```bash
chmod a=rw filename
```

### Numeric Method

The numeric method uses octal numbers to represent permissions:

- `4`: Read

- `2`: Write

- `1`: Execute

Combine these values to set permissions. For example:

- `7` (4+2+1): Read, write, and execute

- `6` (4+2): Read and write

- `5` (4+1): Read and execute

- `4`: Read only

The permissions are set in the order of user, group, and others. For example:


```bash
chmod 755 filename
```

This sets:

- User: Read, write, execute (`7`)

- Group: Read, execute (`5`)

- Others: Read, execute (`5`)

## Changing Ownership
The `chown` (change owner) command changes the ownership of a file or directory:

```bash
chown user:group filename
```

- `user`: New owner

- `group`: New group

To change only the user or group:

- Change user:


```bash
chown user filename
```

- Change group:


```bash
chown :group filename
```

## Exercises

Test your understanding with the following exercises:

### Exercise 1

Create a file named `experiment/test.sh` with content

```bash
echo "hello world"
```
and set its permissions so that:
  - The user can read, write, and execute.
  - The group can read and execute.
  - Others have no permissions.
  - you (the user) can run the file by typing `bash experiment/test.sh` which returned "hello world"

Try you self first and then check with the following soluction to compare the status of the file. Solution may not be unique

**Solution:**

```bash
# Create the file
touch experiment/test.sh
echo "echo 'hello world' > experiment/test.sh
ls -l experiment/test.sh
-rw-r--r-- 1 user group 0 Jan 30 22:49 experiment/test.sh    # Initial state

# Add content to the file


# Change permissions
chmod 750 experiment/test.sh
ls -l experiment/test.sh
-rwxr-x--- 1 user group 11 Jan 30 22:49 experiment/test.sh   # Final state
```

### Exercise 2
Change the group ownership of a directory
1. Make a directory named `experiment/a` and a file named `test.sh` in it.
2. change the group ownership of `experiment/a` to `editors`

**Solution:**

```bash
chown :editors experiment/a
```
```

3. **Exercise 3**
Remove write permission for others from all files in the current directory.
**Solution:**

```bash
chmod o-w *
```

## References

For further reading, consider the following resources:

- [An Introduction to Linux Permissions]()

- [Linux file permissions explained]()

- [Practice Linux Permissions Basics with 13 Easy Questions [Part I]]()

Understanding and managing file permissions are fundamental skills for Linux users and administrators. Practice these commands and concepts to enhance your proficiency in handling Linux file systems securely.
