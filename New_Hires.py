#index practice

new_member = "False"
answ = "False"
new_hire = "anon"
rep = "False"
repdemp = ""

team_1 = ["Mary", "Joe", "Sue", "Caroline", "Bob"]

print(team_1)

answ = input("Is there a new hire?: ")

if answ == "True":
  new_hire = str(input("Who is the new hire? "))
  rep = input("Is someone bring replaced? ")
  if rep == "True":
      repdemp = str(input("Who is being replaced? "))
      if repdemp == "Mary":
          team_1.pop(0)
          team_1.insert(0, new_hire)
      elif repdemp == "Joe":
          team_1.pop(1)
          team_1.insert(1, new_hire)
      elif repdemp == "Sue":
          team_1.pop(2)
          team_1.insert(2, new_hire)
      elif repdemp == "Caroline":
          team_1.pop(3)
          team_1.insert(3, new_hire)
      elif repdemp == "Bob":
          team_1.pop(4)
          team_1.insert(4, new_hire)
      else:
          print("incorrect input")
  else:
      team_1.append(new_hire)
    
print(team_1)
