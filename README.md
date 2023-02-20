# QuickSort_Pivoting_Strategy_Analysis
This project was my 3rd Homework for the course CMPE 300 (Analysis of Algorithms) at Bogazici University. This project focuses on four different implementation strategies for QuickSort algorithm and discusses their advantages &amp; disadvantages respectively.
## About the Project
In this project we have implemented four different versions of QuickSort algorithm. Then with the help of runtime data, we discusses their efficiency with respect to worst & average cases. The detailed information about the versions and the methodology about the project can be found on the description file.
Runtime data and the corresponding inputs can be found in the file 'VolkanOzturkAS1.pdf'. The general table and comments about the data can be found in the file 'VolkanOzturkAS2.pdf'.
Ver1: Classical deterministic algorithm. (Pivot chosen as the firts element of the array.)
Ver2: Randomized algorithm. (Pivot chosen randomly.)
Ver3: Randomized algorithm. (First, array is shuffled randomly, then same as the 'Ver1'.)
Ver4: Deterministic algorithm. (Pivot chosen with 'median of three' rule.)
## To Run the Code
First, one should decide following three HARDCODED specifications and change the code accordingly:
1) 'Case' : '1' for average case or '2' for the worst case.
2) 'IntType' : '1' (Each element of the list is an integer between 1 and 10 * n, chosen randomly.) '2' (Each element of the list is an integer between 1 and 0.75 * n, chosen randomly.) '3' (Each element of the list is an integer between 1 and 0.25 * n, chosen randomly.) '4' (All the elements are integer 1.)
3) 'n' : The number of elements in the array.
Then, one can run the code with:
```python3 tester.py```
The inputs and corresponding runtime date for four different versions of the algorithm will be printed on the console. For the average case ('Case' = '1') there will be five different inputs and for the average runtime data is calculated from their mean. For the worst case there will be just one input. for either case, there will be four different runtime statistics corresponding four different implementation strategies for the QuickSort algorithm. (ex: average1 depicts the Ver1 etc.)
## Final Note
The environment for the runtime data: Lenovo Thinkpad / OS: Ubuntu.
