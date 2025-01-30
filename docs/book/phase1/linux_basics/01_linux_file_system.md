# Linux File System

This section will cover the basics of the Linux file system, including its structure and common commands used to navigate and manage files.

## Concept Explanation
The Linux file system is a hierarchical structure for storing and organizing data. It includes directories, files, and links. Common directories include `/etc` (configuration files), `/var` (variable data), `/home` (user directories), and `/usr` (user programs).

## Common basic commands & explanation
- **`ls`**: List directory contents.
  - `-l`: Use long format listing.
  - `-a`: Show all files, including hidden ones.
  - `-h`: Show file sizes in human-readable format (KB, MB, GB).
  - `-R`: List subdirectories recursively.
- **`cd`**: Change current directory.
  - `..`: Go back to parent directory.
  - `~`: Go to home directory.
  - `-`: Go to previous directory.
- **`pwd`**: Display current directory path.
- **`mkdir`**: Create new directory.
  - `-p`: Create parent directories.
- **`rm`**: Remove files or directories.
  - `-r`: Remove directories recursively.
  - `-f`: Force removal.
- **`echo`**: Print a line of text to the terminal.
  - `>`: Save to a file (overwrite), e.g., `echo "text" > file.txt`
  - `>>`: Append to a file, e.g., `echo "text" >> file.txt`
- **`cp`**: Copy files and directories.
  - `-r`: Copy directories recursively.
  - `-p`: Preserve file attributes.
  - `-v`: Verbose mode, show progress.
- **`mv`**: Move or rename files and directories.
  - `-i`: Interactive mode, prompt before overwrite.
  - `-v`: Verbose mode, show what's being moved.
- **`cat`**: Display file contents.
  - `-n`: Number all output lines.
  - Use `less` or `more` for viewing large files.
- **`head`**: Display first part of files.
  - `-n N`: Show first N lines (default: 10).
  - `-c N`: Show first N bytes.
  - `-q`: Never print headers giving file names.
- **`tail`**: Display last part of files.
  - `-n N`: Show last N lines (default: 10).
  - `-f`: Follow file growth (useful for log files).
  - `-F`: Same as -f, but retry if file becomes inaccessible.
- **`grep`**: Search text using patterns.
  - `-i`: Case-insensitive search.
  - `-r`: Search recursively in directories.
  - `-n`: Show line numbers.
- **`chmod`**: Change file permissions.
  - `+x`: Add execute permission.
  - `u+w`: Add write permission for user.
  - `g+r`: Add read permission for group.
- **`chown`**: Change file owner and group.
  - `-R`: Change ownership recursively.
- **`find`**: Search for files in directory hierarchy.
  - `-name`: Search by name.
  - `-type`: Search by type (f for files, d for directories).
  - `-size`: Search by size.
- **`tar`**: Archive files.
  - `-c`: Create archive.
  - `-x`: Extract archive.
  - `-z`: Use gzip compression.
  - `-f`: Specify archive file.
- **`zip`**: Archive files.
  - `-r`: Recursively archive directories.
  - `-q`: Quiet mode, suppress output.

- **`df`**: Show disk space usage.
  - `-h`: Human-readable sizes.
- **`du`**: Show directory space usage.
  - `-h`: Human-readable sizes.
  - `-s`: Summary only.

## Practical Examples
1. **View All Files and Directories**:
   - **Command**: `ls -la`
   - **Example**: check  `/home` directory and want to see all files (including hidden ones) with details, run:
     ```bash
     ls -la /home
     ```
   - This command will list all files and directories in `/home`, showing permissions, owner, size, and modification date.

2. **Change Directory**:
   - **Command**: `cd /var/log`
   - **Example**: To check log files, enter the logs directory:
     ```bash
     cd /var/log
     ```
   - After this command, your current directory will be `/var/log`, and you can use other commands like `ls` to view its contents.

3. **Create New Directory**:
   - **Command**: `mkdir -p /tmp/newdir`
   - **Example**: To create a nested directory structure:
     ```bash
     mkdir -p /tmp/newdir/subdir
     ```
   - This creates `newdir` and `subdir` under `/tmp`, even if they don't exist.

4. **Remove Directory**:
   - **Command**: `rm -rf /tmp/newdir`
   - **Example**: To safely remove a directory and all its contents:
     ```bash
     rm -rf /tmp/newdir
     ```
   - This command will recursively remove `newdir` and all its contents without confirmation. If you want to confirm the removal, use `rm -r /tmp/newdir`.

## More Practical Examples

5. **File Operations**:
   - **Copy Files and Directories**:
     ```bash
     # Copy a file preserving attributes
     cp -p source.txt backup.txt

     # Copy directory with all contents
     cp -r /path/to/source_dir /path/to/dest_dir
     ```

   - **Move and Rename**:
     ```bash
     # Rename a file
     mv oldname.txt newname.txt

     # Move file to another directory
     mv file.txt /path/to/destination/

     # Move multiple files
     mv file1.txt file2.txt /path/to/destination/
     ```

   - **View File Contents**:
     ```bash
     # View entire file
     cat myfile.txt

     # View file with line numbers
     cat -n myfile.txt

     # View large file page by page
     less largefile.txt

     # View first 5 lines of file
     head -n 5 myfile.txt

     # View last 5 lines of file
     tail -n 5 myfile.txt

     # Monitor log file in real-time
     tail -f /var/log/syslog
     ```

6. **Search Operations**:
   - **Find Files**:
     ```bash
     # Find all .txt files in current directory and subdirectories
     find . -name "*.txt"

     # Find files larger than 100MB
     find /home -size +100M

     # Find directories
     find . -type d
     ```

   - **Search File Contents**:
     ```bash
     # Search for "error" in log file
     grep "error" app.log

     # Search recursively in all files
     grep -r "TODO" /path/to/project/

     # Case-insensitive search with line numbers
     grep -in "warning" *.log
     ```

7. **Archive Management**:
   - **Create and Extract Archives**:
     ```bash
     # Create a compressed archive
     tar -czf backup.tar.gz /path/to/directory

     # Extract a compressed archive
     tar -xzf backup.tar.gz

     # List contents of archive
     tar -tf backup.tar.gz
     ```

   - **Zip Archive**:
     ```bash
     # Create a zip archive
     zip -r backup.zip /path/to/directory

     # Extract a zip archive
     unzip backup.zip

     # List contents of zip archive
     unzip -l backup.zip
     ```

8. **Disk Usage**:
   - **Check Space Usage**:
     ```bash
     # Check disk space usage
     df -h

     # Check directory size
     du -sh /path/to/directory

     # Find largest directories
     du -h /home | sort -rh | head -n 5
     ```

9. **Permission Management**:
   - **Change Permissions**:
     ```bash
     # Make a script executable
     chmod +x script.sh

     # Give read permission to group
     chmod g+r file.txt

     # Change permissions recursively
     chmod -R 755 /path/to/directory
     ```

   - **Change Ownership**:
     ```bash
     # Change file owner
     chown user:group file.txt

     # Change ownership recursively
     chown -R user:group /path/to/directory
     ```

10. **Text Processing**:
    - **Basic Text Operations**:
      ```bash
      # Count lines, words, and characters
      wc myfile.txt

      # Sort file contents
      sort names.txt

      # Remove duplicate lines
      sort names.txt | uniq
      ```

## Common Directory Explanations and Hands-on Examples

1. **`/etc` Directory**
   - **Description**: Stores system and application configuration files.
   - **Hands-on Examples**:
     - View network configuration files:
       ```bash
       ls /etc/network
       ```
     - Edit hosts file (requires admin privileges):
       ```bash
       sudo nano /etc/hosts
       ```

2. **`/var` Directory**
   - **Description**: Used for storing variable data like log files, cache, and temporary files.
   - **Hands-on Examples**:
     - View log files:
       ```bash
       ls /var/log
       ```
     - Check mail queue (if mail service exists):
       ```bash
       ls /var/mail
       ```

3. **`/home` Directory**
   - **Description**: Personal directory for each user, storing user data and configurations.
   - **Hands-on Examples**:
     - Go to current user's home directory:
       ```bash
       cd ~
       ```
     - View all files and directories for current user:
       ```bash
       ls -la ~
       ```

4. **`/usr` Directory**
   - **Description**: Stores user-level programs and data, typically containing binaries, libraries, and shared data.
   - **Hands-on Examples**:
     - View executable files:
       ```bash
       ls /usr/bin
       ```
     - View shared libraries:
       ```bash
       ls /usr/lib
       ```

## Practice Questions

Let's practice the commands we've learned with a comprehensive exercise:

1. Create the following directory structure:
```
test/
├── a/
│   ├── test1.txt
│   └── test2.txt
├── b/
│   └── test3.txt
├── c/
│   └── test4.txt
├── test5.txt
└── test6.txt
```

2. Perform these operations:
   - Rename `test5.txt` to `test7.txt`
   - Remove `test6.txt`
   - Display the modification time of `test1.txt`
   - Add the text "hello world" to both `test1.txt` and `test2.txt`
   - Show the contents of both modified files
   - Display the final directory structure
   - Check and compare the sizes of:
     * Original test directory
     * Directory 'a'
     * Both archive files
   - Add multiple lines of text to test1.txt:
     ```
     Line 1
     Line 2
     Line 3
     Line 4
     Line 5
     ```
   - Display only the first 3 lines of test1.txt
   - Display only the last 2 lines of test1.txt
   - Monitor test1.txt for changes in real-time (use tail -f)
   - Show the contents of both modified files

3. Archive operations:
   - Create a tar archive of the entire test directory named `test_backup.tar.gz`
   - Create a zip archive of only the `a` directory named `a_backup.zip`
   - List the contents of both archives
   - Create a new directory called `restore`
   - Extract both archives into the `restore` directory
   - Compare the contents of original and restored directories

## Answers

Here's how to complete each task:

1. Create the directory structure:
```bash
# Create directories
mkdir -p test/{a,b,c}

# Create files
touch test/a/test{1,2}.txt
touch test/b/test3.txt
touch test/c/test4.txt
touch test/{test5,test6}.txt
```

2. Perform the operations:
```bash
# Rename file
mv test/test5.txt test/test7.txt

# Remove file
rm test/test6.txt

# Check file time
ls -l test/a/test1.txt

# Add content to files
echo "hello world" > test/a/test1.txt
echo "hello world" > test/a/test2.txt

# View contents
cat test/a/test1.txt
cat test/a/test2.txt

# View structure
tree test

# Add multiple lines to test1.txt
echo -e "Line 1\nLine 2\nLine 3\nLine 4\nLine 5" > test/a/test1.txt

# Display first 3 lines
head -n 3 test/a/test1.txt

# Display last 2 lines
tail -n 2 test/a/test1.txt

# Monitor file (Ctrl+C to stop)
tail -f test/a/test1.txt

# View contents
cat test/a/test1.txt
```

3. Archive operations:
```bash
# Create tar archive
tar -czf test_backup.tar.gz test/

# Create zip archive of directory 'a'
cd test && zip -r ../a_backup.zip a/ && cd ..

# List archive contents
tar -tvf test_backup.tar.gz
unzip -l a_backup.zip

# Check sizes
echo "Directory sizes:"
du -sh test/         # Total test directory size
du -sh test/a/       # Directory 'a' size

echo "Archive sizes:"
ls -lh test_backup.tar.gz  # Tar archive size
ls -lh a_backup.zip        # Zip archive size

# Create restore directory and extract archives
mkdir restore
cd restore
tar -xzf ../test_backup.tar.gz
unzip ../a_backup.zip

# Compare original and restored directories
diff -r test/ restore/test/
diff -r test/a/ restore/a/
```

Example output of size checks:
```bash
Directory sizes:
4.0K    test/
2.0K    test/a/

Archive sizes:
2.8K    test_backup.tar.gz
1.5K    a_backup.zip
```

Final directory structure with sizes:
```
.
├── test/
│   ├── a/
│   │   ├── test1.txt (contains "hello world" and multiple lines)
│   │   └── test2.txt (contains "hello world")
│   ├── b/
│   │   └── test3.txt
│   ├── c/
│   │   └── test4.txt
│   └── test7.txt
├── test_backup.tar.gz
├── a_backup.zip
└── restore/
    ├── test/  (from tar archive)
    │   ├── a/
    │   │   ├── test1.txt
    │   │   └── test2.txt
    │   ├── b/
    │   │   └── test3.txt
    │   ├── c/
    │   │   └── test4.txt
    │   └── test7.txt
    └── a/    (from zip archive)
        ├── test1.txt
        └── test2.txt
```

This exercise helps practice:
- Directory and file creation
- File operations (move, remove)
- File inspection and modification
- Directory structure viewing
- Archive creation and extraction with tar and zip
- Directory comparison and verification
- Size checking of files and directories
- Understanding compression ratios