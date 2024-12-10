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
1. Use `chmod u+x script.sh` to add execute permission for the user.
2. Use `chown user:group file.txt` to change the file owner and group.
3. Use `ls -l` to view the current permissions of a file.

## Test Questions
1. How do you add read permission to a file?
2. Which command is used to change the owner of a file?
3. How do you view the permission information of a file?
