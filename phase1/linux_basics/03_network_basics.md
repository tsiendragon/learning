# Network Basics

This section will introduce basic networking concepts in Linux, including configuring network interfaces and using tools like ping and netstat.

## 概念的解释
网络基础涉及计算机之间的通信。包括 IP 地址、子网掩码和网关的配置。

## 参数的解释
- **`ifconfig`**：配置网络接口。
  - `interface`：网络接口名称。
  - `up`：启用接口。
  - `down`：禁用接口。
- **`ping`**：测试网络连通性。
  - `-c`：发送的包数。

## 实践的例子
1. 使用 `ifconfig eth0 up` 启用网络接口。
2. 使用 `ping -c 4 google.com` 测试网络连通性。
3. 使用 `ifconfig` 查看当前网络配置。

## 测试题目
1. 如何查看当前网络接口的配置？
2. 使用哪个命令可以测试与远程服务器的连通性？
3. 如何启用或禁用网络接口？
