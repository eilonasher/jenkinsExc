pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                cleanWs()
                bat 'git clone https://github.com/eilonasher/jenkinsExc'
            }
        }
        stage('Build') {
            steps {
                echo 'Build'
            }
        }
        stage('Test') {
            steps {
                echo 'Test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy'
            }
        }
    }
}
