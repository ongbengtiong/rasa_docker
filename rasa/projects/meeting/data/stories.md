## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_name
* name{"name":"Sam"}
 - utter_greet
 

## story_joke_01
* joke
 - action_joke
 
## story_joke_02
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
* joke
 - action_joke
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 
 
 
## story_find_room
* find_room{"building": "SP12"} 
 - utter_find_room

 
## happy_path
* greet
  - utter_greet
* mood_happy
  - utter_happy
* goodbye
  - utter_goodbye

## sad_path
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
* goodbye
  - utter_goodbye
  
  
## sad_path_02
* mood_unhappy
  - utter_cheer_up
* goodbye
  - utter_goodbye