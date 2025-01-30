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

## User Management and Information

In Linux, understanding user management is crucial as it's closely tied to file permissions. Here are essential commands for viewing and managing user information:

### Basic User Commands

1. **View Current User**

   ```bash
   whoami
   ```

   Shows the username of the currently logged-in user.

2. **View User ID and Groups**

   ```bash
   id
   ```

   Displays detailed information about your user ID (UID), primary group ID (GID), and supplementary groups.

3. **List User Groups**

   ```bash
   groups
   ```

   Shows all groups the current user belongs to.

4. **View Logged-in Users**

   ```bash
   who
   ```

   Lists all users currently logged into the system.

5. **Detailed User Activity**

   ```bash
   w
   ```

   Shows who is logged in and what they're doing.

### Understanding User Information Output

When you run `id`, you'll see output like:

```bash
id
>>> uid=1000(username) gid=1000(primary_group) groups=1000(primary_group),4(adm),24(cdrom),27(sudo)
```

This shows:

- Your user ID (uid)
- Your primary group ID (gid)
- All groups you belong to

### Practical Examples

1. **Check Your Username**:

   ```bash
   whoami
   ```

   Output example: `john`

2. **View Your Group Memberships**:

   ```bash
   groups
   ```

   Output example: `john adm cdrom sudo`

3. **Get Detailed User Information**:

   ```bash
   id
   ```

   Output example: `uid=1000(john) gid=1000(john) groups=1000(john),4(adm),27(sudo)`

## Exercises

Test your understanding with the following exercises:

### Exercise 1 Permission

Create a file named `experiment/test.sh` with content

```bash
echo "hello world"
```

and set its permissions so that:

- The user can read, write, and execute.
- The group can read and execute.
- Others have no permissions.
- you (the user) can run the file by typing `bash experiment/test.sh` which returned "hello world"

Try you self first and then check with the following solusion to compare the status of the file. Solution may not be unique

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

### Exercise 2 Owner
Before doing the excersie, please follow the step to open the root user in mac if you are mac user

  Use Directory Utility: <https://support.apple.com/en-gb/102367>
  Use Spotlight to find and open Directory Utility, or follow these steps:

  From the menu bar in the Finder, choose Go > Go to Folder.

  Type or paste /System/Library/CoreServices/Applications/, then press Return.

  Open Directory Utility from the window that opens.

  To enable or disable the root user
  In the Directory Utility window, click the lock lock icon, then enter an administrator name and password.

  To enable the root user, choose Edit > Enable Root User from the menu bar. Then enter the password you want to use. You can then log in as the root user.

  To disable the root user, choose Edit > Disable Root User.

Complex Directory and File Permissions

First, let's check the current system users and groups:

1. Check system information:

   ```bash
   # Check current user and groups
   whoami # show current user
   id -gn # show current user's group

   # View available system users
   cat /etc/passwd | grep -E '/bin/bash|/bin/sh'

   # View system groups
   cat /etc/group | grep -E 'root|nobody|users|wheel'
   ```

Now, create a project structure under the experiment folder with specific ownership and permissions:

1. Create the following structure:

  ```bash
  experiment/
  └── project/
      ├── src/
      │   ├── main.py
      │   └── config.json
      └── logs/
          └── app.log
  ```

2. Set up the following requirements:
   - The `experiment/project` directory should be owned by your current user and group `users`
   - The `experiment/project/src` directory and its contents should be:
     - Owned by your current user and group `root`
     - Root group members can read and execute the directory
     - Others can only execute the directory
   - For `experiment/project/src/main.py`:
     - Owned by your current user and group `root`
     - Your user can read and write
     - Root group can only read
     - Others have no permissions
   - For `experiment/project/src/config.json`:
     - Owned by `root` user and group `root`
     - Only root can read and write
     - No permissions for anyone else
   - The `experiment/project/logs` directory and `app.log`:
     - Owned by your current user and group `nobody`
     - Your user and nobody group can read and write
     - Others can only read

- for mac user, change group 'root' to 'wheel', and change group 'users' to 'staff', which is a different in linux and mac

**Solution:**

**Solution for macOS:**

```bash
# First, check your username and groups
CURRENT_USER=$(whoami)

# Create directory structure
mkdir -p experiment/project/src experiment/project/logs
touch experiment/project/src/main.py experiment/project/src/config.json experiment/project/logs/app.log

# Set directory ownership
# Use wheel group instead of users group (macOS specific)
chown ${CURRENT_USER}:staff experiment/project
chown -R ${CURRENT_USER}:wheel experiment/project/src
# Only root can own and access this file
sudo chown root:wheel experiment/project/src/config.json
chown -R $CURRENT_USER:staff experiment/project/logs

# Set directory permissions
chmod 755 experiment/project          # rwxr-xr-x (everyone can read and execute)
chmod 750 experiment/project/src      # rwxr-x--- (only owner and wheel group)
chmod 755 experiment/project/logs     # rwxr-xr-x (everyone can read and execute)

# Set file permissions
chmod 640 experiment/project/src/main.py     # rw-r----- (owner can read/write, wheel group can read)
chmod 600 experiment/project/src/config.json  # rw------- (only root can access)
chmod 664 experiment/project/logs/app.log     # rw-rw-r-- (owner and staff group can read/write)
```

Verify the setup with:

```bash
# Check all permissions and ownership
ls -la experiment/project/

# Verify specific permissions
echo "Testing owner permissions..."
test -r experiment/project/src/main.py && echo "✓ Can read main.py" || echo "✗ Cannot read main.py"
test -w experiment/project/src/main.py && echo "✓ Can write main.py" || echo "✗ Cannot write main.py"

echo -e "\nTesting root-owned file..."
sudo test -r experiment/project/src/config.json && echo "✓ Root can read config.json" || echo "✗ Root cannot read config.json"
sudo test -w experiment/project/src/config.json && echo "✓ Root can write config.json" || echo "✗ Root cannot write config.json"

echo -e "\nTesting log file permissions..."
test -w experiment/project/logs/app.log && echo "✓ Can write to app.log" || echo "✗ Cannot write to app.log"
```

Key differences for macOS:

1. Using `wheel` group instead of `root` group (wheel is the admin group in macOS)
2. Using `staff` group for general access (common group for macOS users)
3. Root user must be enabled to use root ownership
4. Using `sudo` for root operations
5. Group permissions focus on `wheel` and `staff` instead of custom groups

Note: To use these commands effectively:

- Root user must be enabled (see Directory Utility instructions above)
- Your user must be a member of the wheel group
- Use `sudo` when changing ownership to root
- The `staff` group is used instead of `nobody` as it's more common in macOS

### Exercise 3
Remove write permission for others from all files in the current directory.
**Solution:**

```bash
chmod o-w *
```

### Exercise 4
Testing File Permissions with Bash Scripts

Create a set of test files with different permissions and verify access:

1. Create the following test files under `experiment/permission_test/`:

   ```
   experiment/permission_test/
   ├── read_only.sh        # Only readable
   ├── write_only.sh       # Only writable
   ├── execute_only.sh     # Only executable
   ├── read_write.sh       # Readable and writable
   ├── read_execute.sh     # Readable and executable
   └── test_permissions.sh # Main test script
   ```

2. Set up the test files with this content:

   For `test_permissions.sh`:

   ```bash
   #!/bin/bash

   # Colors for output
   GREEN='\033[0;32m'
   RED='\033[0;31m'
   NC='\033[0m'

   check_permission() {
       local file=$1
       local expected=$2
       local desc=$3

       # Test read permission
       if echo "$expected" | grep -q "r"; then
           if cat "$file" >/dev/null 2>&1; then
               echo -e "${GREEN}✓ Can read $file (Expected)${NC}"
           else
               echo -e "${RED}✗ Cannot read $file (Should be readable)${NC}"
               return 1
           fi
       else
           if cat "$file" >/dev/null 2>&1; then
               echo -e "${RED}✗ Can read $file (Should not be readable)${NC}"
               return 1
           else
               echo -e "${GREEN}✓ Cannot read $file (Expected)${NC}"
           fi
       fi

       # Test write permission
       if echo "$expected" | grep -q "w"; then
           if echo "test" 2>/dev/null >>"$file"; then
               echo -e "${GREEN}✓ Can write to $file (Expected)${NC}"
           else
               echo -e "${RED}✗ Cannot write to $file (Should be writable)${NC}"
               return 1
           fi
       else
           if echo "test" 2>/dev/null >>"$file"; then
               echo -e "${RED}✗ Can write to $file (Should not be writable)${NC}"
               return 1
           else
               echo -e "${GREEN}✓ Cannot write to $file (Expected)${NC}"
           fi
       fi

       # Test execute permission
       if echo "$expected" | grep -q "x"; then
           if [ -x "$file" ]; then
               echo -e "${GREEN}✓ Can execute $file (Expected)${NC}"
           else
               echo -e "${RED}✗ Cannot execute $file (Should be executable)${NC}"
               return 1
           fi
       else
           if [ -x "$file" ]; then
               echo -e "${RED}✗ Can execute $file (Should not be executable)${NC}"
               return 1
           else
               echo -e "${GREEN}✓ Cannot execute $file (Expected)${NC}"
           fi
       fi

       echo "----------------------------------------"
       return 0
   }

   # Test each file
   echo "Testing file permissions..."
   echo "----------------------------------------"

   check_permission "read_only.sh" "r" "read-only file"
   check_permission "write_only.sh" "w" "write-only file"
   check_permission "execute_only.sh" "x" "execute-only file"
   check_permission "read_write.sh" "rw" "read-write file"
   check_permission "read_execute.sh" "rx" "read-execute file"
   ```

3. Create the test files and set their permissions:

```bash
# Create test directory
mkdir -p experiment/permission_test
cd experiment/permission_test

# Create test files with some content
echo "echo 'This is a read-only file'" > read_only.sh
echo "echo 'This is a write-only file'" > write_only.sh
echo "echo 'This is an execute-only file'" > execute_only.sh
echo "echo 'This is a read-write file'" > read_write.sh
echo "echo 'This is a read-execute file'" > read_execute.sh

# Copy the test_permissions.sh content from above
cat > test_permissions.sh << 'EOF'
#!/bin/bash
# ... (content from above) ...
EOF

# Set different permissions
chmod 444 read_only.sh      # r--r--r--
chmod 222 write_only.sh     # -w--w--w-
chmod 111 execute_only.sh   # --x--x--x
chmod 666 read_write.sh     # rw-rw-rw-
chmod 555 read_execute.sh   # r-xr-xr-x
chmod 755 test_permissions.sh # Make test script executable

# Run the test
./test_permissions.sh
```

The test script will:

1. Check each file's permissions
2. Compare them with expected permissions
3. Show green ✓ for correct permissions
4. Show red ✗ for incorrect permissions
5. Explain what's wrong if permissions don't match

This exercise helps you:

- Understand how to test file permissions programmatically
- See the effects of different permission combinations
- Learn how to verify if permissions match requirements
- Practice using chmod with different permission patterns

## Test Questions

1. How do you display your current username in the terminal?
2. Which command shows all groups a user belongs to?
3. What command provides the most detailed information about user ID and group memberships?
4. How can you see who is currently logged into the system?
5. What command shows both logged-in users and their current activities?

## References

For further reading, consider the following resources:

- [An Introduction to Linux Permissions]()

- [Linux file permissions explained]()

- [Practice Linux Permissions Basics with 13 Easy Questions [Part I]]()

Understanding and managing file permissions are fundamental skills for Linux users and administrators. Practice these commands and concepts to enhance your proficiency in handling Linux file systems securely.
