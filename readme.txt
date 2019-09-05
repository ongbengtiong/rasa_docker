https://rasa.com/docs/core/docker_walkthrough/#adding-natural-language-understanding-rasa-nlu

Compose: 
touch docker-compose.yml
docker-compose up

Test:
Invoke-RestMethod -Method Post -Uri http://localhost:5005/webhooks/rest/webhook -Body '{"sender":"asdad", "message":"hello"}'