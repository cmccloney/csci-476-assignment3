import os
import hashlib

file = open("biglist.txt","r",encoding="utf8")
file_w = open("hashed_biglist.txt","w",encoding="utf8")
for i in file:
    string = i.split("\n")
    file_w.write("%s:" % string[0])
    file_w.write("%s\n" % hashlib.md5(string[0].encode()).hexdigest())
file.close()
file_w.close()

passwords = open("passwords.txt","r")
list = []
for y in passwords:
    string = y.split("\n")
    list.append(string[0])
passwords.close()

cracked = open("cracked.txt","w")
new_dict = open("hashed_biglist.txt","r",encoding="utf8")
for z in new_dict:
    string = z.split(":")
    string[1] = string[1].split("\n")
    if string[1][0] in list:
        cracked.write("%s:" % string[1][0])
        cracked.write("%s\n" % string[0])
new_dict.close()
cracked.close()

list_pwd = open("cracked.txt","r")
i = 0 #counter for preventing printing of duplicate cracked entries
for entry in list_pwd:
    if(i < 6):
        print(entry)
    i = i + 1
list_pwd.close()
