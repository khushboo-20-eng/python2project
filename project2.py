#online voting system
#And options available for parties(BJP , CONGRESS , AAP)

print("voting system!")

print("complete registration first ! ") 

Name = input("Enter your name :")
voter_id = input("Enter voter id :")
password = input("Please enter a 8 characters : ")
party_name = input("Enter the name of party to vote ")


with open("vote.txt" , "a" )  as file :  # "a"  to avoid overrite
    file .write (f"{Name}   , {voter_id} , {password} , {party_name}\n")

with open("vote.txt" , "r") as file :
    print("The total registration of the people for vote :" , len(file.readlines()))


party_votes = {"BJP" : 0  , "congress" : 0 , "AAP" : 0 } 

with open ("vote.txt" , "r" ) as  file : 
    for line in file :
        party = line.strip().split(",")[-1].strip()

        if party in party_votes :
            party_votes[party] += 1 

        else :
            print(" ") 


print(party_votes)

print("\n")
print("ELECTION RESULTS ! ")
winner = max(party_votes , key=party_votes.get)
print("winning party :" , winner)










                
        
   
 






   






           




 

   

