# 九章算法笔记

Leetcode to lintcode mapping: https://www.1point3acres.com/bbs/thread-453640-1-1.html

Tips:
* dp[i]: 存的是AT i的结果(处理的是nums[i])还是FIRST i的结果(处理的是nums[i-1]). 本质是因为坐标不可能有空的情况, 而序列有空的情况
* 求最值型e.g.最长路径：想清楚dp要存的是“路径长度”还是“最长路径长度” (See Longest Continous Increasing Subsequence), 这个影响的是return dp[N]还是return MAX(dp[0..N])

* 什么时候是DP
  * 求min/max, true/false, count
  * 且不允许排序或交换
* 什么时候不是DP
  * 如果题目需要求出所有“具体”的方案而非方案“个数”: 
    * [LC131 Palindrome  Partitioning](https://leetcode.com/problems/palindrome-partitioning) - 用backtracking
  * 输入数据是一个“集合”(可排序)而不是“序列”
    * [LC128 Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence) vs Longest COMMON Sequence
* 四步思路
  * 坐标型
    * state: f[x][y] 表示我从起点走到坐标x,y……
    * function: 研究走到x,y这个点之前的一步
    * intialize: 起点
    * answer: 终点
  * 单序列+状态
    * f[i]: "前i"个位置/数字/字母,(以第i个为结尾的)...
    * f[i] = f[j] j是i之前的例子
    * intialize: f[0]..
    * answer: f[n-1]..
  * 双序列
    * state: f[i][j]代表了第一个sequence的前i个数字/字符 配上第二个sequence的前j个...
    * function: f[i][j] = 研究第i个和第j个的匹配关系
    * intialize: f[i][0] 和 f[0][i]
    * answer: f[s1.length()][s2.length()]
  * 背包
    * N个正整数，装M的背包
    * state: f[i][j] = "前i"个数, 去除一些能否组成和为j
    * function: f[i][j] = f[i-1][j-a[i]] OR f[i-1][j]
    * initialize: f[X][0] = true; f[0][1..M] = false
    * answer: 使得f[n][X]最大的X(0<=X<=M) 
* 滚动数组优化
  * 只和i和i-1有关,那么就i => i%2, i-1 => (i-1)%2
  * 只和i,i-1,i-2有关, 那么就i => i%3, i-1 => (i-1)%3, i-2 => (i-2)%3

## Additional DP Problems
- 博弈型
   * [LC877 Stone Game](https://leetcode.com/problems/stone-game/)
- 背包型

## TODO: Table Summarize

title | type | last step | subproblem | state | transition | init and boundary | order | result


* [LC322 Coin Change](https://leetcode.com/problems/coin-change)
* [LC62 Unique Paths](https://leetcode.com/problems/unique-paths)
* [LC55 Jump Game](https://leetcode.com/problems/jump-game)
* [LC152 Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray)
* [LC63 Unique Paths II](https://leetcode.com/problems/unique-paths-ii)
* [LC256 Paint House](https://leetcode.com/problems/paint-house/)
* [LC91 Decode Ways](https://leetcode.com/problems/decode-ways)
* [LC674 Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)
* [LC64 Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum)
* [LC361 Bomb Enemy](https://leetcode.com/problems/bomb-enemy)
* [LC338 Counting Bits](https://leetcode.com/problems/counting-bits)
- 状态序列型
* [LC256 Paint House II](https://leetcode.com/problems/paint-house-ii)
* [LC198 House Robber](https://leetcode.com/problems/house-robber)
* [LC213 House Robber II](https://leetcode.com/problems/house-robber-ii)
* [LC121 Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)
* [LC122 Best Time To Buy And Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii)
* [LC123 Best Time To Buy And Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii)
* [LC188 Best Time To Buy And Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv)
- 最长序列型 => 直接按坐标型处理
* [LC300 Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)
* [LC354 Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes)
- 划分型
* [LC279 Perfect Squares](https://leetcode.com/problems/perfect-squares)
* [LC132 Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii)
* [LINT437 Copy Books](https://www.lintcode.com/problem/copy-books/)
* [来自九章算法初级][Word Break]
- 博弈型
* [LINT394 Coins in A Line](https://www.lintcode.com/problem/coins-in-a-line)
- 背包型
* [LINT92 Backpack](https://www.lintcode.com/problem/backpack) 可行性背包
* [LINT563 Backpack V](https://www.lintcode.com/problem/backpack-v) 计数型背包
* [LINT564 Backpack VI](https://www.lintcode.com/problem/backpack-vi) 计数型背包
* [LINT125 Backpack II](https://www.lintcode.com/problem/backpack-ii) 最值型背包
* [LINT440 Backpack III](https://www.lintcode.com/problem/backpack-iii) 最值型背包
- 区间型
* [LC516 Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence)
* [LINT396 Coins In A Line III](https://www.lintcode.com/problem/coins-in-a-line-iii)
* [LC87 Scramble String](https://leetcode.com/problems/scramble-string)
* [LC312 Burst Balloons](https://leetcode.com/problems/burst-balloons)
- 双序列型
* [LINT 77 Longest Common Subsequence](https://www.lintcode.com/problem/longest-common-subsequence)
* [LC97 Interleaving String](https://leetcode.com/problems/interleaving-string)
* [LC72 Edit Distance](https://leetcode.com/problems/edit-distance)
* [LC115 Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences)
* [LC10 Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching)
* [LC44 Wildcard Matching](https://leetcode.com/problems/wildcard-matching)
* [LC474 Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes)
- 难题
* [LINT91 Minimum Adjustment Cost](https://www.lintcode.com/problem/minimum-adjustment-cost)
* [LINT89 K-Sum](https://www.lintcode.com/problem/k-sum)
* [LC300 Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)
  * state: 
    * 正确: f[i]表示前i个数字中, 以**第i个结尾**的LIS的长度
    * 错误: f[i]表示前i个数字中最长的LIS的长度
* [LINT623 K Edit Distance](https://www.lintcode.com/problem/k-edit-distance)
* [LC403 Frog Jump](https://leetcode.com/problems/frog-jump)
* [LC639 Decode Ways II](https://leetcode.com/problems/decode-ways-ii)
* [LC221 Maximal Square](https://leetcode.com/problems/maximal-square)



## TOC
- [九章算法笔记](#%e4%b9%9d%e7%ab%a0%e7%ae%97%e6%b3%95%e7%ac%94%e8%ae%b0)
  - [TODO: Table Summarize](#todo-table-summarize)
  - [TOC](#toc)
  - [Dynamic Programming](#dynamic-programming)
  - [Lecture 1 Introduction](#lecture-1-introduction)
    - [Practice Problems](#practice-problems)
      - [Introduction](#introduction)
    - [Coin Change - 极值](#coin-change---%e6%9e%81%e5%80%bc)
      - [Unique Path - 计数](#unique-path---%e8%ae%a1%e6%95%b0)
    - [Jump Game - 存在性](#jump-game---%e5%ad%98%e5%9c%a8%e6%80%a7)
    - [Maximum Product Subarray - 最值型 - 保留大小](#maximum-product-subarray---%e6%9c%80%e5%80%bc%e5%9e%8b---%e4%bf%9d%e7%95%99%e5%a4%a7%e5%b0%8f)
      - [总结](#%e6%80%bb%e7%bb%93)
    - [背包类型题目](#%e8%83%8c%e5%8c%85%e7%b1%bb%e5%9e%8b%e9%a2%98%e7%9b%ae)
  - [Lecture 2 - 坐标型&位操作型 Coordinate Type](#lecture-2---%e5%9d%90%e6%a0%87%e5%9e%8b%e4%bd%8d%e6%93%8d%e4%bd%9c%e5%9e%8b-coordinate-type)
      - [Practice Question](#practice-question)
    - [Unique Paths II - 坐标型](#unique-paths-ii---%e5%9d%90%e6%a0%87%e5%9e%8b)
    - [Paint House - 序列型](#paint-house---%e5%ba%8f%e5%88%97%e5%9e%8b)
      - [序列型小结](#%e5%ba%8f%e5%88%97%e5%9e%8b%e5%b0%8f%e7%bb%93)
    - [Decode Ways - 划分型](#decode-ways---%e5%88%92%e5%88%86%e5%9e%8b)
      - [坐标型简介](#%e5%9d%90%e6%a0%87%e5%9e%8b%e7%ae%80%e4%bb%8b)
    - [Longest Continous Increasing Subsequence](#longest-continous-increasing-subsequence)
    - [Minimum Path Sum](#minimum-path-sum)
        - [滚动数组优化](#%e6%bb%9a%e5%8a%a8%e6%95%b0%e7%bb%84%e4%bc%98%e5%8c%96)
        - [如何求路径 - 开同维数组记录决策 求路径顺藤摸瓜](#%e5%a6%82%e4%bd%95%e6%b1%82%e8%b7%af%e5%be%84---%e5%bc%80%e5%90%8c%e7%bb%b4%e6%95%b0%e7%bb%84%e8%ae%b0%e5%bd%95%e5%86%b3%e7%ad%96-%e6%b1%82%e8%b7%af%e5%be%84%e9%a1%ba%e8%97%a4%e6%91%b8%e7%93%9c)
    - [Bomb Enemy](#bomb-enemy)
    - [Counting Bits 位操作型 - 小众题目](#counting-bits-%e4%bd%8d%e6%93%8d%e4%bd%9c%e5%9e%8b---%e5%b0%8f%e4%bc%97%e9%a2%98%e7%9b%ae)
  - [Lecture 3 - 序列型](#lecture-3---%e5%ba%8f%e5%88%97%e5%9e%8b)
      - [Practice Question](#practice-question-1)
    - [Paint House II](#paint-house-ii)
        - [优化: 记录最小值和次小值 O(NK^2) -> O(NK) 用来快速选择颜色](#%e4%bc%98%e5%8c%96-%e8%ae%b0%e5%bd%95%e6%9c%80%e5%b0%8f%e5%80%bc%e5%92%8c%e6%ac%a1%e5%b0%8f%e5%80%bc-onk2---onk-%e7%94%a8%e6%9d%a5%e5%bf%ab%e9%80%9f%e9%80%89%e6%8b%a9%e9%a2%9c%e8%89%b2)
    - [House Robber ](#house-robber-%08)
        - [优化: 滚动数组](#%e4%bc%98%e5%8c%96-%e6%bb%9a%e5%8a%a8%e6%95%b0%e7%bb%84)
    - [House Robber II](#house-robber-ii)
    - [Best Time To Buy And Sell Stock - 1 time](#best-time-to-buy-and-sell-stock---1-time)
    - [Best Time To Buy And Sell Stock II - unlimited](#best-time-to-buy-and-sell-stock-ii---unlimited)
    - [Best Time To Buy And Sell Stock III - 2 times](#best-time-to-buy-and-sell-stock-iii---2-times)
    - [Best Time To Buy And Sell Stock IV - K times](#best-time-to-buy-and-sell-stock-iv---k-times)
        - [化简技巧](#%e5%8c%96%e7%ae%80%e6%8a%80%e5%b7%a7)
      - [状态序列型小结](#%e7%8a%b6%e6%80%81%e5%ba%8f%e5%88%97%e5%9e%8b%e5%b0%8f%e7%bb%93)
    - [Longest Increasing Subsequence [很popular]](#longest-increasing-subsequence-%e5%be%88popular)
    - [Russian Doll Envelope](#russian-doll-envelope)
        - [2D技巧：先排序](#2d%e6%8a%80%e5%b7%a7%e5%85%88%e6%8e%92%e5%ba%8f)
      - [滚动数组和打印路径如何结合](#%e6%bb%9a%e5%8a%a8%e6%95%b0%e7%bb%84%e5%92%8c%e6%89%93%e5%8d%b0%e8%b7%af%e5%be%84%e5%a6%82%e4%bd%95%e7%bb%93%e5%90%88)
  - [Lecture 4 - 划分型/博弈型/背包型](#lecture-4---%e5%88%92%e5%88%86%e5%9e%8b%e5%8d%9a%e5%bc%88%e5%9e%8b%e8%83%8c%e5%8c%85%e5%9e%8b)
    - [Practice Question](#practice-question-2)
      - [划分型](#%e5%88%92%e5%88%86%e5%9e%8b)
    - [Perfect Square - 无段数信息](#perfect-square---%e6%97%a0%e6%ae%b5%e6%95%b0%e4%bf%a1%e6%81%af)
    - [Palindrome Partitioning II - 无段数信息](#palindrome-partitioning-ii---%e6%97%a0%e6%ae%b5%e6%95%b0%e4%bf%a1%e6%81%af)
        - [回文串](#%e5%9b%9e%e6%96%87%e4%b8%b2)
    - [Copy Books - 指定段数信息](#copy-books---%e6%8c%87%e5%ae%9a%e6%ae%b5%e6%95%b0%e4%bf%a1%e6%81%af)
      - [博弈型方式](#%e5%8d%9a%e5%bc%88%e5%9e%8b%e6%96%b9%e5%bc%8f)
    - [Coins in a line](#coins-in-a-line)
      - [背包型问题 - 数组大小一定与总承重M有关](#%e8%83%8c%e5%8c%85%e5%9e%8b%e9%97%ae%e9%a2%98---%e6%95%b0%e7%bb%84%e5%a4%a7%e5%b0%8f%e4%b8%80%e5%ae%9a%e4%b8%8e%e6%80%bb%e6%89%bf%e9%87%8dm%e6%9c%89%e5%85%b3)
    - [Backpack - 可行性背包 - 每个物品可取1次能否放满背包](#backpack---%e5%8f%af%e8%a1%8c%e6%80%a7%e8%83%8c%e5%8c%85---%e6%af%8f%e4%b8%aa%e7%89%a9%e5%93%81%e5%8f%af%e5%8f%961%e6%ac%a1%e8%83%bd%e5%90%a6%e6%94%be%e6%bb%a1%e8%83%8c%e5%8c%85)
      - [Backpack V - 计数型背包 - 每个物品可取1次几种方式放满背包](#backpack-v---%e8%ae%a1%e6%95%b0%e5%9e%8b%e8%83%8c%e5%8c%85---%e6%af%8f%e4%b8%aa%e7%89%a9%e5%93%81%e5%8f%af%e5%8f%961%e6%ac%a1%e5%87%a0%e7%a7%8d%e6%96%b9%e5%bc%8f%e6%94%be%e6%bb%a1%e8%83%8c%e5%8c%85)
        - [优化](#%e4%bc%98%e5%8c%96)
    - [Backpack VI - 计数型背包 - 每个物品可取多次几种方式放满背包](#backpack-vi---%e8%ae%a1%e6%95%b0%e5%9e%8b%e8%83%8c%e5%8c%85---%e6%af%8f%e4%b8%aa%e7%89%a9%e5%93%81%e5%8f%af%e5%8f%96%e5%a4%9a%e6%ac%a1%e5%87%a0%e7%a7%8d%e6%96%b9%e5%bc%8f%e6%94%be%e6%bb%a1%e8%83%8c%e5%8c%85)
  - [Lecture 5 - 背包型/区间型](#lecture-5---%e8%83%8c%e5%8c%85%e5%9e%8b%e5%8c%ba%e9%97%b4%e5%9e%8b)
      - [Practice Question](#practice-question-3)
    - [Backpack II - 最值背包 - 物品只有1个带走物品的最大价值](#backpack-ii---%e6%9c%80%e5%80%bc%e8%83%8c%e5%8c%85---%e7%89%a9%e5%93%81%e5%8f%aa%e6%9c%891%e4%b8%aa%e5%b8%a6%e8%b5%b0%e7%89%a9%e5%93%81%e7%9a%84%e6%9c%80%e5%a4%a7%e4%bb%b7%e5%80%bc)
    - [【最难 最重要】Backpack III - 最值背包 - 物品可取无数个带走物品的最大价值](#%e6%9c%80%e9%9a%be-%e6%9c%80%e9%87%8d%e8%a6%81backpack-iii---%e6%9c%80%e5%80%bc%e8%83%8c%e5%8c%85---%e7%89%a9%e5%93%81%e5%8f%af%e5%8f%96%e6%97%a0%e6%95%b0%e4%b8%aa%e5%b8%a6%e8%b5%b0%e7%89%a9%e5%93%81%e7%9a%84%e6%9c%80%e5%a4%a7%e4%bb%b7%e5%80%bc)
        - [优化](#%e4%bc%98%e5%8c%96-1)
    - [Longest Palindromic Subsequence](#longest-palindromic-subsequence)
        - [区间模板](#%e5%8c%ba%e9%97%b4%e6%a8%a1%e6%9d%bf)
        - [如何打印出来最长子序列](#%e5%a6%82%e4%bd%95%e6%89%93%e5%8d%b0%e5%87%ba%e6%9d%a5%e6%9c%80%e9%95%bf%e5%ad%90%e5%ba%8f%e5%88%97)
        - [记忆化搜索](#%e8%ae%b0%e5%bf%86%e5%8c%96%e6%90%9c%e7%b4%a2)
    - [Coins In A Line III](#coins-in-a-line-iii)
    - [Scramble String - 四维数组 必会](#scramble-string---%e5%9b%9b%e7%bb%b4%e6%95%b0%e7%bb%84-%e5%bf%85%e4%bc%9a)
    - [【HARD】Burst Balloons - 典型矩阵相乘题 必会](#hardburst-balloons---%e5%85%b8%e5%9e%8b%e7%9f%a9%e9%98%b5%e7%9b%b8%e4%b9%98%e9%a2%98-%e5%bf%85%e4%bc%9a)
        - [消去型](#%e6%b6%88%e5%8e%bb%e5%9e%8b)
  - [Lecture 6 - 双序列型](#lecture-6---%e5%8f%8c%e5%ba%8f%e5%88%97%e5%9e%8b)
      - [双序列](#%e5%8f%8c%e5%ba%8f%e5%88%97)
      - [Practice Question](#practice-question-4)
    - [Longest Common Subsequence - 超级有名,必会](#longest-common-subsequence---%e8%b6%85%e7%ba%a7%e6%9c%89%e5%90%8d%e5%bf%85%e4%bc%9a)
        - [如何输出](#%e5%a6%82%e4%bd%95%e8%be%93%e5%87%ba)
    - [Interleaving String](#interleaving-string)
    - [Edit Distance](#edit-distance)
    - [Distinct Subsequences](#distinct-subsequences)
        - [滚动数组优化](#%e6%bb%9a%e5%8a%a8%e6%95%b0%e7%bb%84%e4%bc%98%e5%8c%96-1)
    - [Regular Expression Matching](#regular-expression-matching)
    - [Wildcard Matching](#wildcard-matching)
        - [如何打印*匹配了哪些](#%e5%a6%82%e4%bd%95%e6%89%93%e5%8d%b0%e5%8c%b9%e9%85%8d%e4%ba%86%e5%93%aa%e4%ba%9b)
        - [双序列总结](#%e5%8f%8c%e5%ba%8f%e5%88%97%e6%80%bb%e7%bb%93)
    - [Ones and Zeroes - 类似于背包 但是是三维dp](#ones-and-zeroes---%e7%b1%bb%e4%bc%bc%e4%ba%8e%e8%83%8c%e5%8c%85-%e4%bd%86%e6%98%af%e6%98%af%e4%b8%89%e7%bb%b4dp)
  - [Lecture 7 - 综合型](#lecture-7---%e7%bb%bc%e5%90%88%e5%9e%8b)
    - [Minimum Adjustment Cost - 序列+状态=>2维数组](#minimum-adjustment-cost---%e5%ba%8f%e5%88%97%e7%8a%b6%e6%80%812%e7%bb%b4%e6%95%b0%e7%bb%84)
    - [K-Sum - 背包型](#k-sum---%e8%83%8c%e5%8c%85%e5%9e%8b)
    - [Longest Increasing Subsequence - 优化为NlogN](#longest-increasing-subsequence---%e4%bc%98%e5%8c%96%e4%b8%banlogn)
    - [K Edit Distance - 树形DP - 本系列最难](#k-edit-distance---%e6%a0%91%e5%bd%a2dp---%e6%9c%ac%e7%b3%bb%e5%88%97%e6%9c%80%e9%9a%be)
    - [Frog Jump - 序列+哈希表](#frog-jump---%e5%ba%8f%e5%88%97%e5%93%88%e5%b8%8c%e8%a1%a8)
    - [Decode Ways II](#decode-ways-ii)
    - [Maximal Square](#maximal-square)
  - [课程总结](#%e8%af%be%e7%a8%8b%e6%80%bb%e7%bb%93)


## Dynamic Programming 

## Lecture 1 Introduction

### Practice Problems
* [LC322 Coin Change](https://leetcode.com/problems/coin-change)
* [LC62 Unique Paths](https://leetcode.com/problems/unique-paths)
* [LC55 Jump Game](https://leetcode.com/problems/jump-game)
* [LC152 Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray)
  
**Extra**:
* [LC518 Coin Change 2](https://leetcode.com/problems/coin-change-2)
* [LC63 Unique Paths II](https://leetcode.com/problems/unique-paths-ii)
* [LC45 Jump Game II](https://leetcode.com/problems/jump-game-ii)

#### Introduction
* Three types
  * Counting 计数 - 子问题一定不可以重复计算
  * Min/Max 极值 - 子问题可以重复计算并不影响结果,但影响效率
  * True/False 存在性

   * 计数型（情况1+情况2+..): 情况无重复无遗漏 <= 加法原理
   * 最值型(min/max{情况1, 情况2 etc}): 情况可重复 但影响效率
   * 存在型(情况A and/or 情况B and/or ...): 情况可重复 但影响效率

* Step 1: 确定状态
  * 确定状态需要两个意识
    * 最后一步怎么做
    * 子问题
* Step 2: 转移方程
* Step 3: 初始条件和边界情况
* Step 4: 计算顺序


### Coin Change - 极值
这是一个典型的完全背包问题。
设dp[i][j]表示使用前i个硬币，总金额为j时需要的最少硬币数量。

$dp[i][j]=max(dp[i-1][j],dp[i-1][j-k*coin[i]]+k) \quad (0\leq k*coin[i] \leq j)$
```java
class Solution {
    /*
    1. State
      * Last step: I have "amount-val" coins, I use "val" coin to make it to amount
      * Sub: how do I get to "amount-val" coins?
      * state: dp[i] = number of coins to get amount i
    2. Transition
      * dp[i] = MIN OF dp[i-coin] + 1 FOR coin IN coins
    3. Init and boundary
      * dp[0] = 0
      * dp[i] init to MAX_INTEGER = amount+1 to avoid overflow
    4. Order
      * dp[1] .. dp[N]
    */
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount+1];
        int MAX_INT = amount + 1;
        
        dp[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            dp[i] = MAX_INT;
            for (int j = 0; j < coins.length; j++) {
                int coin = coins[j];
                if (i - coin >= 0 && dp[i - coin] != MAX_INT) {
                    dp[i] = Math.min(dp[i], dp[i-coin] + 1);
                }
            }
        }
        
        return dp[amount] == MAX_INT ? -1 : dp[amount];
    }
}
 ```

* Step 1: 确定状态
  * 最后一步怎么做: a_k
  * 子问题: 27-a_k
* Step 2: 转移方程
* Step 3: 初始条件和边界情况
* Step 4: 计算顺序

#### Unique Path - 计数

```java
class Solution {
    /*
    1. State
      * Last Step: at last corder, I can only come from up or left
      * Sub: unique path to up or left
      * State: dp[i][j] = unique paths to cell(i,j)
    2. Transition
      * dp[i][j] = dp[i-1][j] + dp[i][j-1]
    3. Init and Boundary
      * dp[0][0] = 1
      * dp[0][j] = 1
      * dp[i][0] = 1
    4. Order
      * Left to right, up to down
    
    */
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        
        return dp[m-1][n-1];
    }
}
```
* Step 1: 确定状态
  * 最后一步怎么做: 走到右下角 通过向下或向右的方式
  * 子问题: 计数的问题 求和<1>不能遗漏 <2>不能重复
  * 状态: f[i][j]机器人有多少种方法走到(i,j)
* Step 2: 转移方程
  * f[i][j] = f[i-1][j] + f[i][j-1]
* Step 3: 初始条件和边界情况
  * 初始: f[0][0] = 1
  * 边界: f[0][j] = 1, f[i][0] = 1 
* Step 4: 计算顺序

### Jump Game - 存在性

Time Complexity: $O(N^2)$
```java
class Solution {
    /*
    1. State
      * Last Step: At last stone, I can jump from stone i that can reach me
         nums[i] <= N-1-i
      * Subproblem: How can I reach stone i
      * State: canJump[i] - I can reach stone i
    2. Transition
      * nums[i] = true if for any j < i and canJump[j] = true and nums[j] >= i - j
    3. Boundary
      * nums[0] = true
    4. Order
      * canJump[0]..canJump[N-1]
    
    
    */
    public boolean canJump(int[] nums) {
        int N = nums.length;
        boolean[] canJump = new boolean[N];
        
        canJump[0] = true;
        
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < i; j++) {
                if (canJump[j] && nums[j] >= i-j) {
                    canJump[i] = true;
                    break;
                }
            }
        }
        return canJump[N-1];
    }
}
```

* Step 1: 确定状态
  * 最后一步怎么做: 跳到最后一块石头 不知道从哪里来的, 所以假设从i跳过来
    * 青蛙能否跳到i
    * N-1-i <= a[i]
  * 子问题: 青蛙能否跳到i
  * 状态: f[i] 青蛙能否跳到i
* Step 2: 转移方程
  * $f[j] = OR_{0 \le i < j} (f[i]  AND i + a[i] >= j)$
* Step 3: 初始条件和边界情况
  * 初始: f[0] = true
* Step 4: 计算顺序
  * 计算f[1] .. f[n-1]


### Maximum Product Subarray - 最值型 - 保留大小

```java
class Solution {
    /*
    1. State
      * Last Step: at i, 
        * I can be the largest
        * I can contribute to the largest
          * if I'm positive, I will multiply largest i-1
          * if I'm negative, I will multiply smallest i-1
      * Subproblem:
        * what's maximum product subarray for i-1
      * State
        * min[i] 
        * max[i]
    2. Transition
      * max[i] = MAX OF nums[i] OR max[i-1]*nums[i] OR min[i-1]*nums[i]
      * min[i] = MIN OF nums[i] OR max[i-1]*nums[i] OR min[i-1]*nums[i]
    3. Init and Boundary
      * Init: max[i] = min[i] = nums[i]
    4. Order
      * max[0], min[0]; max[1], min[1] ...; max[N-1] 
    */
    public int maxProduct(int[] nums) {
        int N = nums.length;
        int[] max = new int[N];
        int[] min = new int[N];
        
        int result = nums[0];
        max[0] = nums[0];
        min[0] = nums[0];
        
        for (int i = 1; i < N; i++) {
            max[i] = Math.max(nums[i], Math.max(max[i-1] * nums[i], min[i-1] * nums[i]));
            min[i] = Math.min(nums[i], Math.min(max[i-1] * nums[i], min[i-1] * nums[i]));
            result = Math.max(result, max[i]);
        }
        return result;
    }
}
```

* Step 1: Define State
  * Last Step:
    * Case I: {a[j]} is maximum, then a[j]
    * Case II: 连续子序列长度大于1, 那么最优策略a[j]前一元素一定是a[j-1]
      * II-1: a[j] 为正, 则a[j-1]最大
      * II-2: a[j] 为负, 则a[j-1]最小
  * State: f[j] 最大子序列, g[i]乘积最小子序列
* Step 2: State Transition
  Maximum: f[j] = max{a[j], max{a[j] * f[j-1], a[j]*g[j-1]} | j > 0}
  Minimum: g[j] = min{a[j], min{a[j] * f[j-1], a[j]*g[j-1]} | j > 0}
* Step 3: 初始条件, 边界条件
  * 初始条件: 无
  * 边界条件: j>0 for Case II, 前面至少有一个元素
* Step 4: 计算顺序
  * f[0], g[0], f[1], g[1]
  * Answer: max{f[0], f[1] ... f[n-1]}

#### 总结
* 四步方法
  * 确定状态
    * 研究最后一步
    * 化为子问题
  * 转移方程
    * 根据子问题定义直接得到
  * 初始条件和边界情况
    * 细心, 考虑周全
  * 计算顺序
    * 利用之前的计算结果
* 8种常见类型
  * 重点: 坐标型(20%): 矩阵
  * 重点: 序列型(20%): 硬币
  * 重点: 划分型(20%): 东西分类
  * 重点: 区间型(15%): 区间乘法, 气球爆炸
  * 背包型(10%)
  * 最长序列型(5%): 最长子序列
  * 博弈型(5%)
  * 综合型(5%)

### 背包类型题目
* See [Huahua's blog](https://zxi.mytechroad.com/blog/tag/knapsack/)
## Lecture 2 - 坐标型&位操作型 Coordinate Type

#### Practice Question
* [LC63 Unique Paths II](https://leetcode.com/problems/unique-paths-ii)
* [LC256 Paint House](https://leetcode.com/problems/paint-house/)
* [LC91 Decode Ways](https://leetcode.com/problems/decode-ways)
* [LC674 Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)
* [LC64 Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum)
* [LC361 Bomb Enemy](https://leetcode.com/problems/bomb-enemy)
* [LC338 Counting Bits](https://leetcode.com/problems/counting-bits)

* 初步探索
  * 坐标型
  * 序列型
  * 划分型
* 本章重点
  * 坐标型

### Unique Paths II - 坐标型
```java
class Solution {
    /*
    1. State:
      * Last Step: At last step, he can come from UP or LEFT
      * dp[i][j] = unique paths to reach cell(i,j)
    2. Transition
      * dp[i][j] = dp[i-1][j] + dp[i][j-1] IF NOT OBSTABLE
      * dp[i][j] = 0 IF OBSTACLE
    3. Init and Boundary
      * dp[0][0] = 1 IF NOT OBSTABLE
      * dp[0][i] = Min(1, dp[0][i-1])
    4. Order
      * left to right, up to down
      * Return dp[m-1][n-1]
    */
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid == null || obstacleGrid.length == 0) {
            return 0;
        }
        
        int M = obstacleGrid.length;
        int N = obstacleGrid[0].length;
        
        int[][] dp = new int[M][N];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (obstacleGrid[i][j] == 1) {
                    dp[i][j] = 0;
                    continue;
                }
                if (i == 0 && j == 0) {
                    dp[0][0] = 1;
                } else if (i == 0) {
                    dp[0][j] = dp[0][j-1];
                } else if (j == 0) {
                    dp[i][0] = dp[i-1][0];
                } else {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        return dp[M-1][N-1];
    }
}
```

* Step 1: 确定状态
  * 最后一步怎么做: 走到右下角 通过向下或向右的方式
  * 子问题: 计数的问题 求和<1>不能遗漏 <2>不能重复
  * 状态: f[i][j]机器人有多少种方法走到(i,j)
* Step 2: 转移方程
  * f[i][j] = f[i-1][j] + f[i][j-1]
  * f[i][j] = 0 if 有障碍
* Step 3: 初始条件和边界情况 - 特殊的地方
  * 初始: f[0][0] = 1
  * 边界: f[0][j] = f[0][j-1], //第一排第一列如果前面遇到障碍就过不来了
          f[i][0] = f[i-1][0]
* Step 4: 计算顺序

### Paint House - 序列型

* 序列型一定是开N+1个数组, 因为你要算前0个, 前1个 ... 前N个
```java
class Solution {
    /*
    Sequence DP
    1. State:
      * dp[i] = first i item's minCost, need color information
        -> dp[i][COLOR] = (i-1)-th house min cost, while (i-1)-th has color COLOR
    2. Transition
      * dp[i][RED] = Math.min(dp[i-1][BLUE], dp[i-1][GREEN]) + cost[i-1][RED]
    3. Init and boundary
      * dp[0][COLOR] = 0
    4. Order
      * dp[i][COLOR] for i = [1..N]
      * Return Math.min(dp[N][color])
    
    */
    public int minCost(int[][] costs) {
        int RED = 0, BLUE = 1, GREEN = 2;
        int N = costs.length;
        int[][] dp = new int[N+1][3];
        int[] pi = new int[N+1]; //decisions
        
        //Init
        for (int i = 0; i <= N; i++) {
            for (int c = 0; c <= 2; c++) {
                if (i == 0) {
                    dp[0][c] = 0;
                } else {
                    dp[i][c] = Integer.MAX_VALUE;
                }
            }
        }
        //Transit
        for (int i = 1; i <= N; i++) {
            for (int c = 0; c <= 2; c++) { //Color of house i-1
                for (int prevC = 0; prevC <= 2; prevC++) { //Color of house i-2
                    if (c != prevC) {
                        if (dp[i][c] > dp[i-1][prevC] + costs[i-1][c]) {
                            pi[i] = c;
                        }
                        dp[i][c] = Math.min(dp[i][c], dp[i-1][prevC] + costs[i-1][c]);
                        System.out.println("dp["+i+"]["+c+"]="+dp[i][c]);
                    }
                }
            }
        }
        
        for (int i = 1; i <= N; i++) {
            System.out.print(pi[i] + " ");
        }
        System.out.println(" ");
        
        return Math.min(dp[N][RED], Math.min(dp[N][BLUE], dp[N][GREEN]));
    }
}
```

* Step 1: 确定状态
  * 最后一步怎么做: 知道前N-2栋房子的最小花费 且知道是什么颜色, 
  * 状态: 设油漆前i栋房子并且房子i-1是红色, 蓝色, 绿色分别为f[i][0], f[i][1], f[i][2]
* Step 2: 转移方程
  * f[i][0]油漆前i个房子, 并且第i-1个房子是红色
  * f[i][0] = min{f[i-1][1] + cost[i-1][0], f[i-1][2] + cost[i-1][0]}
* Step 3: 初始条件和边界情况 - 特殊的地方
  * 初始: f[0][0] = f[0][1] = f[0][2] = 0 即不油漆任何房子的花费
* Step 4: 计算顺序
  * 计算f[1][0], f[1][1], f[1][2]...f[N][0], f[N][1], f[N][2]

#### 序列型小结
* 序列型动态规划: **前i个**..最小/方式数/可行性
* 问题: 在设计过程中,发现需要知道油漆前N-1栋房子的最优序列, 房子N-2的颜色
  * 如果只用f[N-1]则无法区分
  * 解决方法:记录下房子N-2的颜色
  * f[i][j] 当房子n-2为红蓝绿的情况下,油漆前N-1栋房子的最小花费
* 模型: 序列+状态


### Decode Ways - 划分型

```java
/*
DP-Sequence
* State
  * Last step: see the last digit, and make a letter, or last two digits make a letter
  * dp[i] - the first i character has X ways to decode
* Transtion
  * dp[i] = dp[i-1] + (dp[i-2] IF i-2, i-1 BETWEEN 10 AND 26)
* Boundary
  * dp[0] = 1, //Think about this case for dp[2]
  * dp[1] = 0 or 1, //Think whether first character is 0 or 1
* Order
  * Left to right, return dp[N]
*/
class Solution {
    public int numDecodings(String s) {
        int N = s.length();
        if (N == 0) {
            return 0;
        }
        
        int[] dp = new int[N+1]; // dp[i] is the result for first i characters
        dp[0] = 1;
        dp[1] = s.charAt(0) == '0'? 0 : 1;
        for (int i = 2; i <= N; i++) { //First i character means string[0..i-1]
            dp[i] = 0; 
            int oneDigit = s.charAt(i-1)-'0'; 
            int twoDigits = Integer.valueOf(s.substring(i-2, i)); //sub[i-2, i-1]
            if (oneDigit >= 1 && oneDigit <= 9) {
                dp[i] += dp[i-1];
            }
            if (twoDigits >= 10 && twoDigits <= 26) {
                dp[i] += dp[i-2];
            }
        }
        return dp[N];
    }
}
```
* Step 1: State
  * 解密数字串即**划分**成若干段数字, 每段数字一个字母
  * 最后一步(最后一段): 对应一个字母
    * A, B, .., Z
  * 需要知道数字串前N-1和N-2个字符的机密方式数
  * 状态: 数字串前i个数字解密为字母串有f[i]种方式
* Step 2: Transition
  * 设数字串S前i个数字机密成字母串有f[i]种方式
    f[i] = f[i-1] | s[i-1]是字母 + f[i-2] | s[i-2]s[i-1]是字母
* Step 3: Init and Boundary
  * Init:  前0个即空串只有1种 f[0]=1
  * Boundary: i=1，只看最后一位, 其余均看最后一位或两位
* Step 4: 计算顺序
  * f[0]，f[1]..f[N]
  * 答案为f[N]

#### 坐标型简介
* 简介 
 * 最简单的动态规划
 * 给定一个序列或者网格
 * 需要找到序列中某个或某些子序列或网格中的某条路径
    * 具有最大最小
    * 计数
    * 存在性
* 动态规划方程
  * f[i]中的下标i表示以a[i]为结尾的满足条件的子序列的性质
  * f[i][j]表示以(i,j)为结尾的满足条件的路径的性质
  * 初始条件f[0]就是指以a[0]为结尾的子序列的性质


### Longest Continous Increasing Subsequence

```java
class Solution {
    /*
    1. State: - decide what to store, the length OR max length
      * Last step: at N-1, I'm larger than N-2, then I do answer(N-2) + 1, 
                 otherwise, I can start a new sequence
      * Sub: what's the LCIS at N-2
      * State: dp[i] = lcis ENDING AT i
    2. Transition
      * dp[i] = dp[i-1]+1 OR 1
    3. Init and bound
      * dp[0] = 1
    4. Order
      * l2r, return MAX OF dp[i] FOR i IN 0..N-1;
    
    */
    public int findLengthOfLCIS(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        int N = nums.length;
        int[] dp = new int[N];
        dp[0] = 1;
        int max = dp[0];
        for (int i = 1; i < N; i++) {
            if (nums[i] > nums[i-1]) {
                dp[i] = dp[i-1]+1;
            } else {
                dp[i] = 1;
            }
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}
```

* 1. State
  * Last step: a[j] can be the longest itself or can add to a[j-1]
  * Subquesiton: what's the longest continous increasing subsequence ending in a[j-1]
  * State: f[j] = longest continous increasing subsequence ending in a[j]
* 2. Transition
  * f[j] = max{1, f[j-1]+1 IF j> 0 AND a[j-1] < a[j]}
* 3. Init and boundary
  * f[0] =  1
* 4. Order
  * Compute f[0] .. f[n-1]
  * Answer is max(f[0] .. f[n-1])


### Minimum Path Sum

```java
/*
Read https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns

DP-Sequence
* State:
  * Last step: at [M-1][N-1], I can come from left or up
  * Subproblem: what is the minPathSum from those two cells
  * dp[i][j] = min path sum ENDING AT cell(i, j)
* Transition
  * dp[i][j] = MIN(dp[i-1][j], dp[i][j-1]) + cost[i][j]
* Boundary
  * dp[0][0] = cost
  * dp[0][j] = dp[0][j-1] + cost[0][j]
  * dp[i][0] = dp[i-1][0] + cost[i][0]
* Ordre
  * l2r, t2d, return dp[M-1][N-1]
* Rolling array
  * dp[M][N] => dp[2][N]
  * dp[i][j] => dp[i%2][j]
  * dp[i-1][j] => dp[1-i%2][j]
  
*/
class Solution {
    public int minPathSum(int[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        
        int M = grid.length, N = grid[0].length;
        int[][] dp = new int[2][N];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (i == 0 && j == 0) {
                    dp[0][0] = grid[0][0];
                    continue;
                } else if (i == 0) {
                    dp[0][j] = dp[0][j-1] + grid[0][j];
                    continue;
                } else if (j == 0) {
                    dp[i%2][0] = dp[1-i%2][0] + grid[i][0];
                    continue;
                } else {
                    dp[i%2][j] = Math.min(dp[1-i%2][j], dp[i%2][j-1]) + grid[i][j];
                }
            }
        }
        
        return dp[(M-1)%2][N-1];
    }
}
```

* State:
  * Last step：coming from two direction
* Transit
  * f[i][j] = min{f[i-1][j] + f[i][j-1]} + A[i][j]
* Init and Boundary
  * f[0][0] = A[0][0]
  * i = 0 or j = 0 comes from 1 direction only
* Order
  * Answer is f[m-1][n-1]



##### 滚动数组优化
* 计算第i行,只需要第i行和第i-1行
* 步骤 - 写出MN的版本
  * 开数组的M换为2
  * 初始 `int old, now = 0` 记录新旧
  * 每次循环先进行 `old = now; now = 1 - now; //0->1, 1->0`
  * f[i-1]换为f[old], f[i]换位f[now]
  * 返回 f[now][n-1]
* 方法2
  * 本质是将上面的版本中 `new = i % 2, old = 1 - i % 2`
  * f[i-1]换为f[1-i%2], f[i]换为f[i%2]

##### 如何求路径 - 开同维数组记录决策 求路径顺藤摸瓜
* 开个新的MN数组 pi 记录决策
* pi[i][j] = 0则是从上面来， pi[i][j] = 1则是从左边来
```java
// 动态规划专题班打印路径版本
public class Solution {
    /**
     * @param grid: a list of lists of integers
     * @return: An integer, minimizes the sum of all numbers along its path
     */
    public int minPathSum(int[][] A) {
        if (A == null || A.length == 0 || A[0].length == 0) {
            return 0;
        }
        
        int m = A.length, n = A[0].length;
        int[][] f = new int[m][n];
        int[][] pi = new int[m][n];
        int i, j;
        for (i = 0; i < m; ++i) {
            for (j = 0; j < n; ++j) {
                if (i == 0 && j == 0) {
                    f[0][0] = A[0][0];
                    continue;
                }
                
                f[i][j] = Integer.MAX_VALUE;
                if (i > 0) {
                    f[i][j] = Math.min(f[i][j], f[i - 1][j] + A[i][j]);
                    if (f[i][j] == f[i - 1][j] + A[i][j]) {
                        pi[i][j] = 0;
                    }
                }
                
                if (j > 0) {
                    f[i][j] = Math.min(f[i][j], f[i][j - 1] + A[i][j]);
                    if (f[i][j] == f[i][j - 1] + A[i][j]) {
                        pi[i][j] = 1;
                    }
                }
            }
        }
        
        // reverse order
        // m-1,n-1
        int[][] path = new int[m + n - 1][2];
        int p;
        i = m - 1;
        j = n - 1;
        for (p = m + n - 2; p >= 0; --p) {
            path[p][0] = i;
            path[p][1] = j;
            if (p == 0) break;
            if (pi[i][j] == 0) {
                --i;
            }
            else {
                --j;
            }
        }
        
        for (p = 0; p < m + n - 1; ++p) {
            System.out.println("(" + path[p][0] + ", " + path[p][1] + "):" + A[path[p][0]][path[p][1]]);
        }
        
        return f[m - 1][n - 1];
    }
}


```

### Bomb Enemy
```java
/*
Idea: Use the same row and col enemy count until encounter the wall
After encounter a wall, recount everything.

Time Complexity: O(MN)

DP-coordinates
* State
  * How many can I bomb going upwards at (M-1, N-1)
  * Need to know (M-2, N-1)
  * UP[i][j]: number of enemy's I can bomb going UP
* Transition
  * up[i][j] = up[i-1][j] IF (i-1,j) NOT WALL
               + 1   IF ENEMY
* Init and border
  * up[i][j] init to 0
  * up[0][j] init to 1 IF ENEMY, 0 OTHERWISE
* Order
  * Compute UP u2d l2r, DOWN d2u l2r, LEFT l2r u2d, RIGHT r2l, u2d
  * Max(U+D+L+R) if cell is EMPTY


*/
class Solution {
    public int maxKilledEnemies(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        
        int M = grid.length, N = grid[0].length;
        int[][] up = new int[M][N];
        int[][] down = new int[M][N];
        int[][] left = new int[M][N];
        int[][] right = new int[M][N];
        
        //Compute UP
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                up[i][j] = 0;
                if (grid[i][j] == 'E') {
                    up[i][j] += 1;
                }
                if ( i-1 >= 0 && grid[i-1][j] != 'W') {
                    up[i][j] += up[i-1][j];
                }
            }
        }
        
        //Compute LEFT
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                left[i][j] = 0;
                if (grid[i][j] == 'E') {
                    left[i][j] += 1;
                }
                if ( j-1 >= 0 && grid[i][j-1] != 'W') {
                    left[i][j] += left[i][j-1];
                }
            }
        }
        
        //Compute DOWN
        for (int i = M-1; i >= 0; i--) {
            for (int j = 0; j < N; j++) {
                down[i][j] = 0;
                if (grid[i][j] == 'E') {
                    down[i][j] += 1;
                }
                if ( i+1 < M && grid[i+1][j] != 'W') {
                    down[i][j] += down[i+1][j];
                }
            }
        }
        
        //Compute RIGHT
        for (int i = 0; i < M; i++) {
            for (int j = N - 1; j >= 0; j--) {
                right[i][j] = 0;
                if (grid[i][j] == 'E') {
                    right[i][j] += 1;
                }
                if ( j+1 < N && grid[i][j+1] != 'W') {
                    right[i][j] += right[i][j+1];
                }
            }
        }
        
        //Compute result
        int result = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == '0') {
                    result = Math.max(result, up[i][j] + down[i][j] + left[i][j] + right[i][j]);
                }
            }
        }
        return result;
    }
}
```

* State:
  * UP[i][j] - the maximum enemy I can bomb going UP
* Transit:
  * UP[i][j] = UP[i-1][j] IF empty
            |  UP[i-1][j] + 1 IF enemy
            |  0 IF wall
* Boundary
  * UP[0][j] = 0 IF not enemy
            |  1 IF enemy
* Order
  * UP - up to down
  * Result - max(UP+DOWN+LEFT+RIGHT) of when (i,j) is empty space


### Counting Bits 位操作型 - 小众题目

```java
public class Solution {
  public int[] countBits(int num) {
      int[] ans = new int[num + 1];
      for (int i = 1; i <= num; ++i)
        ans[i] = ans[i >> 1] + (i & 1); // x / 2 is x >> 1 and x % 2 is x & 1
      return ans;
  }
}
```
* 和位操作相关的动态规划一般用值做为状态
* State
  * Last step: 观察这个数最后一位二进制(最低位),去掉它,看剩下几个1 
* Transition:
  * f[i] = f[i >> 1] + (i mod 2)

## Lecture 3 - 序列型

#### Practice Question
- 状态序列型
* [LC256 Paint House II](https://leetcode.com/problems/paint-house-ii)
* [LC198 House Robber](https://leetcode.com/problems/house-robber)
* [LC213 House Robber II](https://leetcode.com/problems/house-robber-ii)
* [LC121 Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)
* [LC122 Best Time To Buy And Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii)
* [LC123 Best Time To Buy And Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii)
* [LC188 Best Time To Buy And Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv)
- 最长序列型 => 直接按坐标型处理
* [LC300 Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)
* [LC354 Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes)

- Extension:
* [LC337 House Robber III](https://leetcode.com/problems/house-robber-iii/) - 树形房子
* [LC309 Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown)
* [LC714 Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee)

- Good Read:
* [Stock Series DP](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems)

### Paint House II
```java
class Solution {
    /* Sequence DP
    * State: 
       * Last step: At last house, I will try different color that doesn't conflict with second last one min cost
       * Sub: what's the color of second last house, and what's their mincost
       * dp[i][k] = the min cost of first i house (i-1 house), and its color k
    * Transition
      * dp[i][k] = min(dp[i-1][c]) + cost[i-1][k] where c != k
    * Init and bounder
      * Base: dp[0][k] = 0
      * Init: dp[i][k] = Integer.MAX_VALUE;
    * Order
      * left to right
      * min(dp[N][c])  
    
    */
    public int minCostII(int[][] costs) {
        if (costs == null || costs.length == 0 || costs[0].length == 0) {
            return 0;
        }
        int N = costs.length, K = costs[0].length;
        int[][] dp = new int[N+1][K];
        
        //Init
        for (int c = 0; c < K; c++) {
            dp[0][c] = 0;
        }
        
        //For first i house (house i-1)
        for (int i = 1; i <= N; i++) {
            //What's the two min cost for first i-1 house
            int min1 = Integer.MAX_VALUE, id1 = -1; //smallest cost and its associated color
            int min2 = Integer.MAX_VALUE, id2 = -1; //second smallest cost and its associated color
            for (int c = 0; c < K; c++) {
                int cost = dp[i-1][c];
                if (min1 == -1 || cost < min1) {
                    min2 = min1;
                    id2 = id1;
                    min1 = cost;
                    id1 = c;
                } else if (min2 == -1 || cost < min2) {
                    min2 = cost;
                    id2 = c;
                }
            }
            
            //What's the min cost for it to end in color c
            for (int c = 0; c < K; c++) {
                if (c == id1 && id2 != -1) { //Check for case [[8]] where only 1 house is available
                    dp[i][c] = dp[i-1][id2] + costs[i-1][c];
                } else {
                    dp[i][c] = dp[i-1][id1] + costs[i-1][c];
                }
                
            }
        }
        
        int result = Integer.MAX_VALUE;
        for (int c = 0; c < K; c++) {
            result = Math.min(result, dp[N][c]);
        }
        
        return result;       
    }
}
```


* Solution: https://www.jiuzhang.com/solutions/paint-house-ii/
* Almost the same as Paint House

##### 优化: 记录最小值和次小值 O(NK^2) -> O(NK) 用来快速选择颜色
模板套路: 如何选择除了自已以外的最小值
```java
//Getting min and submin: value and index
int min1 = Integer.MAX_VALUE;
int min2 = Integer.MAX_VALUE;
int id1 = -1, id2 = -1;
for (int i = 0; i < N; i++) {
    if (nums[i] < min1) { //小于最小值, 更新最小值和次小值
        min2 = min1;
        id2 = id1;
        min1 = nums[i];
        id1 = 1;
    } else if (nums[i] < min2) { //小于次小值, 仅更新次小值
        min2 = nums[i];
        id2 = i;
    }
}

//Use min and submin
for (int i = 0; i < N; i++) {
    if (i != id1 || id2 == -1) { //maybe only one element, then use min1
        f[i] += min1;
    } else {
        f[i] += min2;
    }
}
```

### House Robber 
```java
/*
Sequence DP
* State:
  * Last step: i-th house I can either rob it, if I didn't rob i-1
               or not rob it, then the value is the same as i-1
  * Sub: what's the value if i-1 is robbed/not robbed
  * State: dp[i][ROBBED/NOT_ROBBED] - the first i house (i-1th) house is ROBBED/NOT_ROBBED
* Transition
  * dp[i][ROBBED] = dp[i-1][NOT_ROBBED]  + value[i-1]
  * dp[i][NOT_ROBBED] = Math.max(dp[i-1][ROBBED], dp[i-1][NOT_ROBBED])


*/
class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int N = nums.length;
        int[][] dp = new int[N+1][2];
        int ROBBED = 0, NOT_ROBBED = 1;
        dp[0][ROBBED] = 0;
        dp[0][NOT_ROBBED] = 0;
        for (int i = 1; i <= N; i++) {
            dp[i][ROBBED] = dp[i-1][NOT_ROBBED] + nums[i-1];
            dp[i][NOT_ROBBED] = Math.max(dp[i-1][ROBBED], dp[i-1][NOT_ROBBED]);
        }
        return Math.max(dp[N][ROBBED], dp[N][NOT_ROBBED]);
    }
}
```

##### 优化: 滚动数组
用now, old代替一维数组

### House Robber II
* 循环的房子 - 变为没偷房子0, 没偷房子N-1
* 圈的情况比序列复杂,所以一般要特殊处理搞头尾,变为序列的情况
```java
/*
Pretty much the same as House Robber I

Circle makes it hard, so we break it into two situation
We rob 0, and not N-1
We rob N-1, and not 0
*/
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        //Assume the last house is N-1
        //Not Rob N-1: We could rob 0..N-2
        //Not Rob 0:  We could rob 1..N-1
        int robFrom0 = rob(nums, 0, nums.length-2);
        int robFrom1 = rob(nums, 1, nums.length-1);
        return Math.max(robFrom0, robFrom1);
    }
    
    //The order is: prev2, prev1, num
    private int rob(int[] nums, int first, int last) {
        int prev2 = 0; //Will rob current house
        int prev1 = 0; //Will not rob current house
        for (int i = first; i <= last; i++) {
            int temp = prev1;
            prev1 = Math.max(prev2 + nums[i], prev1);
            prev2 = temp;
        }
        return prev1;
    }
}
```



### Best Time To Buy And Sell Stock - 1 time
* 要求:只能买卖**一次**
* 策略: 记录当天位置的最小值, 假如我第i天sell,我什么时候buy最好，类似于贪心

```java
/*
DP[i] = the profit of selling on day i
I will keep track of min purchase price I have seen so far
And compute the potential profit

*/
public class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int minPriceSoFar = Integer.MAX_VALUE;
        for (int price: prices) {
            minPriceSoFar = Math.min(minPriceSoFar, price);
            maxProfit = Math.max(maxProfit, price - minPriceSoFar);
        }
        return maxProfit;
    }
}
```

### Best Time To Buy And Sell Stock II - unlimited
* 要求: 可以买卖**任意多次**,但手头只能有一股
  * 一般含有**任意**最简单,因为不需要记录次数, 类似于背包问题, 反而是限制**K**次最难
* 策略: 贪心, 只要上升我就买
```java
class Solution {
    /*
    Almost greedy:
    
    I will sell as long as I can make a profit from previous day
    */
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] - prices[i-1] > 0) {
                maxProfit += prices[i] - prices[i-1];
            }
        }
        return maxProfit;
    }
}
```

### Best Time To Buy And Sell Stock III - 2 times
* 要求: 可以买卖**2次**,但手头只能有一股
  * 一般**1次**和**任意次**最简单,因为不需要记录次数
  * 比较难因为需要记录买卖多少次
* 状态
  * 不知道有没有买过,就记录下来
  * 分为五个阶段记录下来, 手中持有股票和手中无股票
  * f[i][j] - First i days (on Day i-1), we are in stage j, what's the maximum profit

### Best Time To Buy And Sell Stock IV - K times
* 要求: 可以买卖**K次**,但手头只能有一股
  * 一般**1次**和**任意次**最简单,因为不需要记录次数
  * 比较难因为需要记录买卖多少次
* 状态
  * 不知道有没有买过,就记录下来
  * 分为五个阶段记录下来, 手中持有股票和手中无股票
  * f[i][j] - First i days (on Day i-1), we are in stage j, what's the maximum profit

```java
/*
DP-coordinate
* State: 
  //I can buy from yesterday without making new transaction but pays the price, or continue to hold from yesterday
  * oneStock[i][k] = The maximum profit I can have on i-th Day, making at most k transaction, while have one stock left on hand
  //I can rest from yesterday's no Stock, or sell the stock and make a transaction to make profit 
  * noStock[i][k] = The maximum profit I can have on i-th Day, making at most k transaction, while have no stock left on hand
* Transition
  
  * oneStock[i][k] = noStock[i-1][k] - price[i]  //Buy today's stock
                     OR oneStock[i-1][k]         //Not buy today's stock
  * noStock[i][k] = oneStock[i-1][k-1] + price[i] //Sell today's stock
                    OR noStock[i-1][k]             //Not sell today's stock

* Init, boundary
   * oneStock[0][1] = -price[0]
   * noStock[0][1] = 0
   
* Result
  * i = 1..N-1, k = 1..K
  * return noStock[N-1][K]
  
* Optimization
  * If K >= N/2, then reduce Stock II with unlimited transaction
  * Rolling array to get rid of dimension i
*/

class Solution { 
    public int maxProfit(int K, int[] prices) {
        if (prices == null || prices.length == 0 || K <= 0) {
            return 0;
        }
        
        int N = prices.length;
        int maxProfit = 0;
        if (K >= N/2) {
            for (int i = 1; i < N; i++) {
                if (prices[i] - prices[i-1] > 0) {
                    maxProfit += prices[i] - prices[i-1];
                }
            }
            return maxProfit;
        }
        
        
        int[][] oneStock = new int[N][K+1];
        int[][] noStock = new int[N][K+1];
        
        for (int i = 0; i < N; i++) {
            for (int k = 1; k <= K; k++) {
                if ( i == 0) {
                    oneStock[0][k] = -prices[0];
                    noStock[0][k] = 0;
                } else {
                    oneStock[i][k] = Math.max(
                            oneStock[i-1][k], 
                            noStock[i][k-1] - prices[i]);
                    noStock[i][k] = Math.max(
                            oneStock[i-1][k] + prices[i], 
                            noStock[i-1][k]);
                }
            }
        }
        
        return noStock[N-1][K];
    }
}
```

##### 化简技巧
  * 如果K很大, 也就是 K > N/2 那么题目就可以简化为第二种，仿佛是无限次

#### 状态序列型小结
* 当思考动态规划最后一步时, 这一步的选择依赖于前一步的某种状态
* dp[i]代表的是
  * 序列型: 前i个(处理第i-1个)的结果
  * 坐标型: 第i个(处理第i 个)的结果

### Longest Increasing Subsequence [很popular]
* 状态: 以a[j]结尾的最长子序列长度
* 转移: f[j] = max{1, f[i] + 1 | FOR ALL i < j}
* 时间复杂度 O(N^2), 存在O(Nlog N)的做法
```java
/*
State:
  * Last step: I am at i, what's the LENGTH of LIS ending at i?
  * It could either be 1 (itself), or LIS ending at i-1, plus 1
  * State: dp[i] = longest length of LIS ending at i
Transition:
  * dp[i] = MAX { 1 OR dp[j] + 1 FOR j < i, and nums[j] < nums[i] }
*/

class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int N = nums.length;
        int[] dp = new int[N];
        int result = -1;
        for (int i = 0; i < N; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
            result = Math.max(result, dp[i]);
        }
          
        return result;
    }
}
```


### Russian Doll Envelope
##### 2D技巧：先排序
    * 对于不规律的首先要排序,这样起码先减少一个维度
    * 后面就只需要比较高度
* 状态
  * 第i个信封为最外层的信封,考虑次外层的信封j是哪个且j < i

```java
/*
Idea: Sort ascending for first element, sort descending for second element

See 300 Longest Increasing Subsequnce for more information
https://leetcode.com/problems/longest-increasing-subsequence/submissions/

Video
----
Best Explanation So far O(NlogN): https://www.youtube.com/watch?v=1RpMc3fv0y4

From Tushar:
O(N^2) using DP: https://www.youtube.com/watch?v=CE2b_-XfVDk

*/
class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        if (envelopes == null || envelopes.length == 0) {
            return 0;
        }
        
        int N = envelopes.length;
        
        //Sort envelopes: Increasing on width (first dim), decreasing on height (second dim)
        Arrays.sort(envelopes, (int[] pair1, int[] pair2) -> pair1[0] == pair2[0] ? pair2[1] - pair1[1] : pair1[0] - pair2[0] );
        
        //Run Longest increasing subsequence on heights
        int[] heights = new int[N];
        for (int i = 0; i < N; i++) {
            heights[i] = envelopes[i][1];
            System.out.println(heights[i] + " ");
        }
        
        //Longest subsequnce
        int[] dp = new int[N];
        int result = -1;
        for (int i = 0; i < N; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (heights[j] < heights[i]) {
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
            result = Math.max(result, dp[i]);
        }
        return result;
    }
}
```

#### 滚动数组和打印路径如何结合


## Lecture 4 - 划分型/博弈型/背包型

### Practice Question
- 划分型
* [LC279 Perfect Squares](https://leetcode.com/problems/perfect-squares)
* [LC132 Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii)
* [LINT437 Copy Books](https://www.lintcode.com/problem/copy-books/)
- 博弈型
* [LINT394 Coins in A Line](https://www.lintcode.com/problem/coins-in-a-line)
- 背包 -No leetcode
* [LINT92 Backpack](https://www.lintcode.com/problem/backpack) 可行性背包
* [LINT563 Backpack V](https://www.lintcode.com/problem/backpack-v) 计数型背包
* [LINT564 Backpack VI](https://www.lintcode.com/problem/backpack-vi) 计数型背包

#### 划分型
* 给定长度为N的序列或字符串,要求划分为若干段
  * 段数不限,或指定K段
  * 每一段满足一定的性质
* 做法
  * 类似于序列型, 但通常要加上段数信息
  * 一般用f[i][j]记录前i个元素(0..i-1)分为j段的性质,如最小代价  
* 重要性质
  * 切N刀变为N+1段
  * 分为N段需要N-1刀
* 划分型一定要有连续性, 例如Copy Book那道题
* 如果题目不指定段数, f[i]表示前i个元素分段后的可行性/最值, 可行性, 方式数 e.g.: Palindrome Partitioning
* 如果题目指定段数, f[i][j]表示前i个元素分成j段后的可行性/最值, 可行性, 方式数 e.g.: Copy books

### Perfect Square - 无段数信息
* State: 最后一步完全平方数j^2
  * 只需要知道n-j^2最小可以分为几个
* Transition: f[i] = min{f[i-j^2] + 1} for 1 <= j*j <=i
* Init: f[0] = 0
* Compute: f[1]..f[N], return f[N]
* Time complexity: O (sqrt(N)*N)

```java
class Solution {
    /*
    1. State
      * Last step: [1..N-2], looking at N-1
      * Sub: If I know j*j < N, then dp[N-1] = dp[N-1 - j*j] + 1
           I want to iterate through all j to find the min
      * State: dp[i] = min number of perfect square number of i
    2. Transition
      * dp[i] = 1 + MIN { dp[i - j * j] FOR 0 <= j * j <= i}
    3. Init
      * dp[0] = 0
      * dp[1] = 1
    4. Order
      * Normal
    */
    
    public int numSquares(int n) {
        int[] dp = new int[n+1];
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            dp[i] = i;
            for (int j = 2; j*j <= i; j++) {
                dp[i] = Math.min(dp[i], 1+dp[i-j*j]);
            }
        }
        
        return dp[n];
    }
}
```

### Palindrome Partitioning II - 无段数信息

* 切N刀变为N+1段
* 分为N段需要N-1刀

* State:
  * Last Step: [j..N-1] is Panlindrome
  * Subproblem: min number of panlindrome in [0..i-1]
* Transit
  * f[i] = min {f[j] + 1 | s[j..i-1] is palindrome, j IN 0 TO i-1}  
* Init:
  * f[0] = 0
* 答案是f[N]-1, 而不是最小的段数
  * 分为N段需要N-1刀
  * 切N刀变为N+1段

##### 回文串
```java
class Solution {
    /*
    1. State
      * Last step: Looking at last string [j, i], if it is a panlindrome, then the mincut is [0,j-1]+1
      * Child: What's the mincut for [0..j-1] 
      * dp[i] = Number of panlindrome of first i character making a cut at j. Last char is [j,i-1] is Panlindrome
    2. Transition
      * dp[i] = MIN { dp[j] + 1 FOR all j that [j,i-1] is Palindrome}
    3. Init and boundary
      * dp[0] = 0
      * dp[1] = 1
      * dp[2] = 1 IF PANLINDROME or 2 IF NOT PANLINDROME
    4. Order
      * Normal
      * Return dp[N] - 1; //dp[N] is the number of panlindrome, the cut would be dp[N]-1
    */
    
    private char[] cs;
    
    public int minCut(String s) {
        char[] cs = s.toCharArray();
        int N = s.length();
        boolean[][] isPalindrome = new boolean[N][N];

        //Build isPalindrome table
        for (int i = 0; i < N; i++) {
            //Center at i
            for (int left = i, right = i; left >= 0  && right < N && cs[left] == cs[right]; left--, right++) {
                isPalindrome[left][right] = true;
            }
            //Center at i,i+1
            for (int left = i, right = i+1; left >= 0  && right < N && cs[left] == cs[right]; left--, right++) {
                isPalindrome[left][right] = true;
            }   
        }
        
        //Use transition formula to build the dp table
        int[] dp = new int[N+1];
        dp[0] = 0;
        for (int i = 1; i <= N; i++) {
            dp[i] = i;
            for (int j = 0; j < i; j++) {
                if (isPalindrome[j][i-1]) {
                    dp[i] = Math.min(dp[i], dp[j] + 1);
                }
            }
        }
        return dp[N]-1;
    }
}
```


* 回文串分为两种: 假设字符串为N
  * 长度为奇数：从一个字符开始,两边扩展. 共N个字符
  * 长度为偶数: 以一条线(空串)开始,两边扩展. 共N-1个中心轴
     => 可以在N^2中判断所有回文串

```java
int i, j, c; 
//c is center character for odd-length
for (c = 0; c < N; c++) {
    i = j = c;
    while (i >= 0 && j < N && s[i] == s[j]){
        isPanlin[i][j] = true;
        --i;
        ++j;
    }
}

//c is center line for even-length
for (c = 0; c < N - 1; c++) {
    i = c;
    j = c + 1;
    while (i >= 0 && j < N && s[i] == s[j]){
        isPanlin[i][j] = true;
        --i;
        ++j;
    }
}
```

### Copy Books - 指定段数信息

技巧: 
* 如果K>N，则可以另 K= N，因为反正他们没有事情干
* 计算sum的时候j从后往前计算

State: 
 * f[k][i] 前K个抄写员最少需要多少时间抄写完前i本(第i-1本)书
Transition:
 * f[k][i] = min FOR j = 0...I {
     max {f[k-1][j], 
         A[j]+..+A[i-1]} } 
 * 你可以自由选择怎么去分数,但是你要告诉我谁最慢
Init:
 * f[0][0] = 0
 * f[0][i] = MAX_INFINITY，0个抄写员抄完几本书用无穷.
 * f[k][0] = 0
Order:
 * f[K][N]

#### 博弈型方式
* 先手:先出招的一方
* 博弈动态规划是唯一一个从第一步来进行分析的，而不是最后一步
  - 因为局面越来越简单
* 必胜vs必败
  * 必胜:在当前的局面走出一步,可以让对手无路可走
  * 必败: 自己无路可走

### Coins in a line
* State:
  * 设f[i]为面对i个石子 - 拿走一个或者两个都可以让对手必败
* 状态: 
    f[i] = TRUE f[i-1] == FALSE OR f[i-2] == FALSE
        | FALSE f[i-1] == TRUE AND f[i-2] == TRUE
* Init
  * f[0] = FALSE
  * f[1] = f[2] = TRUE

#### 背包型问题 - 数组大小一定与总承重M有关 
* 背包问题中, 数组大小一定与总承重M有关
* 独特类型, 思考方式很不一样
* 最后一步
  * 最后一个背包内的物品是哪个(无顺序)
  * 最后一个物品有没有进背包(有顺序)


### Backpack - 可行性背包 - 每个物品可取1次能否放满背包
* 1.确定状态 - 需要知道N个物品能否拼出重量W(W = 0, 1,..W)
  * 最后一步: 最后一个物品(重量A[N-1])能否进入背包
    * 情况一: 如果前N-1个物品能拼出W，那么前N个物品也能拼出W
    * 情况二: 如果前N-1个物品能拼出W-A[N-1], 那么加上最后一个物体也能拼出W
  * 状态 f[i][w]=true/false 能否**前i个**（第i-1个）物品拼出重量w
  * 常见错误: f[i]为前i个物品能拼出的最大重量(不超过target)
    * 反例: A=[3 9 5 2]，target = 10, 求出来为9，但实际为10
    * 原因: 最优策略中,前N-1个物品拼出出来的**不一定**是不超过Target的最大重量
* 2. Transit
  * f[i][w] = f[i-1][w] OR f[i-1][w-a[i-1]]
* 3. Init and Bondary
  * f[0][0] = true
  * f[0][1..M] = false
  * 边界: f[i-1][w-A[i-1]]只能在 w >= A[i-1]时使用
* 4. 顺序
  * 初始化: 前0个物品可以拼出哪些重量
  * 前一个物品可以拼出哪些重量
  * 前二个物品可以拼出哪些重量
  * ..
  * 前N个物品可以拼出哪些重量
  * 答案: f[N][Target]

#### Backpack V - 计数型背包 - 每个物品可取1次几种方式放满背包
* 隐含着的背包: 数组之和为target
* 1.确定状态 - 需要知道N个物品能否拼出重量W(W = 0, 1,..W)
  * 最后一步: 最后一个物品(重量A[N-1])能否进入背包
    * 情况一: 如果前N-1个物品能拼出W，那么前N个物品也能拼出W
    * 情况二: 如果前N-1个物品能拼出W-A[N-1], 那么加上最后一个物体也能拼出W
  * 情况1+情况2
 * 2. Transit
  * f[i][w] = f[i-1][w] + f[i-1][w-A[i-1]] 
* 3. Init and Bondary
  * f[0][0] = 1
  * f[0][1..M] = 0
  * 边界: f[i-1][w-A[i-1]]只能在 w >= A[i-1]时使用
* 4. 顺序
  * 初始化: 前0个物品可以拼出哪些重量
  * 前一个物品可以拼出哪些重量
  * 前二个物品可以拼出哪些重量
  * ..
  * 前N个物品可以拼出哪些重量
  * 答案: f[N][Target]
##### 优化
  * f[i][w] = f[i-1][w] + f[i-1][w-A[i-1]] 
  * 从后往前算就可以只用一维数组
  * 按照f[i][Target] .. f[i][0]的顺序更新

### Backpack VI - 计数型背包 - 每个物品可取多次几种方式放满背包
* 状态:
  * 看似更难, 其实更简单
  * 最后一步: 可以是任意物品
  * 子问题: f[w] = 有多少组合可以拼出w 
* 转移方程:
  * f[w] = f[w-A[0]] + f[w-A[1]] + .. + f[w-A[N-1]]

## Lecture 5 - 背包型/区间型

#### Practice Question
- 背包 -No leetcode
* [LINT125 Backpack II](https://www.lintcode.com/problem/backpack-ii) 最值型背包
* [LINT440 Backpack III](https://www.lintcode.com/problem/backpack-iii) 最值型背包
- 区间型
* [LC516 Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence)
* [LINT396 Coins In A Line III](https://www.lintcode.com/problem/coins-in-a-line-iii)
* [LC87 Scramble String](https://leetcode.com/problems/scramble-string)
* [LC312 Burst Balloons](https://leetcode.com/problems/burst-balloons)


### Backpack II - 最值背包 - 物品只有1个带走物品的最大价值
* 1.确定状态 - 需要知道N个物品能否拼出重量W(W = 0, 1,..W)
  * 最后一步: 最后一个物品(重量A[N-1])能否进入背包
    * 情况一: 如果前N-1个物品能拼出W，最大价值为V, 那么前N个物品也能拼出W,最大价值为V
    * 情况二: 如果前N-1个物品能拼出W-A[N-1], 最大价值为Vx, 那么加上最后一个物体也能拼出W, 价值为V2+V[N-1]
  * 两种中选择总价值最大的方案
* 2. 转移
  * f[i][w] = MAX(f[i-1][w], f[i-1][w-A[i-1]] + V[i-1] | 能拼出 且 不越界)
* 4. 顺序
  * 答案: f[N][0..w]的最大值

### 【最难 最重要】Backpack III - 最值背包 - 物品可取无数个带走物品的最大价值 
* 1.状态: 类似于背包2
   * **前N-1`个`**背包变为**前N-1`种`**背包，然后枚举可以拿多少个
* 2. 转移:
   f[i][w] = MAX(f[i-1][w-k*A[i-1]] + k*V[i-1] | k >= 0 且 能拼出 且 不越界)
##### 优化
  * 从前往后计算weight 可以进行时间上的优化
  * 优化: `f[i][w] = MAX(f[i-1][w], f[i][w-A[i]] + V[i-1])`  第二项为用前`i`种种物品拼出w-A[i-1]
  * 变为一维数组 从前往后计算

####区间型问题 -  想不出就直接记忆化搜索

* 考虑去头还是去尾巴
* 按照区间长度来扩展, 
  * 不能按照i的顺序去算
  * 按照长度j-i从小到大的顺序


### Longest Palindromic Subsequence
```java
public class Solution {
    /*
    Range type DP
    1. State:
      * Last step: Looking at [i,j]
         if s[i] == s[j], dp[i+1, j-1] + 2
         else dp[i+1][j] or dp[i][j-1] //No char at i, or no char at j
      * Sub: what's the LPS at [i+1,j-1]
      * dp[i][j] = longest palindromic subsequnce starting at i and end at j
    2. Transition
      * dp[i][j] = dp[i+1][j-1] + 2 IF s[i] == s[j]
                 | MAX(dp[i+1][j], dp[i][j-1])
    3. Init
    4. Order
       * length is the number of chars
       * Range length based: len = j - i + 1; j = i + len - 1; i < N - len
    */
    
    public int longestPalindromeSubseq(String s) {
        int N = s.length();
        char[] cs = s.toCharArray();
        int[][] dp = new int[N][N];
    
        //Len is the length of substring
        for (int len = 1; len <= N; len++) {
            for (int i = 0; i <= N - len; i++) {
                int j = i + len - 1;
                if (len == 1) { //Base for single char palindrome
                    dp[i][j] = 1;
                } else if (len == 2) { //Base for double char palindrome
                    if (cs[i] == cs[j]) {
                        dp[i][j] = 2;
                    } else {
                        dp[i][j] = 1;
                    }
                } else { //Transition for len >= 3
                    if (cs[i] == cs[j]) {
                        dp[i][j] = dp[i+1][j-1] + 2;
                    } else {
                        dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]);
                    }
                }
            }
        }
        return dp[0][N-1];
    }    
}
```


1. 状态:
  * 情况1: 回文串长度是1, 即一个字母
  * 情况2: 回文串铲毒大于1, 那么必有T[0] = T[M-1]
    * 设T[0]是s[i], T[M-1]是s[j]
    * 那么s[i+1, j-1]仍是最长回文子串 if s[i] == s[j]
    * 否则就是s[i,j-1]和s[i+1,j]中的最大
2. 转移方程
  * f[i][j] = max{f[i+1][j], f[i][j-1], f[i+1][j-1]+2 | S[i] = S[j]}
3. 初始条件
  * f[i][i] = 1
  * S[i] == S[i+1], f[i][i+1] = 2
  * S[i] != S[i+1], f[i][i+1] = 1
4. 计算顺序: 按照长度len = j-i+1来计算[i,j]
 

##### 区间模板

```java
int[][] dp = new int[N][N]; //dp[n][n]因为我们需要的是两个端点 [i,j]
//enumerate all len = [1 .. N]
//i = [0, 1, 3, ... n - len]
for (int len = 1; len <= N; len++) {
    for (int i = 0; i <= N - len; i++ ) {
        int j = i + len - 1;
        //Compute for [i,j]
    }
}
```

##### 如何打印出来最长子序列
* 开Pi数组记录每一步是去头还是去尾还是都去掉了, 然后把东西逆序回来

##### 记忆化搜索
* 区间搜索适合用记忆化搜索,因为递推方式的便利方式很奇怪
* 每次储存计算过的结果
* 递推方法从下而上, 记忆化搜索从上而下
* 递推方式可以进行空间优化例如滚动数组, 而记忆化搜索必须搜索全部

### Coins In A Line III
* 博弈目标: 己方数字和为A，对手数字和为B， 目标为A >= B, 等价于A - B >= 0
* 对于X: Sx = A - B, Sy = B - A, note that Sx = -Sy
* 一直对手为Sy 那么我的数字之和为Sx = -Sy + nums
* 状态:
```
  f[i][j] = max { -f[i+1][j] + a[i], //我取头, 对手取[i+1..j]的和
                  -f[i][j-1] + a[j]  //我取尾, 对手取[i..j-1]的和
                }
```
* 初始条件
 * 区间长度为1, 我可以取走唯一的

### Scramble String - 四维数组 必会
* 确定状态:
  * f[i][j][k] = 以S[i]开头长度为k的数组是否是T[j]开头长度为k的数组的scramble

```
class Solution {
    /*
    Brutal force:
    Is TRUE if for any position i, 
                s1[0..i] is scamble to s2[0..i] 
            AND s1[i+1..len-1] is scamble to s2[i+1..len-1] 
      OR
                s1[0..i] is scamble to s2[len - i .. len - 1] 
            AND s1[len - i..len-1] is scamble to s2[0 .. i] 
    OTHERWISE false
    
    */
    public boolean isScramble(String s1, String s2) {
        //System.out.println("Looking at <" + s1 +"> and <" + s2 + ">");
        int m = s1.length();
        if (s1.length() != s2.length()) {
            return false;
        }
        if (m == 0) {
            return true;
        }
        if (s1.equals(s2)) {
            return true;
        }
        
        char[] cs1 = new char[26];
        char[] cs2 = new char[26];
        for (char c: s1.toCharArray()) {
            cs1[c-'a']++;
        }
        for (char c: s2.toCharArray()) {
            cs2[c-'a']++;
        }
        for (int i = 0; i < 26; i++) {
            if (cs1[i] != cs2[i]) {
                return false;
            }
        }
        
        //See if any split can make it a scramble, otherwise false
        for (int i = 1; i < m; i++) {
            if (isScramble(s1.substring(0, i), s2.substring(0, i))
               && isScramble(s1.substring(i), s2.substring(i))) {
                return true;
            }
            if (isScramble(s1.substring(0, i), s2.substring(m-i))
               && isScramble(s1.substring(i), s2.substring(0, m-i))) {
                return true;
            }
            
        }
        return false;
    }
}
```

### 【HARD】Burst Balloons - 典型矩阵相乘题 必会
```
class Solution {
    /*
    Range DP
    * State: 
      * Last step: in range [i,j], I will last burst k, I will have nums[i]*nums[k]*nums[j] coins
                    PLUS nums[i,k] and [k,j]
      * dp[i][j] = MAX COIN that can be obtained in (i, j) not bursting i, j
    * Transition
      * dp[i][j] = MAX of dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j] for i < k < j
    * Init
    * Order
       * len: num of points, 3 ... N-1
       * i = 0 .. N - len
       * result = [0][N-1]
      
    */
    public int maxCoins(int[] nums) {
        int N = nums.length + 2;
        //Pad 1 at the begin and end of nums
        int[] balloons = new int[nums.length + 2];
        for (int i = 0; i < nums.length; i++) {
            balloons[i+1] = nums[i];
        }
        balloons[0] = 1;
        balloons[N-1] = 1;

        int[][] dp = new int[N][N];
        for (int len = 3; len <= N; len++) {
            for (int i = 0; i <= N - len; i++) {
                int j = i + len - 1; // [i, j]
                dp[i][j] = 0;
                for (int k = i + 1; k < j; k++) {
                    dp[i][j] = Math.max(dp[i][j], dp[i][k] + dp[k][j] + balloons[i] * balloons[k] * balloons[j]);
                }
            }
        }
        return dp[0][N-1];
    }
}
```

#####  消去型
* 消去型:删除之后不相邻的变为相邻的 一定不要按照题目的意思去想，否则你还要去记录谁去了哪里, 没法去解决问题了
* 一定从最后一步去想,按照最后选择的那个元素去分成两个区间,左右两个区间是独立的, 因为他们从来没有相邻过
* 例如矩阵相乘, 要想最后一个矩阵是谁和谁相乘
* 这道题去想扎最后一个中间的气球是怎样的, 自然就分成了两个区间
* 这是典型的矩阵链乘DP的问题: https://leetcode.com/problems/Burst-Balloons/discuss/167057/Simple-Matrix-Chain-Multiplication.-Only-one-condition-changed-!!

* 状态:
  * 最后一步: 一定有一个气球被扎破, 假设编号为i
    * 扎破时候, 左边是0, 右边是N+1, 获得a[i]
    * 知道左边[1..i-1]最多的金币数和右边[j+1，N]
  * 状态dp[i][j]代表扎破[i+1,j-1]号气球最多获得的金币数
    * 为什么offset 1? 因为左右两边的气球都不可以扎  
* 转移:
  $f[i][j] = max_{1<k<j} {f[i][k] + f[k][j] + a[i] * a[k] * a[j]}$
  * 注意i,j不能扎破
* 初始条件: 没有气球可以扎破, 最多获得0枚金币
  * f[0][1] = f[1][2] = .. = f[N][N+1] = 0

* 本题关键点: 把数组变为N+2,然后区间的两个端点不要扎


## Lecture 6 - 双序列型

#### 双序列
* 每给字符串长度分别为一个维度

#### Practice Question
* [LINT 77 Longest Common Subsequence](https://www.lintcode.com/problem/longest-common-subsequence)
* [LC97 Interleaving String](https://leetcode.com/problems/interleaving-string)
* [LC72 Edit Distance](https://leetcode.com/problems/edit-distance)
* [LC115 Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences)
* [LC10 Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching)
* [LC44 Wildcard Matching](https://leetcode.com/problems/wildcard-matching)
* [LC474 Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes)

### Longest Common Subsequence - 超级有名,必会
* 状态
  * 最后一步: 
    1. A中的最后一个字符M不在公共子串
    2. B中的最后一个字符N不在公共子串
    3. 两个字符相同,在公共子串, 则最长为M-1和N-1中的最长子序列
    4. 两个都不在, 已经为1,2包含了
  * 因为我们在求最长, 而不是方式数,所以重叠没有关系
  * 状态 f[i][j]为A**前i个**A[0..i-1]和B**前j个**B[0..j-1]的最长公共子串

##### 如何输出
记录每次的选择结果

### Interleaving String

* 状态
  * 最后一步: 看X中的最后一个字符,
       Case 1: 从A[0..A-2], B[0..B-2], 和X[0..X-2] interleave
    OR Case 2: 从B来: A[0..A-1], B[0..B-2], 和X[0..X-2] interleave
  * 子问题 subA, B, X是不是interleaving string
  * dp[i][j]: 前i个字符 和前j个字符是substringmatch前i+j个
* Transition
   dp[i][j] = (dp[i-1][j] && A[i-1] == X[i+j-1]) || (dp[i][j-1] && B[j-1] == X[i+j-1])
* Init
  dp[0][0] = true 交错形成了空串
  dp[0][j] = dp[0][j-1] && B[j-1] == X[j-1] 只看情况2
  dp[i][0] = dp[i-1][0] && A[i-1] == X[X-1] 只看情况1

### Edit Distance
* 状态
  * 最后一步: A[0..A-1], B[0..B-1]
  * 看A和B的最后一个字符
    * 有A无B 删除A: A[0..A-2] + B[0..B-1] + 1
    * 无A有B 增加A: A[0..A-1] + B[0..B-2] + 1
    * 有A有B 相等: A[0..A-2] + B[0..B-2]
    * 有A有B 替换A: A[0..A-2] + B[0..B-2] + 1
  * State: d=[i][j] first i in A and first j in B, what's the min distance
* Transition
   d[i][j] = min{d[i-1][j] + 1, d[i][j-1] + 1, dp[i-1][j-1] + 1, dp[i-1][j-1] IF A[i-1]==B[j-1]}
* Init
  dp[0][0] = 0
  dp[i][0] = i
  dp[0][j] = j
* Order

### Distinct Subsequences
* 状态: A[0..A-1], B[0..B-1]，looking at last char at A and B
    * 我知道A[0..A-2]和B[0..B-2] 
    * a != b: A[0..A-2]B[0..B-1] //B不和A连
    * a == b: A[0..A-2]B[0..B-2]  //B和A连
  * dp[i][j] = Distinct subsequenc of first i char in A and first j char in B makes
* Transtion
  * f[i][j] = f[i-1][j-1] IF A[i-1]==B[j-1] + f[i-1][j]
* Init
  * dp[i][0] = 1 <= 看谁会用到dp[i][0]根据那个来设值 不能瞎猜
  * dp[0][j] = 0

##### 滚动数组优化

### Regular Expression Matching
* 存在型DP 
* State
  * Last step: Text[1..i] Pattern[1..j]  For last character i in Text.
    * T[i] == P[j] | . : Text[1..i-1], Pattern[1..j-1]
    * P[j] == * : 
        * Text does not match P[j-1], see if whole text matches P[1..j-2]
        * Text matches P[j-1], see if Text[i-1] matches P[1..j]
  * Child: Does Text[1..i-1] or Pattern[1..j-1] match
  * State: dp[i][j] = first i chars in Text matches first j chars in Pattern
* Transition
  * dp[i][j] = dp[i-1][j-1] IF T[i-1] == P[j-1] or P[j-1] == '.'
             OR dp[i][j-2] IF P[j-2][j-1] == 'c*'  and
             OR dp[i-1][j] IF P[j-2] = '.' OR P[j-2] == T[i-1]
* Init
  * dp[0][0] = true
  * dp[i][0] = false
* Order: regular

### Wildcard Matching
* State
  * Last step: Text[0..i-1] Pattern[0..j-1]
    * Pattern[j-1] == '?': Pattern[0..j-2] matches text[0..i-2]
    * Pattern[j-1] == '*': 
         Matches 0: Text[0..m-1] matches Pattern[0..j-2]
         Matches any: Text[0..m-2] matches pattern[0..j-1]
    * Pattern[j-1] = c:
         Matches: Text[0..m-2] matches Pattern[0..j-2]
         No match: false
* Transition
 dp[i][j] = f[i-1][j-1]    IF i - 1 >= 0, and B[j-1]='?' or A[i-1]=b{j-1}
        OR (f[i-1][j] OR f[i][j-1]   IF B[j-1]='*')
* Init
f[0][0] = true
f[1..M][0] = false          

##### 如何打印*匹配了哪些
用pi数组

##### 双序列总结
* 突破口
  * 串A和串B的最后一个字符是否匹配
  * 是否需要串A/B的最后一个字符
  * 缩减问题规模
* 数组下标
  * dp[i][j] = 序列A前i个, 序列B前j个
* 初始条件和边界条件
  * 空串如何处理
  * 计数型（情况1+情况2+..)最值型(min/max{情况1, 情况2 etc}) 存在型(情况A and/or 情况B and/or ...)
* 匹配的情况下勿忘加1

### Ones and Zeroes - 类似于背包 但是是三维dp
* State: For the optimal solution, do I have the last string S_{t-1}
  Case I： No S_{t-1}, need to know first T-1‘s optimal solution
  Case II: Have S_{t-1}
    * Let T-1 have a 0s and b 1s
    * Need to know m-a 0s and n-b 1s can make ones and zeros
  State: dp[i][j][k]前i个01串最多能被多少个j个0和k个1组成
* Transition
  dp[i][m][n] = MAX{dp[i-1][j][k],
           dp[t][j-t0][k-t1] + 1 | j >= t0, k >= t1 }
DO NOT FORGET TO ADD 1
* Bounder and Init
* Result f[T][m][n]


## Lecture 7 - 综合型
* [LINT91 Minimum Adjustment Cost](https://www.lintcode.com/problem/minimum-adjustment-cost)
* [LINT89 K-Sum](https://www.lintcode.com/problem/k-sum)
* [LC300 Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)
* [LINT623 K Edit Distance](https://www.lintcode.com/problem/k-edit-distance)
* [LC403 Frog Jump](https://leetcode.com/problems/frog-jump)
* [LC639 Decode Ways II](https://leetcode.com/problems/decode-ways-ii)
* [LC221 Maximal Square](https://leetcode.com/problems/maximal-square)


### Minimum Adjustment Cost - 序列+状态=>2维数组
* NOTE: 如果没说1~100的范围, 那么就枚举Amin ~ Amax
* State:
  * Last Step: A change to B, let A[n-1] change to X, the cost is |A[n-1]-X|, |X-B[n-2]| <= Target
  * Need to know te result of A[0..N-2]'s minimum adjstment cost
  * but you don't know the value of X, so you have to write it down
    => Sequence with State
  * State: f[i][j] is the minimum adjustment cost of FIRST i elements to B, wher A[i-1] is changed to j
* Transition
  * f[i][j] = MIN OF f[i-1][k] + |j - A[i-1]|  FOR 0<=k<=100 AND j - target <= k  <= j + B[n-2]
* Init
  * f[1][j] = |j-1|

### K-Sum - 背包型
* Knapsack DP
  * State
    * Array: of weights, Target: maximum weight of backpack
    * dp[i][k][s] = Using first i objects to select k objects and make up to weight s
  * Transition
    * dp[i][k][s] = dp[i-1][k-1][s - nums[i]] | WITHIN BOUDNARY
                   + dp[i-1][k][s]
  * Init
     * f[0][-][-] = 0
     * Boundary: within subscript
  * Order
    * Regular
    * Return dp[N][K][Target]
    * Optimization: N*K*Target => K*Target

### Longest Increasing Subsequence - 优化为NlogN
* Original
   * dp[j] = max{1, dp[i] + 1 | i < j AND a[i] < a[j]}
   * Make a note that we always extend the dp[i] that's the largest one that's smaller than a[j]

### K Edit Distance - 树形DP - 本系列最难
* Keynote: If some string share a common prefix, then there dp[i][j] can be shared as well
  * Use Trie to lookup for prefix
  * How to share dp[i][j]? Use dp[前缀][j] to represent the minimum edit distance between a Prefix and a Target
* Sp = prefix, Sparent = parent of Sprefix
  f[Sp][j] = MIN OF f[Sp][j-1] + 1      => Insert
                  | f[Sparent][j] + 1   => Delete
                  | f[Sparent][j-1] + 1 => Swap
                  | f[Sparent][j-1] IF last = Target[j-1] 
* Init and boundary
  * f[Sroot][j] = f[""][j] = j
  * f[Sp][0] = length of Sp
* Computation
  * DFS for all f[Sp][0] .. f[Sp][n]
  * Result: f[Sp][N] <= K and Sp is a given word

```java
public class TrieNode {
    public TrieNode[] children;
    public boolean hasWord;
    public String word;

    public TrieNode() {
        children = new TrieNode[26];
        for (int i = 0; i < 26; i++) {
            son[i] = null;
        }
        hasWord = false;
    }

    static public void Insert(TrieNode p, String word) {
        for (int i = 0; i < word.legnth(); ++i) {
            int c = word.charAt(i) - 'a';
            if (p.children[c] == null) {
                p.children[c] = new TrieNode();
            }
            p = p.children[c];
        }

        //p is the node that contains word
        p.hasWord = true;
        p.word = word;
    }
}
```

### Frog Jump - 序列+哈希表
* State
  * 最后一步
    * 能否最后一步L跳到a[n-1]
    * Last jump is L-1, L, L+1 to a[i] = a[n-1]-L
  * 坐标+状态型
  * State: dp[i][j] can jump to stone i with jump j
* Transition
  * f[i][j] = f[k][j-1] OR f[k][j] OR f[k][j+1] | a[k] = a[i] - j
* Init
  * f[0][j] = true     

### Decode Ways II
* 情况1 - 最后一位匹配 - 讨论*
* 情况2 - 最后两位匹配 - 讨论*

### Maximal Square
* f[i][j] 以i,j为右下角的正方形的边长
* f[i][j] = MIN {f[i-1][j], f[i][j-1], f[i-1][j-1]} + 1
* return MAX f[i][j]^2


## 课程总结
* 常见类型
  * 坐标 - dp[i]对应nums[i]. i-th element
  * 序列 - dp[i]对应nums[i-1]. First i element
  * 划分 - what to do with the last section
  * 区间 - 按长度来计算
  * 背包 - 重量进维度
  * 最长序列型 - N^2 => NlogN
  * 博弈型 - 确定先手必胜态 
  * 综合型
* 如何学习
  * 先抄模板代码
  * 默写模板代码
  * 自由书写
* 模式
  * 确定状态
    * 确定最后一步 (博弈除外, 看第一步)
    * 化为子问题
  * 转移方程
    * 根据子问题定义直接得到
  * 初始条件和边界
    * 细心,考虑周全
  * 计算顺序
    * 利用之前的结果
  * 优化
    * 记忆化搜索好写但无法进行空间优化
    * 滚动数组 i%2和1-i%2
    * 打印solution: pi数组倒推
    * 背包的从左到右和从右到左压缩为一维