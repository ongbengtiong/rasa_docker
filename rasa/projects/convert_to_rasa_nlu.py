import json


def sanitize(s) :
    s = s.replace(' ', '_')
    s = s.replace('\'', '_')
    s = s.replace('&', '_')
    s = s.replace('(', '_')
    s = s.replace(')', '_')
    s = s.replace('/', '_')
    
    return s

nlu_file = open('nlu.md','w', encoding="utf-8") 
  
domainIntents = []
domainTemplates = []
domainActions = []

with open('source/question_grouping_data.json') as json_file:
    data = json.load(json_file)
    pathCount = 0
    for p in data: 
        intent = p['answer']
        intent = sanitize(intent)
        nlu_file.write('## intent:' + intent + '\n')
                       
        main_question = p['main_question'].replace('\n', ' ')
        main_question = sanitize(main_question)
                       
        nlu_file.write('- ' + main_question + '\n')        
        for nonmain_question in  p['augment']:
            nlu_file.write('- ' + nonmain_question + '\n')
        nlu_file.write('\n') 
        
        domainIntents.append(' - ' +  intent)
   
        pathCount = pathCount + 1
     
nlu_file.close() 

 
stories_file = open('stories.md','w', encoding="utf-8")  
  

with open('source/ans_id_to_answer.json') as json_file:
    data = json.load(json_file)
    pathCount = 0
    for p in data:  
        intent = sanitize(p)
      
        stories_file.write('## ' + intent + ' ' + str(pathCount) + '\n')
        stories_file.write('* ' + intent +  '\n') 
        stories_file.write('  - utter_' + intent + '\n')  
        
        domainTemplates.append(' utter_' +  intent + ':')
        
        domainActions.append(' - utter_' +  intent)
        for answer in data[p]:
            answer = answer.replace('\n', '    ')
            answer = sanitize(answer)
            #domainTemplates.append('  -\n   text: |-\n    ' +  answer + '')
            domainTemplates.append('  - text: "' +  intent + '"')
            
        
        stories_file.write('\n') 
        pathCount = pathCount + 1
      
stories_file.close()  


domain_file = open('domain.yml','w', encoding="utf-8") 

domain_file.write('intents:\n') 
for p in domainIntents:
    domain_file.write(p + '\n') 
    
    
domain_file.write('\n') 
domain_file.write('actions:\n') 
for p in domainActions:
    domain_file.write(p + '\n')  

domain_file.write('\n') 
domain_file.write('templates:\n') 
for p in domainTemplates:
    domain_file.write(p + '\n')   
    
    
        
domain_file.close()  