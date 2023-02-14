1. Reverse a string using slice  
 > mystring[::-1]  
 > mystring[start:end:stepsize] ( ends at end -1 )  
  
 ** Strings are immutable   
 
2. b = None
   myset = {1,2,3}
   mylist = [1,2,4,5]
   myTuple = (1,2,[a,a],5)
   
3. with open('myfile.txt',mode = 'w+') as myfile:
       content = myfile.read()
       myfile.seek(0) // cursor backto first
        
     [ modes = r | w | a | r+ | w+ ]
     
4. enumerate  
  for index,letter in words:  
      print(f'{index}' - 'letter')  
      
     0 - S  
     1 - A  
     2 - T  
     
5. zip 
   for item in zip(list1,list2)  
       print(item)  
     
     [(1,a),(2,b),(3,c)]   
     
     zipping into tupples to lowest list length
       
6.   'in' Iterable  
      a in list == True  

7. List Comprehension :
   mylist = [ (listItem*2) for listItem in range(0,10) if listItem%2==0]   