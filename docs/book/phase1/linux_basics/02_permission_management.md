# Permission Management

This section will cover how to manage file and directory permissions in Linux, including the use of chmod, chown, and other related commands.

## Concept Explanation
Permission management refers to controlling user access to system resources. Linux uses users, groups, and permission bits to manage permissions.

## Parameter Explanation
- **`chmod`**：Changes file permissions.
  - `u`：User permissions.
  - `g`：Group permissions.
  - `o`：Other user permissions.
  - `+`：Adds permissions.
  - `-`：Removes permissions.
- **`chown`**：Changes the file owner.
  - `user`：New owner.
  - `group`：New group.

## Practical Examples
1. **Changing File Permissions with `chmod`**:
   - **Command**: `chmod u+x script.sh`
   - **Example**: If you have a script named `script.sh` and you want to allow the user to execute it, use:
     ```bash
     chmod u+x script.sh
     ```
   - This command adds execute permission for the user who owns the file. You can verify the change with:
     ```bash
     ls -l script.sh
     ```
   - The output will show `x` in the user permission section (e.g., `-rwxr--r--`).

2. **Changing File Owner with `chown`**:
   - **Command**: `chown user:group file.txt`
   - **Example**: To change the owner of `file.txt` to `user` and the group to `group`, execute:
     ```bash
     sudo chown user:group file.txt
     ```
   - This command changes the ownership, which can be confirmed by listing the file details:
     ```bash
     ls -l file.txt
     ```
   - The output will reflect the new owner and group.

3. **Recursive Permission Change**:
   - **Command**: `chmod -R 755 /path/to/directory`
   - **Example**: To set read, write, and execute permissions for the owner, and read and execute for others on all files and directories within `/path/to/directory`, use:
     ```bash
     chmod -R 755 /path/to/directory
     ```
   - This applies the permissions recursively to all contents within the directory.

4. **Changing Group Ownership**:
   - **Command**: `chown :group file.txt`
   - **Example**: If you only want to change the group of `file.txt` to `group`, run:
     ```bash
     sudo chown :group file.txt
     ```
   - This changes the group ownership while keeping the current user as the owner.

## Test Questions
1. How do you add read permission to a file?
2. Which command is used to change the owner of a file?
3. How do you view the permission information of a file?
