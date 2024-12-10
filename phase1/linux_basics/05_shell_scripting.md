# Shell 脚本和自动化

This section will cover the basics of writing shell scripts in Linux, including syntax, variables, and control structures.

## 概念的解释
Shell scripting involves writing scripts to automate tasks, consisting of a series of commands.

## 参数的解释
- **`#!/bin/bash`**：Specifies the script interpreter.
- **Variables**：Used to store data.
  - `VAR=value`：Define a variable.
  - `$VAR`：Reference a variable.
- **Control Structures**：Used to control the flow of script execution.
  - `if`：Conditional statements.
  - `for`：Loops.

## 实践的例子
### 实践的例子

1. **创建一个简单的脚本 `hello.sh`**：
   - **步骤**：
     1. 打开终端。
     2. 使用文本编辑器创建一个名为 `hello.sh` 的文件：
        ```bash
        nano hello.sh
        ```
     3. 在文件中输入以下内容：
        ```bash
        #!/bin/bash
        echo "Hello, World!"
        ```
     4. 保存文件并退出编辑器（在 Nano 中按 `CTRL + O` 保存，然后按 `CTRL + X` 退出）。
     5. 使脚本可执行：
        ```bash
        chmod +x hello.sh
        ```
     6. 运行脚本：
        ```bash
        ./hello.sh
        ```
     - 这将输出 “Hello, World!” 到终端。

2. **使用变量和条件语句**：
   - **步骤**：
     1. 创建一个名为 `greet.sh` 的脚本：
        ```bash
        nano greet.sh
        ```
     2. 输入以下内容：
        ```bash
        #!/bin/bash
        NAME="Alice"
        if [ "$NAME" == "Alice" ]; then
          echo "Hello, Alice!"
        else
          echo "Hello, Stranger!"
        fi
        ```
     3. 保存并退出。
     4. 赋予执行权限：
        ```bash
        chmod +x greet.sh
        ```
     5. 运行脚本：
        ```bash
        ./greet.sh
        ```
     - 如果变量 `NAME` 的值是 “Alice”，则输出 “Hello, Alice！”。

3. **使用循环**：
   - **步骤**：
     1. 创建一个名为 `count.sh` 的脚本：
        ```bash
        nano count.sh
        ```
     2. 输入以下内容：
        ```bash
        #!/bin/bash
        for i in {1..5}
        do
          echo "Number: $i"
        done
        ```
     3. 保存并退出。
     4. 赋予执行权限：
        ```bash
        chmod +x count.sh
        ```
     5. 运行脚本：
        ```bash
        ./count.sh
        ```
     - 这将输出数字 1 到 5。

## 测试题目

1. **如何定义一个变量并输出其值？**
   - 创建一个名为 `variable_test.sh` 的脚本，定义一个变量 `GREETING` 并将其值设为 "Hello, Linux!"，然后输出该变量。
   - **步骤**：
     1. 使用文本编辑器打开或创建 `variable_test.sh`。
     2. 输入以下内容：
        ```bash
        #!/bin/bash
        GREETING="Hello, Linux!"
        echo $GREETING
        ```
     3. 保存并退出编辑器。
     4. 赋予执行权限并运行脚本。

2. **如何编写一个条件语句来检查文件是否存在？**
   - 编写一个脚本 `check_file.sh`，检查文件 `example.txt` 是否存在，并输出相应的消息。
   - **步骤**：
     1. 创建并编辑 `check_file.sh`。
     2. 输入以下内容：
        ```bash
        #!/bin/bash
        if [ -f "example.txt" ]; then
          echo "File exists."
        else
          echo "File does not exist."
        fi
        ```
     3. 保存并退出。
     4. 赋予执行权限并运行脚本。

3. **如何使用循环打印 1 到 10？**
   - 创建一个脚本 `print_numbers.sh`，使用 `for` 循环打印数字 1 到 10。
   - **步骤**：
     1. 创建并编辑 `print_numbers.sh`。
     2. 输入以下内容：
        ```bash
        #!/bin/bash
        for i in {1..10}
        do
          echo $i
        done
        ```
     3. 保存并退出。
     4. 赋予执行权限并运行脚本。
