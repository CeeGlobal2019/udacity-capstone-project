pipeline {
    agent any
    environment {
        registry = "ceemezla/udacitycapstone"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
    stages {
         stage('Linting my app and container') {
              steps {
                  sh 'make lint'
              }
         }
         stage('Building Docker image') {
            steps{
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Uploading Docker-Image to Docker hub') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Remove docker image not in use') {
            steps{
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
        stage('Update Kubernetes Configuration file'){
            steps {
                withAWS(region:'us-east-1',credentials:'aws') {
                    sh 'sudo aws eks --region us-east-1 update-kubeconfig --name udacity-capstone-project'                    
                }
            }
        }
        stage('Deploy Docker Image Update to Cluster'){
            steps {
                sh '''
                    export IMAGE="$registry:$BUILD_NUMBER"
                    sed -ie "s~IMAGE~$IMAGE~g" resources/deployment.yml
                    sudo kubectl apply -f ./resources
                    '''
            }
        }
       
    }
}