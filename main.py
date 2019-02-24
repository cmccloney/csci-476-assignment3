import os
import hashlib

'''file = open("wordlist.txt","w")
for i in range(0,200000):
    file.write("%s:" % str(i))
    obj = str(i)
    file.write("%s\n" % hashlib.md5(obj.encode()).hexdigest())
file.close()'''

'''file = open("rockyou.txt","r",encoding="utf8")
file_w = open("hashed_rock.txt","w",encoding="utf8")
for i in file:
    string = i.split("\n")
    file_w.write("%s:" % string[0])
    file_w.write("%s\n" % hashlib.md5(string[0].encode()).hexdigest())
file.close()
file_w.close()'''

passwords = open("passwords.txt","r")
list = []
for y in passwords:
    string = y.split("\n")
    list.append(string[0])
passwords.close()

dicti = open("wordlist.txt","r")
cracked = open("cracked.txt","w")
for x in dicti:
    string = x.split(":")
    string[1] = string[1].split("\n")
    #print(string[1][0])
    if string[1][0] in list:
        #print(string[0])
        cracked.write("%s:" % string[1][0])
        cracked.write("%s\n" % string[0])
            
dicti.close()
new_dict = open("hashed_rock.txt","r")
for z in new_dict:
    string = z.split(":")
    string[1] = string[1].split("\n")
    #print(string[1][0])
    if string[1][0] in list:
        #print(string[0])
        cracked.write("%s:" % string[1][0])
        cracked.write("%s\n" % string[0])
new_dict.close()
cracked.close()
