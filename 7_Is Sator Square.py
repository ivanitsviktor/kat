





































def is_sator_square(tablet):
    for i in range(len(tablet)):
        for j in range(len(tablet)):
            if tablet[i][j]!=tablet[j][i]:
                print(tablet[i][j],tablet[j][i])
                return False
    for i in range(len(tablet)):
        for j in range(len(tablet)):
            if tablet[i][-1-j]!=tablet[j][-1-i]:
                print(tablet[i][-1-j],tablet[j][-1-i])
                return False
                       
    return True        
                
        
    
     
# print(is_sator_square([['B', 'A', 'T', 'S'],
#                      ['A', 'B', 'U', 'T'],
#                      ['T', 'U', 'B', 'A'],
#                      ['S', 'T', 'A', 'B']]))





































# def is_sator_square(tablet):

  

#     r=0
#     p=0
#     for i in range(len(tablet)):
#         for j in range(len(tablet)):
#             if tablet[i]==list(reversed(tablet[j])):
#                 for x in range(len(tablet)):
#                     tab=[]
#                     for y in range(len(tablet)):
#                         tab+=tablet[y][x]
#                     # revtab=list(reversed(tab))
#                     if tab==tablet[i]:
#                         for v in range(len(tablet)):
#                             tab2=[]
#                             for b in range(len(tablet)):
#                                 tab2+=tablet[-1-v][-1-b]
#                             if tab2==tablet[i]:
#                                 print(tablet[i], tab, tab2)
                                
#                 if r!=0:
#                     p+=1                    
                                
#     print(r,p)
#     if p==len(tablet)*len(tablet):
#         return True
#     else:
#         return False
                
                
  
# print(is_sator_square(tablet =[['T', 'E', 'N'],
#                   ['E', 'Y', 'E'],
#                   ['N', 'E', 'T']]))  
  
  
  
  
  
  
  
                
# # print(is_sator_square(tablet = 
# #                  [['S', 'A', 'L', 'A', 'S'],
# #                   ['A', 'R', 'E', 'N', 'A'],
# #                   ['L', 'E', 'V', 'E', 'L'],
# #                   ['A', 'R', 'E', 'N', 'A'],
# #                   ['S', 'A', 'L', 'A', 'S']]))                    
        



