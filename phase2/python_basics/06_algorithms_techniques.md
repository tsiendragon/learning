# 常用算法与技巧

## 概念的解释
算法是解决问题的步骤，技巧是编程中的小窍门。

## 参数的解释
- **排序算法**：如快速排序、归并排序。
  - `sorted()`：内置排序函数。
- **搜索算法**：如二分查找。
  - `bisect`：用于二分查找的模块。

## 实践的例子
1. 使用 `sorted()` 对列表排序：
   ```python
   numbers = [3, 1, 4, 1, 5]
   sorted_numbers = sorted(numbers)
   print(sorted_numbers)
   ```
2. 使用 `bisect` 进行二分查找：
   ```python
   import bisect
   index = bisect.bisect_left(numbers, 4)
   print(index)
   ```

## 测试题目
1. 如何使用 `sorted()` 对字典按值排序？
2. 使用哪个模块可以进行二分查找？
3. 如何编写一个简单的排序算法？
