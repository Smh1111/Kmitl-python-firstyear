def bubble_sort(list):
    for i in range(0, len(list) - 1):
       

        for j in range(0, len(list) - 1):

          if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                
                print(list)

        
     
    return list
    
def main():
    list1 = [3, 2, 9, 7, 8, 1, 4]
    print(bubble_sort(list1)) 

main()