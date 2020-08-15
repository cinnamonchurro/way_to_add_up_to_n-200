def solution(n):
    #Your code here
    #this is basically a code to find out how many different ways there are to add up to a particular integer using unique integers only
    #this is partitions of number theory and looking for unique partition
    #odd partition = distinct partition
    #maximum number of distinct numbers used is governed by triangular numbers 
    matrix=[[0]*(n+1) for i in range(n+1)]
    print(matrix)

solution(5)