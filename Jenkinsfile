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
        stage('Remove Unused docker image') {
            steps{
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
       
    }
}