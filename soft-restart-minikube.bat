kubectl apply -n rabbits -f Broker/Files

::timeout 60

:: kubectl -n rabbits port-forward service/frontend-service 80:90
:: kubectl -n rabbits port-forward deployment/backend-service 3600:3600
:: kubectl -n rabbits port-forward service/mysql 3306:3306
:: kubectl -n rabbits port-forward rabbitmq-0 15672:15672