'''
24 Nov 2023 - present: Brazilian Portuguese imperative verb decliner
Make three different classes of verbs: -ar, -er, -ir
Tenses (each tense is a class function; declined forms stored as object attributes):
present, imperfect preterit, perfect preterit, -present participle (special case)
Start with just imperatives for now
-maybe later: separate this project into 2 files (1 for main program, 1 for classes/functions -->
import BTS file into main program file)
-also: the program itself should make files using I/O (do that later)
Main Program: create new chart (in old or existing txt file), view existing charts, modify existing charts, delete charts, irregular vrebs
'''
from PORT_Verb_Decliner_BTS import *

#currently focusing on REGULAR verbs
#note: later in project, involve subjunctives/imperatives/irregular or stem-changing verbs

print("Welcome to the Brazilian Portuguese Verb Recliner! Obrigada por vir.")
#while loop to keep running decliner until user wants to stop
end=False
while end==False:
    #get infinitive and tense from the user
    #validate data: ensure user enters a declinable word
    valid_inf=False
    while valid_inf==False:
        inf=input('Enter an infinitive Portuguese verb: ') 
        if inf[-2:]=='ar' or inf[-2:]=='er' or inf[-2:]=='ir':
            #this doesn't account for infinitives; later, make list of irregular Vs
            #and check 'if inf in list_name'
            valid_inf=True
        else:
            print("Invalid input, please try again.")

    valid_tense=False
    while valid_tense==False:
        tense=input('Which tense would you like to test? Present (1), imperfect \
preterit (2), or perfect preterit (3)? ') 
        if tense=='1' or tense=='2' or tense=='3':
            #this doesn't account for infinitives; later, make list of irregular Vs
            #and check 'if inf in list_name'
            valid_tense=True
        else:
            print("Invalid input, please try again.")


                    
    #make a menu for user to choose which tense they want to conjugate inf to
    activity=input("Main Menu: Would you like to test your knowledge (1), \
view a verb chart (2), save a new chart (3), or view all saved charts (4)? \
Enter a number or 'stop' to end the program. ")
    match activity.lower():
        case '1':
            print("Test your knowledge! Let's see how many verbs you can decline.")


        case '2': #print out a verb chart
            print('holder statement while I test this in the BTS file')
            #use cases here (match tense) to create new class instance w/ attributes depending on num entered  
            
        case '3': #write in verb chart to text file using append mode
            with open("Portuguese_Verb_Charts.txt",'a') as file_obj: #open and/or create new file to write into
                file_obj.write((g._tense.capitalize()+' tense forms of '+inf.lower()+': '+'\n'))
                #use list for charts; need to be able to index
                for header in ['Person','Singular','Plural']: #each str heads a column w/ corresponding info
                    file_obj.write((format(header,'<20s')+''))
                file_obj.write('\n')

                for n in range(3):
                    #for each row, need to pull both sing. and pl. verb form of that Person
                    file_obj.write((format(persons[n],'<20s')+''+format(forms_list[n],'<20s')+''+forms_list[n+3]+'\n'))

                file_obj.write('\n'+'*'*60+'\n') #line of chars separating charts
            file_obj.close()

            print("Declined verb chart has been saved in text file named \"Portuguese_Verb_Charts\".")
            
        case '4': #read data from text file as str; print out to the user in a formatted fashion...
            print('holder statement while I test this in the BTS file')
            #charts are separated by '*' lines w/ len=60
            #first use try block to check if chart exists w/ read mode
            #also give user another choice here: to wipe all existing charts or just remove 1
            #to wipe all existing charts, use write mode and write in ''

        case 'stop':
            end=True
        case _:
            print("Sorry, that's not a valid option. Returning to the main menu now.")
    
    
    try: #use try/except/else block for opening a file (if no file exists yet, program will
        #catch the exception
        infinitive=input('Please enter an infinitive verb form. ')

        word=Verb(infinitivo)
        #testing if the basic structure still works; later, should be input-driven for tense:
        print('the imperfect 1st/2nd/3rd person form of your infinitive is',\
              word.imp_123ps())
    except:
        print("Invalid input, please try again.")

'''
inf=input('infinitive? ')
g=Ar_Verb(inf)
g.pst1s(inf)
g.pst23s(inf)
print(g._pst1s,g._pst23s)


print('starting with "estar"')
word1=Verb('estar')
print('imperfect 1st person singular form is', word1.imp_123ps())
'''

#word2=Verb('beber')
#print(word2.imp_123ps())

#word3=Verb('dizer')
#print(word3.imp_123ps())


#CHART FORMAT: infinitive header (title); columns singular/plural; rows Person

