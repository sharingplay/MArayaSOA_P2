minikube stop

minikube delete --all

minikube start

minikube addons enable gcp-auth

kubectl create ns rabbits

kubectl apply -n rabbits -f Broker/Files

::timeout 60

:: kubectl -n rabbits port-forward service/frontend-service 80:90