# 今日leetcode

> 由于被线代折磨，今天就做了两题

### 第一题:3的幂

> 给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。
>
> 整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x
>

这题我用的是递归做，交的时候一直报错不停的改逻辑错误

第一先判断n是否等于0或者是否是3的倍数，并且不等于1

` if((n == 0 || n % 3 != 0) && n != 1)`

否则返回false

然后再判断他是否是3或者是否是1

`if(n == 3 || n == 1)`

是则返回true

然后将n/3后递归重新进入方法，直到得出结果

` return isPowerOfThree(n/3)`

时间复杂度很低，击败96%，但递归空间复杂度很高

### 第二题：FuzzBUzz

> 给你一个整数 n ，找出从 1 到 n 各个整数的 Fizz Buzz 表示，并用字符串数组 answer（下标从 1 开始）返回结果，其中：
>
> answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
> answer[i] == "Fizz" 如果 i 是 3 的倍数。
> answer[i] == "Buzz" 如果 i 是 5 的倍数。
> answer[i] == i （以字符串形式）如果上述条件全不满足。

这题挺简单的，先创建一个String类型的List

`List<String> answer = new ArraryList<>() ;`

然后for遍历，3个if判断15的倍数3的倍数和5的倍数，如果都不是就将i转换为String再放入List

