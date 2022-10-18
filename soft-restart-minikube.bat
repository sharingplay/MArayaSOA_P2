kubectl apply -n rabbits -f Broker/Files

::timeout 60

:: kubectl -n rabbits port-forward service/frontend-service 80:90
:: kubectl -n rabbits port-forward deployment/rabbitmq 15672:15672
:: kubectl -n rabbits port-forward service/mysql 3306:3306