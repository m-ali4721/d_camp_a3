pipeline {
    agent any

    stages{
        stage('Checkout') {
            steps{
               checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/m-ali4721/d_camp_a3']]) 
            }
        }
    }
}