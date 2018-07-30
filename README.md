#Leetcode
Some classifications in questions worth reviewing  

## Algorithm  
- String Algorithms  
 - String search: 028 (passed with basic search; consider KMP)  
 - 635 Strings are comparable!

- Array Sum Questions  
 - 001 Unsorted Two Sum with O(n) time  
 - 015 Three Sum with O(n^2) time  
 - 016 Three Sum Closest  
 - 018 Four Sum  
 - 039 Combination Sum  
 - 040 Combination Sum 2  
 - 562 Methods to traverse a 2D array (matrix)

- Tricks
 - 011 Container with Most Water with O(n) time. Prove correctness.  
 - 004 Median of Two Sorted Arrays with O(log(n)) time  
 - 017 Letter Combination. Array traversal.
 - 020 How to recursively define validity of a parenthesis string and figure out a way to divide-and-conquer it easily?
 - 022 How to make a combo of bracket always balanced?  
 - 050 Power to a very large exponential.  
 - 102 (Java) Generics are not covariants [StackOverflow](https://stackoverflow.com/questions/24796273/incompatible-types-list-of-list-and-arraylist-of-arraylist)  
 - 659 Usage of Python collections and enumeration. Difference between subsequence and substring.  
 - 660 What does it mean by removing 9?  
 - 665 Decide if an array is non-decreasing (with <=1 anomaly)  
 - 667 Beautiful arrangement 2: construct a list of length n containing [1,n] where the abs differences between neighbors form exactly k distinct numbers  
 - Number elimination:
  - Original Joseph question: eliminate one, skip one, in circle. Memorize the solution (2*l+1 where l is the `Integer.largestOneBit(N)`)
  - 390 eliminate one, skip one, go backwards in array, repeat
  - 810 Chalkboard XOR game: A first, eliminate one number each time. If all numbers XOR to 0 A wins. Can A win?
 - 825 & 826 optimization.

- Conversions  
 - 008 atoi  
 - 012 013 Integer / Roman conversions  
 - 010 Regular Expression Matching  

- Searching and Sorting  
 - 278 Remember how to implement Binary search  
 - 33 Binary search: Two pointers pointing to the {pos 0 and pos length}, then while (j>i+1); ans is in mid=i. There can be other ways to do so: {pos 0 and pos length-1}, then while (j>i); ans is in i==j==mid==ans. See revised solution.  
 - 37 Backtracking search to solve Sudoku   
 - 638 Applying coupon to products.
 - 646 Sort a 2d primitive type array in Java and Python (Syntax!)  
 - 658 K-nearest elements of an array: Effecient code in Python  
 - 668 Find the kth largest number in the multiplication table.  

- Dynamic Programming  
 - 042 Trapping rain water (1D)  
 - 072 Edit Distance (2D)
 - 583 Longest Common Subsequence (and comparison with Longest Common Substring)  
 - 634 Array Dearrangement
 - 639 Decode ways 2. Figure out how to DP and write codes concisely.  
 - 801 Minimum swaps needed to make sequences strictly increasing.  
 - 813 Largest sum of averages of K adjacent groups

- Computational Geometry  
 - 587 Convex hull (implemented is Grahm's scan in Python)
 - 593 How to decide whether coordinates form a square  
 - 858 How to consider mirror reflection?  

## Data Structure
- Linked List  
 - 019 Remove the nth element (counting from the back) from a linked list, in a single pass  
 - 023 Merge k sorted linked lists. Usage of PriorityQueue

- String
 - 592 A simplified string to number calculator.

- HashSet
 - 036 Java: Use HashSet.add() return values smartly.

- Trie  
 - 209 Implement a basic Trie. Remember how to let it support "search" and "startsWith".  
 - 642 Auto-complete search. Do it with a Trie.
 - 648 Also a Trie problem.

- Graphs
 - 785 Bipartite graph
 - 787 Cheapest flights within k stops
 - 802 Search for eventually safe states
 - 815 Bus Routes
