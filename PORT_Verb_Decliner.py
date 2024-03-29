'''
24 Nov 2023 - present: Brazilian Portuguese imperative verb decliner
For now, this only deals with regular, non-stem-changing imperative verbs

Main Program: create new chart (in old or existing txt file), view existing charts, modify existing charts, delete charts, irregular Vs
'''
from PORT_Verb_Decliner_BTS import *

#currently focusing on REGULAR verbs
#note: later in project, involve subjunctives/imperatives/irregular or stem-changing verbs

print("Welcome to the Brazilian Portuguese Verb Recliner! Obrigada por vir.")

#default user permissions: none. Resets each time user starts the program. See BTS for notes
user_permission = '00000'
    
#while loop to keep running decliner until user wants to stop
end_program=False
while end_program==False:

    #get infinitive and tense from the user
    #validate data: ensure user enters a declinable word
    valid_inf=False
    while valid_inf==False:
        inf=input('\nEnter an infinitive Portuguese verb: ') 
        if inf[-2:]=='ar' or inf[-2:]=='er' or inf[-2:]=='ir':
            #this doesn't account for infinitives; later, make list of irregular Vs
            #and check 'if inf in list_name'
            valid_inf=True
        #irregular verbs: make dict w/ nested lists for each declined tense form
        #elif inf in irregular_roots:
        else:
            print("Invalid input, please try again.")

    valid_tense=False
    while valid_tense==False:
        tense=input('Which tense would you like to decline your verb to? Present (1), imperfect \
preterit (2), or perfect preterit (3)? ') 
        if tense=='1' or tense=='2' or tense=='3':
            #this doesn't account for infinitives; later, make list of irregular Vs
            #and check 'if inf in list_name'
            valid_tense=True
        else:
            print("Invalid input, please try again.")

    #create instance of Tense class object with given infinitive
    match tense:
        case '1':
            v=Present(inf)
            match inf[-2:]:
                case 'ar':
                    v.ar_pst1s(inf)
                    v.ar_pst23s(inf)
                    v.ar_pst1p(inf)
                    v.ar_pst23p(inf)
                case 'er':
                    v.er_pst1s(inf)
                    v.er_pst23s(inf)
                    v.er_pst1p(inf)
                    v.er_pst23p(inf)
                case 'ir':
                    v.ir_pst1s(inf)
                    v.ir_pst23s(inf)
                    v.ir_pst1p(inf)
                    v.ir_pst23p(inf)
        case '2':
            v=ImperfectPreterit(inf)
            match inf[-2:]:
                case 'ar':
                    v.ar_imp123s(inf)
                    v.ar_imp1p(inf)
                    v.ar_imp23p(inf)
                case 'er':
                    v.er_imp123s(inf)
                    v.er_imp1p(inf)
                    v.er_imp23p(inf)
                case 'ir':
                    v.ir_imp123s(inf)
                    v.ir_imp1p(inf)
                    v.ir_imp23p(inf)
                    
        case '3':
            v=PerfectPreterit(inf)
            match inf[-2:]:
                case 'ar':
                    v.ar_prf1s(inf)
                    v.ar_prf23s(inf)
                    v.ar_prf1p(inf)
                    v.ar_prf23p(inf)
                case 'er':
                    v.er_prf1s(inf)
                    v.er_prf23s(inf)
                    v.er_prf1p(inf)
                    v.er_prf23p(inf)
                case 'ir':
                    v.ir_prf1s(inf)
                    v.ir_prf23s(inf)
                    v.ir_prf1p(inf)
                    v.ir_prf23p(inf)

    v.forms()

    #by choosing inf/tense for new verb, user unlocks ability to take test
    user_permission = allow_test
     
    #nested while loop to let user do multiple actions with the declined forms
    end_menu=False
    while end_menu==False:
        #make a menu for user to choose which tense they want to conjugate inf to
        activity=input("\nMain Menu:\nWhat would you like to do with your declined verb?\
\n(1) Test your knowledge {},\n\
(2) View a verb chart {}, \n(3) Save a new chart {}, \n(4) View all saved charts {}, or\
\n(5) Delete an existing chart {}? \nEnter a number, 'back' to choose a new verb, or \
'stop' to end the program. ".format('[' + permission_status[int(user_permission[0])] + ']', '[' + permission_status[int(user_permission[1])] + ']',\
                                    '[' + permission_status[int(user_permission[2])] + ']', '[' + permission_status[int(user_permission[3])] + ']',\
                                    '[' + permission_status[int(user_permission[4])] + ']' ) )
        #.format to print [UN]LOCKED status for each action in {} position
        
        match activity.lower():
            case '1':
                #check user permission
                if not compare_permission(user_permission,allow_test):
                    print("Sorry, you don't have permission to access the Main Menu. Please try entering a verb and tense first.")
                    continue #return to Main Menu
                
                print("\nTest your knowledge! Let's see how many forms you can decline. You must earn a full score\
 to unlock actions (2) and (3).",'\n','Enter the corresponding declined form to match each subject pronoun. Boa sorte!')
                counter=0
                score=0
                forms_dict={}
                for i in v._forms:
                    answer=input(subjects[counter]+' __: ') #order of subjects' indexes corresponds to v._forms' indexes
                    #add entry in forms_dict w/ key being correct form and value being user's answer
                    forms_dict[i]=answer.lower()
                    #check if answer is correct (forms are equivalent); if yes, add 1 point to score
                    if i==answer.lower():
                        score+=1
                        print('Correct!')
                    else:
                        print('Incorrect. The correct form is',i+'.')
                    counter+=1 #upon next iteration, subsequent pronoun is referenced
                print('Your total score was %d out of 6.' % score)
                if score==6: #user unlocks ability to save/view chart
                    user_permission=allow_new_chart
                

            case '2': #print out a verb chart
                #check user permission
                if not compare_permission(user_permission,allow_new_chart): #minimum permission 11000 required
                #if bin(user_permission & allow_new_chart) < 0b11000: #scrapped the bitwise idea; did not work for multiple tests due to bin() returning str
                    print("Sorry, you don't have permission to view this chart. Please try completing a test (1) first.")
                    continue
                
                #CHART FORMAT: infinitive header (title); columns by singular/plural; rows by person
                print('\n'+v._tense.capitalize(),'tense forms of',inf.lower()+':','\n')
                #use list for charts; need to be able to index
                for header in ['Person','Singular','Plural']: #each str heads a column w/ corresponding info
                    print(format(header,'<20s'),end='')
                print()

                for n in range(3):
                    #for each row, need to pull both sing. and pl. verb form of that Person
                    print(format(persons[n],'<20s'),format(v._forms[n],'<20s'),v._forms[n+3],sep='')

                print('\n'+'*'*60) #line of chars separating charts
     
                
            case '3': #write in verb chart to text file using append mode
                #check user permission
                if not compare_permission(user_permission,allow_new_chart): #minimum permission 11100 required
                #if (int(user_permission) & int(allow_new_chart)) < 0b11100:
                    print("Sorry, you don't have permission to save this chart. Please try completing a test (1) first.")
                    continue #return to Main Menu
                
                with open("Portuguese_Verb_Charts.txt",'a') as charts: #open and/or create new file to write into
                    charts.write((v._tense.capitalize()+' tense forms of '+inf.lower()+': '+'\n'))
                    #use list for charts; need to be able to index
                    for header in ['Person','Singular','Plural']: #each str heads a column w/ corresponding info
                        charts.write((format(header,'<20s')+''))
                    charts.write('\n')

                    for n in range(3):
                        #for each row, need to pull both sing. and pl. verb form of that Person
                        charts.write((format(persons[n],'<20s')+''+format(v._forms[n],'<20s')+''+v._forms[n+3]+'\n'))

                    charts.write('\n'+'*'*60+'\n') #line of chars separating charts
                charts.close()

                print("\nDeclined verb chart has been saved in text file named \"Portuguese_Verb_Charts\".")

                #user unlocks permission to view all/delete saved charts
                user_permission = allow_chart_mod
                
            case '4': #read data from text file as str; print out to the user in a formatted fashion...
                #check user permission
                if not compare_permission(user_permission,allow_chart_mod): #minimum permission 11010 required    
                #if bin(user_permission & allow_chart_mod) < 0b11010: 
                    print("Sorry, you don't have permission to view saved charts. Please try saving a chart (3) first.")
                    continue #return to Main Menu
                
                try: 
                    with open("Portuguese_Verb_Charts.txt",'r') as charts:
                        charts_txt=charts.read()
                        #lines in text file are separated by line break
                        for line in charts_txt.split('\n'):
                            print(line)
                    
                except: #if verb chart file has not been created
                   print("\nSorry, an error occurred. Please ensure that file Portuguese_Verb_Charts exists in the same folder as this program.")
                #first use try block to check if chart exists w/ read mode
                #also give user another choice here: to wipe all existing charts or just remove 1
                #to wipe all existing charts, use write mode and write in ''

                finally: #if try block raises exception after opening file, this block runs regardless of how far the other blocks execute
                    charts.close()

            case '5':
                #check user permission
                if not compare_permission(user_permission,allow_chart_mod): #minimum permission 11001 required
                #if bin(user_permission & allow_chart_mod) < 0b11001:
                    print("Sorry, you don't have permission to delete a chart. Please try saving a chart (3) first.")
                    continue #return to Main Menu
                
                try:                         
                    with open("Portuguese_Verb_Charts.txt",'r+') as charts:
                        charts_txt=charts.read()
                        chart_start=charts_txt.find(v._tense.capitalize()+' tense forms of '+inf.lower())
                        chart_not_found(chart_start)
                        chart_end=charts_txt.find('*', chart_start) #finds first occurrence of '*' substring after chart_start
                        chart_end+=59 #line of 60 '*'s marks end of the chart; add 59 to find final index of chart
                        charts.truncate(0) #change file handle position from end to beginning of charts
                        revised_txt=charts_txt[:chart_start]+charts_txt[chart_end+1:]
                        charts.write(revised_txt)
                        print(v._tense.capitalize(),'chart of',inf.lower(),'has been deleted from your charts.')

                except: #if chart has not yet been written into file, will raise an exception
                    print("\nSorry, an error occurred. Please ensure that text file Portuguese_Verb_Charts exists in the same folder as this program\
and that",v._tense,"chart of",inf.lower(),'exists in your saved charts.')

                finally:
                    charts.close()
                    
            case 'back':
                end_menu=True
                
            case 'stop':
                end_program=True
                end_menu=True #need to break out of both loops, otherwise nested loop will continue iterating
                
            case _: #if user enters other input, restart loop
                print("Sorry, that's not a valid option. Please try again.")
                continue
    
