pipeline {
    agent any
    
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                        echo 'pip install selenium begin'
                        sh 'pip install selenium'
                        echo 'pip install selenium finish'
                }
            }
        }
        stage('Build') {
            steps {
                echo 'Hello, Jenkins!'
                sh 'python3 easyDemo.py'
            }
        }
    }
}
