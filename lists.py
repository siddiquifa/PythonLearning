members = ['asif','fahad','rehan','waqad']
print(members)
print ("The Guru of the group is "+ members[0].title())
members.append('shujaat')
print (members)
members.append('safwan')
print (members)
members.insert(6,'yasir')
print (members)
del members [6]
print (members)
popedmember= members.pop()
print (members)
members.insert(5,popedmember)
print (members)
print("Membership of "+popedmember+" is still doubtful")
members.pop(0)
print (members)

