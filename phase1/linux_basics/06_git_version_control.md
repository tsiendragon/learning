# Git Version Control System

This section will introduce Git, a distributed version control system, and cover basic commands for managing repositories.

## Concept Explanation
Git is a distributed version control system used to track changes in files and collaborate on development.

## Parameter Explanation
- **`git init`**: Initializes a new Git repository.
- **`git clone`**: Clones a remote repository.
- **`git add`**: Adds files to the staging area.
- **`git commit`**: Commits changes.
  - `-m`: Adds a commit message.
- **`git push`**: Pushes local commits to a remote repository.

## Practical Examples
1. Use `git init` to initialize a new repository.
2. Use `git clone <repo>` to clone a remote repository.
3. Use `git add .` to add all changes to the staging area.
4. Use `git commit -m "Initial commit"` to commit changes.
5. Use `git push origin main` to push to a remote repository.

## Test Questions
1. How do you initialize a new Git repository?
2. Which command is used to clone a remote repository?
3. How do you commit changes and add a commit message?

# Git 版本控制系统

## 概念的解释
Git 是一个分布式版本控制系统，用于跟踪文件的更改和协作开发。

## 参数的解释
- **`git init`**：初始化一个新的 Git 仓库。
- **`git clone`**：克隆远程仓库。
- **`git add`**：添加文件到暂存区。
- **`git commit`**：提交更改。
  - `-m`：添加提交信息。
- **`git push`**：推送本地提交到远程仓库。
- **`git merge --squash`**：将指定分支的更改合并到当前分支，但不自动创建合并提交。合并的更改会被暂存，用户需要手动创建提交。

## 实践的例子
1. 在 `master` 创建一个分支 `feature/test`：
   ```bash
   git checkout master
   git checkout -b feature/test
   ```

2. 在 `feature/test` 上进行几个实验性的 commit：
   ```bash
   # 修改文件并提交
   echo "Experiment 1" >> experiment.txt
   git add experiment.txt
   git commit -m "Add experiment 1"

   echo "Experiment 2" >> experiment.txt
   git add experiment.txt
   git commit -m "Add experiment 2"
   ```

3. 在 `master` 创建一个正式分支 `feature/a`：
   ```bash
   git checkout master
   git checkout -b feature/a
   ```

4. 把 `feature/test` 上的工作复制到 `feature/a` 上：
   ```bash
   git checkout feature/a
   git merge --squash feature/test
   git commit -m "Integrate experimental features"
   ```

5. 进行 merge request：
   - 提交 `feature/a` 到远程仓库并创建 merge request。
   ```bash
   git push origin feature/a
   ```

6. 进行 merge review 并合并 merge request：
   - 在代码评审通过后，合并 `feature/a` 到 `master`。
   ```bash
   git checkout master
   git merge feature/a
   ```

## 测试题目
1. 如何初始化一个新的 Git 仓库？
2. 使用哪个命令可以克隆远程仓库？
3. 如何提交更改并添加提交信息？