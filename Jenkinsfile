pipeline {
    agent any

    environment {
        dockerImage =''
        registry = 'makbar4721/dicea3'
    }

    stages{
        stage('Checkout') {
            steps{
               checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/m-ali4721/d_camp_a3']]) 
            }
        }

        stage('Docker Image'){
            steps {
                script {
                    dockerImage = docker.build registry
                }
            }
        }
    }
}