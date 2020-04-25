import io
import collections

    
nationalities = ["American","European","Latin American","Asian","Arab","Middle Eastern","African",\
                "Mexican","Brazilian","Russian","Indian","Chinese","Japanese","Australian",\
                 "Iranian","Saudi Arabian","Indonesian","Pakistanian","Nigerian",\
                 "Bangladeshi", "Ethiopian","Filipino","Turkish","Thai","Egyptian","Congolese",\
                 "British","German",""]
modifiers = ["man","woman"]


def findDifference(toAnalyze,benchmark):
    ratios = {}
    singleMentions = {}
    for key, value in toAnalyze.items():
        if key in benchmark.keys():
            compVal = benchmark[key]
            ratio = value/compVal
            ratios[key] = (ratio,(value,compVal))
        else:
            singleMentions[key] = value
    weightedRatios = [(k,v) for k, v in sorted(ratios.items(), key=lambda item: item[1][0]*(item[1][1][0]-item[1][1][1]),reverse = True)]
    ratios = [(k,v) for k, v in sorted(ratios.items(), key=lambda item: item[1][0],reverse = True)]
    singleMentions = [(k,v) for k, v in sorted(singleMentions.items(), key=lambda item: item[1],reverse = True)]
    return ratios,weightedRatios,singleMentions

def compare(toAnalyze, benchmark):
    overRepresented, weightedOver, singleMentions = findDifference(toAnalyze,benchmark)
    underRepresented, weightedOver, unmentioned = findDifference(benchmark,toAnalyze)
    return overRepresented,weightedOver, singleMentions,underRepresented,weightedOver,unmentioned
def prettyPrint(init,fieldSep,sep,toPrint,quantity):
    print(fieldSep)
    print(init)
    print(fieldSep)
    if(sep != " "):
        for i in range(quantity):
            print(toPrint[i],end = sep)
            
        print()
    else:
        print(toPrint[0:quantity])


def stats(key1,key2,quantity = 50,sep = " "):
    over,weightO,single,under,weightU,blank = compare(wordLists[key1],wordLists[key2])
    
    fieldSep = "_"*50
    initOver = "Over represented in: " + key1
    initWeightedOver = "(Weighted)Over represented in: " + key1
    initSingle =  "Only mentioned in: " + key1
    initUnder = "Over represented in: " + key2
    initWeightedUnder = "(Weighted)Over represented in: " + key2
    initBlank = "Only mentioned in: " + key2
    
    prettyPrint(initOver,fieldSep,sep,over,quantity)
    prettyPrint(initWeightedOver,fieldSep,sep,weightO,quantity)
    prettyPrint(initSingle,fieldSep,sep,single,quantity)
    prettyPrint(initUnder,fieldSep,sep,under,quantity)
    prettyPrint(initWeightedUnder,fieldSep,sep,weightU,quantity)
    prettyPrint(initBlank,fieldSep,sep,blank,quantity)

wordLists = {}
overRepresented = {}
singleMentions = {}
underRepresented = {}
unmentioned = {}
for nationality in nationalities:
    for modifier in modifiers:
        key = nationality +" "+modifier
        filename = nationality+modifier+".txt"
        with io.open(filename, 'r', encoding='utf8') as f:
            wordLists[key] = [word for line in f for word in line.split()]
            counter = collections.Counter(wordLists[key])
            wordLists[key] = counter
