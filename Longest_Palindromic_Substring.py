# Python Program to check longest palindromic substring

def Longest_Palindromic_Sub_String():
    # List=[1,2,3,1]
    # print(List[0:len(List)-1])
    # print(List[-1])
    List1=[]
    Palindromic_SubString=""
    Longest_Palindromic=""
    Input= "cbwoowddggdd"
    for char in Input:
        if len(List1)==0:
              List1.append(char)
        elif len(Palindromic_SubString)>0 and List1[-1] != char:
          if len(Longest_Palindromic)< len(Palindromic_SubString):
              Longest_Palindromic=Palindromic_SubString
          Palindromic_SubString=""
          List1=[]
          List1.append(char)
        elif List1[-1]!=char:
            List1.append(char)
        else:
            List1=List1[0:len(List1)-1]
            Palindromic_SubString= char+ Palindromic_SubString+ char
    if len(Longest_Palindromic)< len(Palindromic_SubString):
        Longest_Palindromic=Palindromic_SubString
    print(Longest_Palindromic)
Longest_Palindromic_Sub_String()
    
    


