import os
import hashlib
import time

file = open("biglist.txt","r",encoding="utf8")
file_w = open("hashed_biglist.txt","w",encoding="utf8")
for i in file:
    string = i.split("\n")
    file_w.write("%s:" % string[0])
    file_w.write("%s\n" % hashlib.md5(string[0].encode()).hexdigest())
file.close()
file_w.close()

passwords = open("passwords.txt","r")
list_p = []
timer = {}
for y in passwords:
    string = y.split("\n")
    list_p.append(string[0])
    timer[string[0]] = 0.0
passwords.close()

cracked = open("cracked.txt","w")
new_dict = open("hashed_biglist.txt","r",encoding="utf8")
t0 = time.time()
for z in new_dict:
    string = z.split(":")
    string[1] = string[1].split("\n")
    if string[1][0] in list_p:
        t1 = time.time() #used for tracking how long the program needed to
        total = t1 - t0 #crack password
        timer[string[1][0]] = total
        t0 = t1
        cracked.write("%s:" % string[1][0])
        cracked.write("%s\n" % string[0])
new_dict.close()
cracked.close()

list_pwd = open("cracked.txt","r")
i = 0 #counter for preventing printing of duplicate cracked entries
for entry in list_pwd:
    string = entry.split(":")
    string[1] = string[1].split("\n")
    if(i < 6):
        print("The password for hash value ", string[0], " is ", string[1][0], ", it takes the program %.3f sec to recover this password" % timer[string[0]])
    i = i + 1
list_pwd.close()
