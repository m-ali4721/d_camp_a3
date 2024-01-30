pipeline {
    agent any

    environment {
        dockerImage =''
        registry = 'makbar4721/dicea3'
        registryCredential='dockerhub_id'
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

        stage('Uploading Image'){
            steps {
                script{
                    docker.withRegistry('', registryCredential){
                        dockerImage.push()
                    }

                }
            }
        }

        stage('docker run'){
            steps {
                script{
                    docker.withRegistry('', registryCredential) {
                        docker.image(registry).run("-p 8020:8020 --name dicea3c2")
                    }
                }
            }
        }

        }
    }
