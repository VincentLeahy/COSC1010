#
# Name Vincent Leahy
# Date 2/9/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#get # of people at cookout.
#get number of hotdogs each person will get.
#Calculate # of packs of dogs and buns are needed.
# get leftovers
#hot dogs = 10
#buns = 8

#people attending cookout
people = input("How many people are attedning the cookout? ")

#get number of hot dogs each person is getting.
hot_dogs_per_person = input("How many hot dogs does each person get? ")

#number inputs
people = int(people)
hot_dogs_per_person = int(hot_dogs_per_person)

#calculate the number of hotdogs we need
total_hot_dogs = people * hot_dogs_per_person

#number of packages of hot dogs needed
hot_dog_packs = total_hot_dogs // 10 
#gives the number of full packs of hot dogs
if total_hot_dogs % 10 !=0:
    hot_dog_packs = hot_dog_packs + 1
# for any remainders adding 1 will hopefully fix that.

#Calculate number of buns are needed
bun_packs = total_hot_dogs // 8
#gives full packs of buns
if total_hot_dogs % 8 !=0:
    bun_packs = bun_packs +1
#same case for the hot dogs, getting the remainders.

#leftovers for hot dogs and buns.
leftover_hot_dogs = hot_dog_packs * 10 - total_hot_dogs
leftover_buns = bun_packs * 8 - total_hot_dogs

#Results printed out after calculations
print("You will need: ")
print("Hot dog packs: " + str(hot_dog_packs))
print("Bun packs: " + str(bun_packs))
print("Leftover hot dogs are: " + str(leftover_hot_dogs))
print("Leftoverbuns are: " + str(leftover_buns))