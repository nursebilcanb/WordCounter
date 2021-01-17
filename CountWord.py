def how_many(word):
    file = open("alice_in_wonderland.txt","r")
    content = file.read()
    content_splt = content.split()
    count1 = 0
    count2 = 0
    
    for scanner in content_splt:
        if scanner == word:
            count1 += 1
            
    for element in content_splt:
        count2 +=1

    print(word, ":" , count1)
    print(f"Count of element : {count2}")
    
    file.close()


how_many('of')
