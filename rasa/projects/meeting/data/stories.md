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
  
## interactive_story_1
* find_room{"building": "SP12", "capacity": "5"}
    - slot{"building": "SP12"}
    - slot{"capacity": "5"}
    - utter_find_room

## interactive_story_1
* find_room{"building": "SP12", "capacity": "5"}
    - slot{"building": "SP12"}
    - slot{"capacity": "5"}
    - utter_find_room
* find_room{"building": "SP12", "capacity": "5", "startTime": "5PM"}
    - slot{"building": "SP12"}
    - slot{"capacity": "5"}
    - slot{"startTime": "5PM"}
    - utter_find_room
* find_room{"building": "SP12", "capacity": "55"}
    - slot{"building": "SP12"}
    - slot{"capacity": "55"}
    - utter_find_room
* find_room{"building": "SP12", "capacity": "5"}
    - slot{"building": "SP12"}
    - slot{"capacity": "5"}
    - utter_find_room

## interactive_story_1
* find_room{"building": "SP12", "capacity": "5", "startTime": "3PM"}
    - slot{"building": "SP12"}
    - slot{"capacity": "5"}
    - slot{"startTime": "3PM"}
    - utter_find_room
* find_room{"building": "SP12", "capacity": "5", "startTime": "3PM", "duration": "4 hours"}
    - slot{"building": "SP12"}
    - slot{"capacity": "5"}
    - slot{"duration": "4 hours"}
    - slot{"startTime": "3PM"}
    - utter_find_room

## interactive_story_1
* find_room{"building": "SP12", "capacity": "5", "startTime": "3PM", "duration": "5 hours"}
    - slot{"building": "SP12"}
    - slot{"capacity": "5"}
    - slot{"duration": "5 hours"}
    - slot{"startTime": "3PM"}
    - utter_find_room

## interactive_story_1
* find_room{"building": "SP12", "capacity": "5", "startTime": "3PM", "duration": "5 hours", "number": 5, "time": "2019-09-12T15:00:00.000-07:00"}
    - slot{"building": "SP12"}
    - slot{"capacity": "5"}
    - slot{"duration": "5 hours"}
    - slot{"startTime": "3PM"}
    - utter_find_room
* find_room{"startDate": "tomorrow"}
    - slot{"startDate": "tomorrow"}
    - utter_find_room
* find_room{"startDate": "today", "startTime": "3PM", "time": "2019-09-12T15:00:00.000-07:00"}
    - slot{"startDate": "today"}
    - slot{"startTime": "3PM"}
    - utter_find_room
