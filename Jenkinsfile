pipeline{
    agent any

    tools {
        nodejs "nodeJS"
    }

    environment {
        REGISTRY = 'neoairavataproject/ui-service'
        REGISTRY_CREDENTIAL = 'docker-credentials'
        FILE = 'fe-service.yaml'
        SERVICE_NAME = 'ui-service'
        DEPLOY_NAME = 'fe-deploy'
        HOME_DIRECTORY = 'Neo-FE'
        KUBE_DIRECTORY = '/home/ubuntu/deploy'
    }
    stages{
        stage('Clone Git Repo') {
            steps{
                checkout scm
                echo "Successfully cloned git repository"
            }
        }

        stage('Install dependencies') {
            steps{
                sh 'cd ${HOME_DIRECTORY} && npm install'
                echo "Successfully installed npm packages"
            }
		    
	    }

        stage('Test App') {
		    steps{
                echo "Successfully tested app"
            }
	    }

        stage('Build Docker Image') {
            agent any
            steps{
                sh 'cd ${HOME_DIRECTORY} && pwd && docker image build . -t ${SERVICE_NAME}:latest'
                sh 'docker tag ${SERVICE_NAME}:latest ${REGISTRY}:latest'
                echo "Successfully built docker images"
            }
        }

        stage('Push Image to Dockerhub'){
            agent any
            steps{
                withCredentials([usernamePassword(credentialsId: 'REGISTRY_CREDENTIAL', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                    sh 'docker push ${REGISTRY}:latest'
                }
                echo "Successfully pushed image to docker hub"
            }    
        
        }

        stage('Clean Up Disk Space') {
            steps{
                sh "docker system prune -af --volumes" 
            }
        }    

        stage('Kubernetes Cluster Deployment') {
            steps{
                sshagent (credentials: ['PRIVATE_KEY'])
                {
                    script{
                        try{
                            sh 'ssh -o StrictHostKeyChecking=no ubuntu@149.165.153.238 mkdir ${HOME_DIRECTORY}'
                        }catch(error)
                        {}
                    }
                    sh 'scp -r -o StrictHostKeyChecking=no ${HOME_DIRECTORY}/fe*.yaml ubuntu@149.165.153.238:/home/ubuntu/${HOME_DIRECTORY}'
                    script{
                        try{
                            sh 'ssh -o StrictHostKeyChecking=no ubuntu@149.165.153.238 sudo kubectl delete --ignore-not-found=true -f ${HOME_DIRECTORY}/fe-service.yaml -f ${HOME_DIRECTORY}/fe-deployment.yaml'
                            sh 'ssh -o StrictHostKeyChecking=no ubuntu@149.165.153.238 sudo kubectl apply -f ${HOME_DIRECTORY}/fe-service.yaml -f ${HOME_DIRECTORY}/fe-deployment.yaml'
                            sh 'ssh -o StrictHostKeyChecking=no ubuntu@149.165.153.238 sudo rm -rf ${HOME_DIRECTORY}'
                        }catch(error)
                        {}
                    }
                }
            }
        }
    }    
}
