## Point Docker to Minikube
eval $(minikube docker-env)

docker build -t llmops-app:latest .

# Add values to secrets before running below command
# kubectl create secret generic llmops-secrets \
#   --from-literal=GROQ_API_KEY="" \
#   --from-literal=HUGGINGFACEHUB_API_TOKEN=""

kubectl apply -f llmops-k8s.yaml


kubectl get pods

### U will see pods running


# Do minikube tunnel if run on local machine

minikube tunnel


# With VM cloud, use this command

kubectl port-forward svc/llmops-service 8500:80 --address 0.0.0.0

## Now copy external ip and :8500 and see ur app there....

