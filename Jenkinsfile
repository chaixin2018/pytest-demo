pipeline {
    agent any
    stage('Install Dependencies') {
            steps {
                script {
                        sh 'pip install selenium'
                }
            }
        }
    stages {
        stage('Build') {
            steps {
                echo 'Hello, Jenkins!'
                sh 'python3 easyDemo.py'
            }
        }
    }
}
