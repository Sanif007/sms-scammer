with open("sess.txt","r") as file :
   first_line = file.readline()
   for last_line in file :
      pass
print("\033[94mFirst time used : \033[0m"+first_line)
print("\033[94mMost recently used : \033[0m"+last_line)
