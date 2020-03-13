# OOD

- [OOD](#ood)
- [Lecture 1 面向对象设计入门 - Elevator System - Strategy Pattern](#lecture-1-%e9%9d%a2%e5%90%91%e5%af%b9%e8%b1%a1%e8%ae%be%e8%ae%a1%e5%85%a5%e9%97%a8---elevator-system---strategy-pattern)
  - [小结](#%e5%b0%8f%e7%bb%93)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [5C解题法](#5c%e8%a7%a3%e9%a2%98%e6%b3%95)
  - [Design Elevator System](#design-elevator-system)
    - [Clarify](#clarify)
    - [Core Object](#core-object)
    - [Cases](#cases)
    - [Class](#class)
    - [Correctness](#correctness)
  - [Challenge](#challenge)
    - [Design Pattern: Strategy Pattern](#design-pattern-strategy-pattern)
- [Lecture 2 - 管理类OOD: Parking Lot & Restaurant - Singleton Pattern](#lecture-2---%e7%ae%a1%e7%90%86%e7%b1%bbood-parking-lot--restaurant---singleton-pattern)
  - [Clarify](#clarify-1)
  - [Core Object](#core-object-1)
  - [Cases - 站在管理员的角度想](#cases---%e7%ab%99%e5%9c%a8%e7%ae%a1%e7%90%86%e5%91%98%e7%9a%84%e8%a7%92%e5%ba%a6%e6%83%b3)
  - [Class & Correctness](#class--correctness)
  - [Design Pattern - Singleton](#design-pattern---singleton)
- [Lecture 3 - 预定类: Hotel & Airline Ticket](#lecture-3---%e9%a2%84%e5%ae%9a%e7%b1%bb-hotel--airline-ticket)
  - [餐馆OOD](#%e9%a4%90%e9%a6%86ood)
    - [Clarify](#clarify-2)
    - [Use Case & Classes](#use-case--classes)
  - [预定类OOD](#%e9%a2%84%e5%ae%9a%e7%b1%bbood)
  - [Hotel Reservation](#hotel-reservation)
- [Lecture 4 - 实物类: Vending Machine & Juke Box - Factory & Adaptor Pattern](#lecture-4---%e5%ae%9e%e7%89%a9%e7%b1%bb-vending-machine--juke-box---factory--adaptor-pattern)
  - [Vending Machine & ATM Machine](#vending-machine--atm-machine)
    - [State Design Pattern](#state-design-pattern)
  - [Coffee Machine](#coffee-machine)
    - [Decorator Design Pattern](#decorator-design-pattern)
  - [Kindle](#kindle)
    - [Factory Design Pattern](#factory-design-pattern)
- [Lecture 5 - 棋牌类: Black Jack & Chinese Chess](#lecture-5---%e6%a3%8b%e7%89%8c%e7%b1%bb-black-jack--chinese-chess)
  - [棋牌类解题思路](#%e6%a3%8b%e7%89%8c%e7%b1%bb%e8%a7%a3%e9%a2%98%e6%80%9d%e8%b7%af)
    - [TicTacToe](#tictactoe)
    - [Chinese Chess](#chinese-chess)
    - [牌类 - Blackjack](#%e7%89%8c%e7%b1%bb---blackjack)

# Lecture 1 面向对象设计入门 - Elevator System - Strategy Pattern

## 小结
* 管理类 - Parking Lot
  * Use Case: Reserve, Serve, Checkout
  * 技巧: 使用Receipt来储存relationship (Table vs People. Parking vs Car, Book vs Student)
* 预订类 - Restaurant, Hotel
  * Use Case: Reserve
    * Search, make reservation, cancel reservation
  * 技巧: Search criteria -> Search() -> List<Result> -> Select() -> Receipt
  * 技巧2: 利用LRU进行优化
* 实物类
  * ATM & Vending Machine - State 
  * Coffee Maker - Decorator
  * Kindle - Factory
* 棋牌类总结
  * Clarify : 玩家，规则，胜负，积分
  * Core object: Hand, Board, Deck/Table, Suit, ...
  * Use cases: Initialization / Play / Checkout
  * 对于牌类，需要从Player的角度出发


## 简介
* OOD特点
  * OOD在面试当中很重要, 尤其对于Intern和Entry level 
  * 题目没有标准答案, Everything is an object
  * 题目类型明显，可用固定的模板解题
* OOD面试中的陷阱
  * 起手式的陷阱: 自说自话 & 指鹿为马
  * 解题中的陷阱: 朝出夕改
  * 收手式的陷阱: 虎头蛇尾
* 评判OOD面试
  * S – Single responsibility principle
  * O – Open close principle
  * L – Liskov substitution principle
  * I – Interface segregation principle
  * D – Dependency inversion principle

## 5C解题法
* Clarify: 通过和面试官交流，去除题目中的歧义，确定答题范围
* Core objects: 确定题目所涉及的类，以及类之间的映射关系
* Cases: 确定题目中所需要实现的场景和功能
* Classes: 通过类图的方式，具体填充题目中涉及的类
* Correctness: 检查自己的设计，是否满足关键点

## Design Elevator System

### Clarify
* Overview
  * What: 针对题目中的**关键字**来提问, 通过名词的属性来考虑
  * How: 针对问题主题的**规则**来提问
  * Who: 以**系统**为主导
* What - 关键词
  * Elevator:
    * 电梯能够获取当前重量?
    * 客梯和货梯?
  * Building
    * 是否有多处能搭乘的电梯口?
* How - 规则
  * 当按下按钮时，哪一台电梯会相应
  * 当电梯在运行时，哪些按键可以响应
* Who 
  * 电梯系统如何获取每位乘客的重量

### Core Object
* 为什么要定义Core Object ?
  * 这是和面试官初步的纸面contract
  * 承上启下，来自于Clarify的结果，成为Use case的依据
  * 为画类图打下基础
* 如何定义Core Object ?
  * 以一个Object作为基础，**线性**思考
    * 只考虑input/output
  * 确定Objects之间的映射关系
* Good Practice
  * Use Access modifier
    * package - 尽量避免
    * public
    * private - 封装
    * protected - 继承
  * package
    * 如果什么都不声明，变量和函数都是package level visible
    * 在同一个package内的其他类都可以访问
    * 在类图中，避免使用default的package level access
    * 常用于写Unit Test

### Cases
* 为什么要写Use cases
  * 这是你和面试官白纸黑字达成的第二份共识，把你将要实现的功能列在白板上
  * 帮助你在解题过程中，理清条例，一个一个Case实现
  * 作为检查的标准
* 怎么写Use cases
  * 利用定义的Core Object, 列举出每个Object对应产生的use case.
  * 每个use case只需要先用一句简单的话来􏲼述即可
* ElevatorSystem
  * Handle request
* Request 
  * N/A
* Elevator
  * Take external request
  * Take internal request
  * Open gate
  * Close gate
  * Check weight
* ElevatorButton
  * Press button

### Class
* 为什么要画类图?
  * 可交付，Minimal Viable Product
  * 节省时间，不容易在Coding上挣扎
  * 建立在Use case上，和之前的步骤层层递进，条例清晰，便于交流和修改
  * 如果时间允许/面试官要求，便于转化成Code
* 怎么画类图?
  * 遍历你所列出的use cases
  * 对于每一个use case，更加详细的描述这个use case在做什么事情 
    * 例如:take external request
      * ElevatorSystem takes an external request, and decide to push this request to an appropriate elevator
  * 针对这个描述，在已有的Core objects里填充进所需要的信息
* Use case: Handle request
  * ElevatorSystem takes an external request, and decide to push this request to an appropriate elevator


### Correctness
* 从以下几方面检查:
  * Validate use cases (检查是否支持所有的use case)
  * Follow good practice (面试当中的加分项，展现一个程序员的经验)
  * S.O.L.I.D
  * Design pattern

## Challenge
* Q: What if I want to apply different ways to handle external requests during different time of a day?
* A: Use Strategy design pattern

### Design Pattern: Strategy Pattern

* 封装了多种 算法/策略
* 使得算法/策略之间能够互相替换


# Lecture 2 - 管理类OOD: Parking Lot & Restaurant - Singleton Pattern
* 管理类 - 题目后面都可以接上三个字: 管理员
  * e.g.: Gym, Parking lot, Restaurant, Library, Super market, Hotel
  * 设计一个模拟/代替管理员日常工作的系统
* 解题方法
  * Clarify: 除了题目中问的名词外，还需要从管理的名词来考
  * Core object: 有进有出
  * Cases: 从管理员角度考虑
    * Reserve: 预定
    * Serve: 服务
    * Checkout: 买单
  * Class: 经常可以使用**收据**的形式，来保管信息
  * Correctness

## Clarify
* What
  * 关键词: Parking lot, Vehicle, Parking Spot
  * Parking lot: 考虑多层的Parking lot, 没有错层
  * Vehicle: 考虑三种大小的车
  * 不考虑残疾人停车位/充电车位
* How
  * 规则1: 如何停车
    * 一定要从**停车场**的角度来考虑,而不是车的角度
      * 停车场: 开进停车场 -> 返回一个能停的地方 ->停进一个位 置
      * 车: 开进停车场 -> 经过每一个位置看看能不能停 -> 停进一个位置
  * 规则2: 付费
    * 免费还是付费
* Who: Optional

## Core Object
* Parking Lot
* Parking spot
* Car, Bus, Motorcycle
* 映射关系
  * Parking has a list of Spot
  * 错误方法: spot里面有car,或者parking lot有list of car

## Cases - 站在管理员的角度想
* Bus / Car / Motorcycle
  * N/A
* Parking Lot
  * Get available count (reserve)
  * Park vehicle (serve)
  * Clear spot (checkout)
  * Calculate price (checkout)
* Parking Spot
  * N/A

## Class & Correctness
* Draw UML per Use Case
* 从以下几方面检查:
  * Validate use cases (检查是否支持所有的use case)
  * Follow good practice (面试当中的加分项，展现一个程序员的经验)
  * S.O.L.I.D
  * Design pattern

## Design Pattern - Singleton

```java
public class ParkingLot {
  private static ParkingLot _instance = null;

  private List<Level> levels;

  private ParkingLost() {
    levels = new ArrayList<List>();
  }

  public static synchronized ParkingLot getInstance() {
    if (_instance == null) {
      _instance = new ParkingLot();
    }
    return _instance;
  }
}
```

* `synchronized getInstance()`使得Singleton线程安全
* `static _instance` 使得只有一个instance
* `private ParkingLot()`使得constructor只被调用一次

# Lecture 3 - 预定类: Hotel & Airline Ticket
## 餐馆OOD
### Clarify
* What
  * 管理: Party -> Restaurant -> Table
* How
  * 能否预约
  * 能否外送
* Who - Optional
  * 思考模式1: 过于复杂
    * Party 进入餐馆 -> Host指引到空桌 (find table) -> 一个waiter负责这桌客人 (assign waiter) -> 客人点菜 (take order) -> Chief 拿到order，按顺序做菜 (cook by order) -> Order做好后，waiter上菜 (serve order) -> 客人吃完后付钱 (check out)
  * 思考模式2
    * 客人进入餐馆，餐馆返回一个Table
    * 客人点菜，餐馆返回一桌菜
    * 客人付账，餐馆清空Table

### Use Case & Classes
* Restaruant
  * Find Table (serve)
  * Take Order (serve)
  * Checkout (checkout)

## 预定类OOD
* 题库
  * Restaurant reservation system
  * Hotel reservation system
  * Flight/Bus/Train reservation system
* 解题思路
  * What: 考虑预定的东西
  * Use Case = Reserve
    * `Search Criteria` -> `search()` -> `List<Result>` -> `select()` -> `Receipt`
      * `Reservation findTableForReservation(Time slot) throws NoTableForReservationException`
      * `void confirmReservation(Reservation reservation)`

## Hotel Reservation
* Can you design a hotel reservation system
* What
  * 是为一间酒店设计预定房间系统，还是先选择酒店的系统?
  * 搜索条件区别: 人数+时间 VS 人数+时间+地址
  * Search criteria -> Search() -> List<Result> -> Select() -> Receipt


# Lecture 4 - 实物类: Vending Machine & Juke Box - Factory & Adaptor Pattern
* 实物类OOD题型
  * Vending machine
  * Jukebox
  * CD Player
  * Coffee maker
  * ATM
* 实物类
  * 考虑对于实物的输入输出
* 技巧
  * State pattern 
  * Decorate pattern 
  * Factory pattern

## Vending Machine & ATM Machine

### State Design Pattern
* States
  * HAS_SELECTION - NO_SELECTION
  * COINS_INSERTED - NO_COIN
  * SOLD
  * SOLD_OUT
* State related actions:
  * select item
  * insert coin
  * execute transaction
  * cancel transaction
  
```java
public interface State {
    public oid selectItem(String selection);
    public void insertMoney(int value);
    public void executeTransaction();
    pulic int cancelTransaction();
}

public class NoSelectionState implements State {
  VendingMachine vendingMachine;

  public NoSectionsState(VendingMachine vendingMachine) {
    this.vendingMachine = vendingMachine;
  }

  //Implement, and change state
  @Override
  public void selectItem(String selection) {
    vendingMachine.setSelectedItem(selection);
    vendingMachine.changeToHasSelectionState();
  }
}

public class VendingMachine {
  private State state;
  private NoSelectionState noSelectionState;
  privte HasSelectionState hasSelectionState

  //Constructor: init all state, and set inital state
  public VendingMachine() {
    noSelectionState = new NoSelectionState(this);
    hasSelectionState = new hasSelectionState(this);
    state = noSelectonState;
  }

  //Expose to other State class for changing 
  public void changeToHasSelectionState() {
    state = hasSelectionState();
  }

  //API, use different state to implement
  public void selectItem(String selection) {
    state.selectItem(selection);
  }
}
```

## Coffee Machine

### Decorator Design Pattern

```java
public interface Coffee {
  public double getCost();
  public String getDescripton();
}

public class Expresso implements Coffee {
  public Expresso() {
    description = "Expresso";
  }

  public float getCost() {
    return 1.99;
  }

  public String getDecription() {
    return description;
  }
}

public abstract class CoffeeDecorator implements Coffee {
  protected final Coffe decoratedCoffee;

  public CoffeeDecorator(Coffee c) {
    this.decoratedCoffee = c;
  }

  public double getCost() {
    return decoratedCoffee.getCost();
  }

  public double getDescription() {
    return decoratedCoffee.getDescription();
  }
}

public class WithMocha extends CoffeeDecorator {
  public WithMocha(Coffee coffee) {
    super(c);
  }

  public String getDescription() {
    return super.getDescription() + ", Mocha";
  }

  public float getCost() {
    return super.getCost() + 0.5;
  }
}

public void test() {
  Coffee c = new Expresso();
  c = new WithMocha(c);
  c = new WithMocha(c);
  // Expresso, Mocha, Mocha $2.99
  System.out.println(c.getDescription() + "$ " + c.getCost());
}

```

## Kindle
### Factory Design Pattern
* Simple Factory: 将if-else放入一个单独的factory里面
* Factory method
* Abstract Factory


# Lecture 5 - 棋牌类: Black Jack & Chinese Chess

## 棋牌类解题思路
* 特点 - Clarify
  * 玩家
  * 规则
  * 胜负
  * 积分
* 术语 - Core Object
  * Board 
  * Suit 
  * Hand
* State - Use Case
  * Initialization (摆盘，洗牌...)
  * Play (下棋，出牌...)
  * Win/Lose check (胜负结算) + Tie (流局)

### TicTacToe
```java
//Simulator.java
makeMove(1,1)

//TicTacToe.java
public void makeMove(int row, int col) {
  board.makeMove(row, col, currentMove);
  if (board.checkWin()) {
    print (currentMove + " win!");
  } else if (board.isBoardFull()) {
    print("It's a tie");
  }
  changePlayer();
}
```

### Chinese Chess
* 特点 - Clarify
  * 玩家
  * 规则
  * 胜负
  * 积分
* 术语 - Core Object
  * Board 
  * Suit 
  * Hand
* State - Use Case
  * Initialization (摆盘，洗牌...)
  * Play (下棋，出牌...)
  * Win/Lose check (胜负结算) + Tie (流局)

### 牌类 - Blackjack
* Core Objects - 牌类较为固定的framework
  * Hand, Player, Dealer, Card, Deck
* Use Case
  * Initialization (摆盘，洗牌...)
    * Join table
    * Place bet
    * Get initial cards
  * Play (下棋，出牌...)
    * Deal
    * Increase bet
    * Stop dealing
  * Win/Lose check (胜负结算) + Tie / Draw (平局)
    * Compare score
    * Take/Lose bets
