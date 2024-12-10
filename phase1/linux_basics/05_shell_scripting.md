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
1. 创建一个简单的脚本 `hello.sh`：
   ```bash
   #!/bin/bash
   echo "Hello, World!"
   ```
2. 使用 `chmod +x hello.sh` 赋予执行权限，然后 `./hello.sh` 运行脚本。
3. 编写一个循环脚本打印 1 到 5：
   ```bash
   #!/bin/bash
   for i in {1..5}; do
       echo $i
   done
   ```

## 测试题目
1. 如何定义一个变量并输出其值？
2. 使用哪个命令可以赋予脚本执行权限？
3. 如何编写一个条件判断语句？
