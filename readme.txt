https://rasa.com/docs/core/docker_walkthrough/#adding-natural-language-understanding-rasa-nlu

Compose: 
touch docker-compose.yml

  action_server:
    image: rasa/rasa-sdk:latest
    volumes:
      - ./actions:/app/actions

docker-compose up


Test:
Invoke-RestMethod -UseBasicParsing -Method Post -Uri http://localhost:5005/webhooks/rest/webhook -Body '{"sender":"asdad", "message":"find me a room"}'
Invoke-WebRequest -UseBasicParsing -Method Post -Uri http://localhost:5005/webhooks/rest/webhook -Body '{"sender":"asdad", "message":"find me a room"}'