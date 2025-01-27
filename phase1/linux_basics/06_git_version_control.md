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
- **`git cherry-pick`**：从远程仓库中提取指定的提交并应用到本地。
- **`git rebase`**：`git rebase` 是一个用于将一个分支的更改应用到另一个分支之上的命令。它常用于线性化提交历史，保持历史的简洁性和可读性。在使用 `git rebase` 时，Git 会把当前分支从其基础分支“移出”，并将其应用到新的基础之上。需要注意的是，rebase 会改变提交历史，因此在共享分支上使用时要谨慎。
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*K4anH9QzRcPqLCv-7HyiCQ.png)

### git flow best practice
![git flow best practice](https://media.geeksforgeeks.org/wp-content/uploads/20240223193253/gitflow_diagram_gfg-660.png)

Git Flow 是一个基于分支的软件开发工作流程，它定义了一组严格的分支操作规则。主要包含以下分支：

1. **Main/Master 分支**
   - 存储官方发布历史
   - 只包含稳定的、已发布的代码
   - 每个提交都应该有一个版本标签（tag）

2. **Develop 分支**
   - 主要的开发分支
   - 包含最新的开发特性
   - 所有特性分支都从这里分出
   - 当开发完成时，合并回 main 分支

3. **Feature 分支**
   - 用于开发新功能
   - 从 develop 分支创建
   - 命名规范：feature/功能名
   - 完成后合并回 develop 分支

4. **Release 分支**
   - 准备发布新版本时创建
   - 从 develop 分支创建
   - 命名规范：release/版本号
   - 只修复 bug，不添加新功能
   - 完成后同时合并到 main 和 develop

5. **Hotfix 分支**
   - 用于修复生产环境的紧急问题
   - 从 main 分支创建
   - 命名规范：hotfix/问题描述
   - 完成后同时合并到 main 和 develop

工作流程：

1. 开发新功能：

   ```bash
   git checkout develop
   git checkout -b feature/new-feature
   # 开发完成后
   git checkout develop
   git merge feature/new-feature
   ```

2. 准备发布：

   ```bash
   git checkout develop
   git checkout -b release/1.0.0
   # 修复 bug 后
   git checkout main
   git merge release/1.0.0
   git checkout develop
   git merge release/1.0.0
   git tag -a v1.0.0
   ```

3. 紧急修复：

   ```bash
   git checkout main
   git checkout -b hotfix/critical-bug
   # 修复后
   git checkout main
   git merge hotfix/critical-bug
   git checkout develop
   git merge hotfix/critical-bug
   git tag -a v1.0.1
   ```

注意事项：

- 保持 main 分支稳定，只合并已测试的代码
- develop 分支应该始终包含最新的开发代码
- feature 分支应该定期与 develop 同步
- release 和 hotfix 分支需要同时合并到 main 和 develop
- 每次发布都要打上版本标签

## 实践的例子

### 1. workflow simulation

1. 在 `main` 创建一个分支 `zhangwei/feature/test`：

   ```bash
   git checkout main
   git checkout -b zhangwei/feature/test
   ```

2. 在 `zhangwei/feature/test` 上进行几个实验性的 commit：

   ```bash
   # 修改文件并提交
   mkdir experiment
   echo "Experiment 1" >> experiment/experiment.txt
   git add experiment/experiment.txt
   git commit -m "Add experiment 1"

   echo "Experiment 2" >> experiment/experiment.txt
   git add experiment/experiment.txt
   git commit -m "Add experiment 2"
   ```

3. 在 `main` 创建一个正式分支 `zhangwei/feature/a`：

   ```bash
   git checkout main
   git checkout -b zhangwei/feature/a
   ```

4. 把 `zhangwei/feature/test` 上的工作复制到 `zhangwei/feature/a` 上：

   ```bash
   git checkout zhangwei/feature/a
   git merge --squash zhangwei/feature/test
   git commit -m "Integrate experimental features"
   git push
   ```

5. 进行 merge request：
   - 提交 `zhangwei/feature/a` 到远程仓库并创建 merge request。

   ```bash
   git push origin zhangwei/feature/a
   ```

6. 进行 merge review 并合并 merge request：
   - 在代码评审通过后，合并 `zhangwei/feature/a` 到 `main`。
   ![alt text](../../docs/images/image.png)

   ```bash
   git checkout main
   git pull  # 再次确保 main 是最新的
   ```

### 2.use git stash to work cross branches

1. 在 `zhangwei/feature/a` 分支上工作时，突然需要切换到 `xiaohong/feature/b` 修复bug：

   ```bash
   git checkout xiaohong/feature/a
   # 在 zhangwei/feature/a 上进行工作
   echo "Feature A work in progress" >> experiment/feature_a.txt
   git add experiment/feature_a.txt

   # 需要切换分支，但工作还未完成，使用 stash 保存
   git stash save "feature A work in progress"

   # 切换到 xiaohong/feature/b 分支
   git checkout xiaohong/feature/b

   # 在 xiaohong/feature/b 上修复 bug
   echo "Bug fix in feature B" >> experiment/feature_b.txt
   git add experiment/feature_b.txt
   git commit -m "Fix bug in feature B"
   ```

2. 在 `xiaohong/feature/b` 上又有新的任务，但需要先回到 `zhangwei/feature/a`：

   ```bash
   # xiaohong/feature/b 上的新工作
   echo "New task in feature B" >> experiment/feature_b.txt
   git add experiment/feature_b.txt

   # 保存 xiaohong/feature/b 的工作
   git stash save "feature B new task"

   # 切回 zhangwei/feature/a 并恢复之前的工作
   git checkout zhangwei/feature/a
   git stash list  # 查看所有 stash
   git stash pop   # 恢复最近的 stash（feature A 的工作）

   # 完成 zhangwei/feature/a 的工作并提交
   git add experiment/feature_a.txt
   git commit -m "Complete feature A work"
   ```

3. 返回 `xiaohong/feature/b` 继续工作：

   ```bash
   git checkout xiaohong/feature/b
   git stash pop   # 恢复 feature B 的工作

   # 完成 xiaohong/feature/b 的工作并提交
   git add experiment/feature_b.txt
   git commit -m "Complete new task in feature B"
   ```

### 3. merge 工作流程

张伟和小红在同一个项目上工作，他们需要分别开发不同的功能。

1. 张伟开始开发用户登录功能：

   ```bash
   # 张伟：从最新的 main 分支创建功能分支
   git checkout main
   git pull  # 确保 main 是最新的
   git checkout -b zhangwei/feature/login

   # 张伟：开发登录功能
   echo "登录页面设计" > experiment/login.txt
   git add experiment/login.txt
   git commit -m "Add login page design"

   echo "登录验证" >> experiment/login.txt
   git add experiment/login.txt
   git commit -m "Add login validation"

   # 张伟：提交并合并功能
   git push origin zhangwei/feature/login
   # 创建 merge request
   git checkout main
   git pull  # 再次确保 main 是最新的
   git merge zhangwei/feature/login
   git push origin main
   ```

2. 同时，小红在开发注册功能：

   ```bash
   # 小红：从最新的 main 分支创建功能分支
   git checkout main
   git pull  # 确保 main 是最新的
   git checkout -b xiaohong/feature/register

   # 小红：开发注册功能
   echo "注册页面设计" > experiment/register.txt
   git add experiment/register.txt
   git commit -m "Add register page design"

   echo "注册验证" >> experiment/register.txt
   git add experiment/register.txt
   git commit -m "Add register validation"
   ```

3. 张伟的功能已经合并，小红需要更新她的分支：

   ```bash
   # 小红：获取最新的 main 分支并更新自己的功能分支
   git checkout main
   git pull
   git checkout xiaohong/feature/register
   git merge main  # 将最新的 main 合并到自己的功能分支

   # 解决可能的冲突后继续工作
   echo "邮箱验证" >> experiment/register.txt
   git add experiment/register.txt
   git commit -m "Add email verification"

   # 小红：提交并合并功能
   git push origin xiaohong/feature/register
   # 创建 merge request
   git checkout main
   git pull
   git merge xiaohong/feature/register
   git push origin main
   ```

4. 开发新功能：

   ```bash
   # 张伟和小红都从最新的 main 开始新的功能开发
   git checkout main
   git pull
   git checkout -b zhangwei/feature/new-feature  # 张伟的新功能分支
   # 或
   git checkout -b xiaohong/feature/new-feature  # 小红的新功能分支
   ```

### 4. git cherry-pick

准备工作：首先创建并设置两个分支的内容。

1. 小红的分支：创建一个包含常用函数列表的文件

   ```bash
   # 小红创建新分支
   git checkout main
   git checkout -b xiaohong/feature/register

   # 创建实验目录
   mkdir -p experiment

   # 创建工具文件
   echo "1. 邮箱格式检查函数" > experiment/utils.txt
   git add experiment/utils.txt
   git commit -m "Add email check function"

   echo "2. 密码强度检查函数" >> experiment/utils.txt
   git add experiment/utils.txt
   git commit -m "Add password check function"
   ```

2. 张伟的分支：开始开发登录功能

   ```bash
   # 张伟创建新分支
   git checkout main
   git checkout -b zhangwei/feature/login

   # 确保实验目录存在
   mkdir -p experiment

   # 创建登录功能文件
   echo "登录页面设计" > experiment/login.txt
   git add experiment/login.txt
   git commit -m "Add login page design"
   ```

3. 张伟发现小红的密码检查函数很实用，想要在登录功能中使用：

   ```bash
   # 查看小红分支的提交历史
   git log xiaohong/feature/register

   # 找到密码检查函数的提交（第二个提交）
   git checkout zhangwei/feature/login
   git cherry-pick abc123  # abc123 是密码检查函数的提交 hash

   # 现在 experiment/login.txt 中会包含密码检查函数
   echo "使用密码强度检查" >> experiment/login.txt
   git add experiment/login.txt
   git commit -m "Integrate password check into login"
   ```

### 5. git rebase

准备工作：模拟一个需要进行 rebase 的场景。

1. 张伟在开发新功能时，main 分支有了新的更新：

   ```bash
   # 创建并切换到功能分支
   git checkout main
   git checkout -b zhangwei/feature/payment

   # 在功能分支上进行一些提交
   echo "添加支付按钮" > experiment/payment.txt
   git add experiment/payment.txt
   git commit -m "Add payment button"

   echo "添加支付处理函数" >> experiment/payment.txt
   git add experiment/payment.txt
   git commit -m "Add payment handler"

   # 这时候发现 main 分支有了新的更新
   # 比如小红的代码被合并到了 main
   ```

2.1/2 模拟小红的工作

```bash
# 小红在张伟开发期间，完成了用户资料更新功能
git checkout main
git checkout -b xiaohong/feature/profile

# 添加用户资料更新功能
echo "添加用户头像上传" > experiment/profile.txt
git add experiment/profile.txt
git commit -m "Add avatar upload"

echo "添加个人信息编辑" >> experiment/profile.txt
git add experiment/profile.txt
git commit -m "Add profile editor"

# 小红的功能完成并合并到 main
git checkout main
git merge xiaohong/feature/profile
git push origin main

# 这时 main 分支已经包含了小红的更新
# 张伟需要将这些更新应用到他的支付功能分支上
```

2. 使用 rebase 更新功能分支：

   ```bash
   # 首先更新 main 分支
   git checkout main
   git pull

   # 切回功能分支并执行 rebase
   git checkout zhangwei/feature/payment
   git rebase main

   # 如果有冲突，解决后继续
   git add .
   git rebase --continue
   ```

3. 使用 rebase 合并多个提交：

   ```bash
   # 假设我们想要合并最近的三个提交
   git rebase -i HEAD~3

   # Git 会打开编辑器，显示类似下面的内容：
   # pick abc123 Add payment button
   # pick def456 Add payment handler
   # pick ghi789 Fix payment bug

   # 修改为：
   # pick abc123 Add payment button
   # squash def456 Add payment handler
   # squash ghi789 Fix payment bug

   # 保存并退出编辑器后，Git 会让你编辑合并后的提交信息
   ```

4. 推送更新后的分支：

   ```bash
   # 因为 rebase 改变了历史，需要强制推送
   git push --force-with-lease origin zhangwei/feature/payment
   ```

注意事项：

- 不要在公共分支上使用 rebase（比如 main 分支）
- 强制推送要谨慎使用，确保不会影响他人的工作
- 如果遇到复杂的冲突，可以使用 `git rebase --abort` 取消操作
- 建议在 rebase 之前创建一个备份分支：

  ```bash
  git branch zhangwei/feature/payment-backup
  ```

### 6. git reset

`git reset` 有三种模式：

- `--soft`：仅重置 HEAD 到指定提交，保留暂存区和工作目录的更改
- `--mixed`（默认）：重置 HEAD 和暂存区，保留工作目录的更改
- `--hard`：重置 HEAD、暂存区和工作目录，完全回到指定提交的状态

准备工作：创建一个场景来演示不同类型的文件状态。

1. 初始设置：

   ```bash
   # 创建新分支
   git checkout main
   git checkout -b zhangwei/feature/reset-demo

   # 创建实验目录
   mkdir -p experiment

   # 第一个提交：添加项目配置
   echo "项目配置文件" > experiment/config.txt
   git add experiment/config.txt
   git commit -m "Initial commit: Add config file"

   # 第二个提交：添加用户模块
   echo "用户登录功能" > experiment/user.txt
   git add experiment/user.txt
   git commit -m "Add user login module"

   # 第三个提交：添加订单模块
   echo "订单处理功能" > experiment/order.txt
   git add experiment/order.txt
   git commit -m "Add order processing module"

   # 第四个提交：更新配置
   echo "更新配置参数" >> experiment/config.txt
   git add experiment/config.txt
   git commit -m "Update config settings"

   # 查看提交历史
   git log --oneline
   # 会显示类似：
   # abc1234 Update config settings
   # def5678 Add order processing module
   # ghi9012 Add user login module
   # jkl3456 Initial commit: Add config file
   ```

现在准备演示不同的文件状态：

   ```bash
   # 1. 已暂存的文件
   echo "已暂存的文件" > experiment/staged.txt
   git add experiment/staged.txt

   # 2. 已修改但未暂存的文件
   echo "新的订单功能" >> experiment/order.txt

   # 3. 未跟踪的文件
   echo "未跟踪的文件" > experiment/untracked.txt
   ```

2. 查看当前状态：

   ```bash
   git status
   # 会显示：
   # Changes to be committed:
   #   new file:   experiment/staged.txt
   # Changes not staged for commit:
   #   modified:   experiment/order.txt
   # Untracked files:
   #   experiment/untracked.txt
   ```

3. 使用 `git reset --soft`：

   ```bash
   # 软重置到上一个提交
   git reset --soft HEAD~1

   git status
   # 现在 committed.txt 的更改会出现在暂存区
   # staged.txt 仍然在暂存区
   # modified.txt 的修改仍然存在
   # untracked.txt 仍然未跟踪
   ```

4. 使用 `git reset --mixed`（默认模式）：

   ```bash
   # 先恢复到最新提交
   git reset --hard HEAD@{1}

   # 然后执行混合重置
   git reset HEAD~1  # 或 git reset --mixed HEAD~1

   git status
   # 现在 committed.txt 和 staged.txt 的更改会出现在未暂存区
   # modified.txt 的修改仍然存在
   # untracked.txt 仍然未跟踪
   ```

5. 使用 `git reset --hard`：

   ```bash
   # 先恢复到最新提交
   git reset --hard HEAD@{1}

   # 然后执行硬重置
   git reset --hard HEAD~1

   git status
   # 现在 committed.txt 的更改完全消失
   # staged.txt 的更改完全消失
   # modified.txt 恢复到原始状态
   # untracked.txt 仍然存在（注意：未跟踪的文件不受影响）
   ```

6. 重置单个文件：

   ```bash
   # 只重置暂存区中的特定文件
   git reset experiment/staged.txt
   # 文件内容保持不变，但会从暂存区移除

   # 重置单个文件到特定提交
   git reset abc123 experiment/modified.txt
   # 将文件重置到指定提交的状态，但更改仍在工作目录中
   ```

注意事项：

- `--hard` 是不可逆的，使用前要确保不需要保留任何更改
- 未跟踪的文件不受 `git reset` 影响
- 如果不确定，可以先创建分支备份：

  ```bash
  git branch backup-before-reset
  ```

- 可以使用 `git reflog` 查看操作历史，在意外重置后恢复：

  ```bash
  git reflog  # 查看操作历史
  git reset HEAD@{1}  # 恢复到上一个操作
  ```
