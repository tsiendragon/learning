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
1. **Enabling a Network Interface**:
   - **Command**: `ifconfig eth0 up`
   - **Step-by-Step**:
     1. Open a terminal.
     2. To enable the network interface `eth0`, execute:
        ```bash
        sudo ifconfig eth0 up
        ```
     3. Verify the interface is up by running:
        ```bash
        ifconfig eth0
        ```
     - This command enables the specified network interface, making it ready for network communication.

2. **Testing Network Connectivity**:
   - **Command**: `ping -c 4 google.com`
   - **Step-by-Step**:
     1. Open a terminal.
     2. To test connectivity to Google's servers, use:
        ```bash
        ping -c 4 google.com
        ```
     3. Observe the results to see if packets are successfully sent and received.
     - This command sends 4 packets to `google.com` and reports the response time, helping to diagnose connectivity issues.

3. **Viewing Current Network Configuration**:
   - **Command**: `ifconfig`
   - **Step-by-Step**:
     1. Open a terminal.
     2. To view the current network configuration, simply type:
        ```bash
        ifconfig
        ```
     3. Review the output to see details about all network interfaces, including IP addresses and status.
     - This command provides a snapshot of the current network settings and status of all interfaces.

## 测试题目
1. 如何查看当前网络接口的配置？
2. 使用哪个命令可以测试与远程服务器的连通性？
3. 如何启用或禁用网络接口？
