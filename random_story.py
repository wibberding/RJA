from random import randint

adjList=["wild","fluffy","hilarious", "soft", "yellow", "green"]
placeList=["Chicago","China","Brazil", "Oregon", "Disneyland", "the ocean"]
nounList=["telephone", "karate", "green bean", "taco", "car", "hill"]

index1=randint(0,len(adjList)-1)
adj1=adjList[index1]

index2=randint(0,len(adjList)-1)
adj2=adjList[index2]

index3=randint(0,len(adjList)-1)
adj3=adjList[index3]

index4=randint(0,len(placeList)-1)
place1=placeList[index4]

index5=randint(0,len(placeList)-1)
place2=placeList[index5]

index6=randint(0,len(placeList)-1)
place3=placeList[index6]

index7=randint(0,len(adjList)-1)
noun1=nounList[index7]

index8=randint(0,len(adjList)-1)
noun2=nounList[index8]

index9=randint(0,len(adjList)-1)
noun3=nounList[index9]

sentence1= "Last year, I went on a "+adj1+" trip to "+place1+"." 
sentence2= "The weather there was "+adj2+", and I couldn't wait to eat a big "+noun1+" while I was there."
sentence3="Next year, I want to go to "+place2+", because I've always wanted to see the "+adj3+" "+noun2+"."

print (sentence1,sentence2,sentence3)
