HASHING

hash function takes an input (string for example) and output an index that relates to a 'bucket'

take string input, take each letter's place in the alphabet, add them and take the mod of the number of 'buckets' and place it in the hash table

but if they map to the same place in the hash table we have a hash collision
 

HASH COLLISION
1 - separate chaining, store the values that have the hash position as linked lists. each individual one is also a linked list, just with one element

purpose of hash table - implement hash set or hash map

HASH SET
set that uses hashing, set has unique items
looking up something takes o(1) time in relation to length (n), still has to go over the entire length of the string originally (clarification)
o(1) on average though (amortized). if there was a linked list in a place in the table due to hash collision, absurdly worse it could take o(n) time, (considering all the elements were in that one table position and in the linked list)

lookup - o(1)
add - o(1)
delete - o(1)

HASH MAP
all functionality of hash set except it can store data
stores in keys and values
keys must be hashable
values can be anything

in the hash table the key and the value are stored together in the linked list (considering separate chaining) as a tuple

lookup - o(1)
add - o(1)
remove - o(1)

DIFFERENT WAY TO HANDLE COLLISION - LINEAR PROBING

if a hash position was already full it would move it to the next avaliable hash position
same operations as hash set and map

lookup - find hash position and if not there then keep going down till its found, if a blank is found then that means it doesnt exist in the set/map. 
not truly constant time (o(n) worst case) but on average o(1)

** important **delete - might break probing, since you can delete but if something that was supposed to be there was moved down because of linear probing it won't be found later since it has been deleted
so delete needs to be marked by something (ex: -1) so it doesnt break the lookup

WHAT IS HASHABLE - immutable (can't change the memory of)
strings, integers, tuples

NOT HASHABLE - (can change the memory of)
lists, dictionaries
