Credit
https://iorilan.medium.com/after-900-leetcode-problems-here-is-what-i-learned-4d39b17e0853

## DFS
A classic way traverse tree or graph start from a node reach until end. or within a metrix finding the area by going up,down,left,right .usually every tree or graph or 0–1 metrix searching problem could be related to DFS .
## BFS
Unlike DFS. BFS could be done with queue .Find the next reachable nodes, add into queue until queue is empty. unlike DFS, BFS focus more on all “next nodes” from current “parents” queue.
## Binary Search
Within sorted array find some value , usually fall into this category .
## Heap
When find max or min , or topK issue . usually this structure is available in the language you choose, can directly use it . java, c#, python etc. if not you can also build your heap .
## Trie
Given dictionary , build the Trie , do word search or frequency .
## Stack
Use min or max stack to compare the top 1 in stack while looping through some array.
## Linklist
common problems are like find cycle, common node between 2 link list , reverse , etc .
## Greedy
The idea isto use “greedy thinking” find the maximum or minimum .
## Sliding window
use start and end position to track the “window” start and end position while looping array, need increase the start when match some condition ,usually need to track the window size also
## Two pointers
maintain 2 index while looping array or string
## Back Tracking
like DFS ,just that need loop through each possibilities for each recursion .This approach only useful for small amount of input values .
## Devide and conquer
The idea is to find a partitioner and devide the issue into smaller ones (e.g. left and right), find the answer for each of them and “merge” the sub-answers . e.g. quick-sort
## Union Find
“Group” the parents to the same “root-parent” while finding parent for child node
## Dynamic programming
There is an array to store “previous answers” . it may not be easy to come out with this approach in the first time . but when we solved some issue with DFS or back tracking ,then we may find “some issue solved there should be a cache for these previous answers” . this is when DP come to be a solution.
Another pattern is “bottom-up” . try solve the problem with small amount of numbers, see if the answer, the trying to reuse previous answer to solve the problem with more numbers added in.
## Topo sort
while traverse graph remove the “out degree=0”
## Bit manipulation
use bit operation to solve the issue . e.g. bit mask