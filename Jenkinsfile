pipeline {
    agent any
    
    stages {
        stage('Install Dependencies') {
            steps {
                        echo 'pip install selenium begin'
                        sh 'pip3 install selenium'
                        echo 'pip install selenium finish'
                }
            }
        
        stage('Build') {
            steps {
                echo '111 Hello, Jenkins!'
                sh 'python3 easyDemo.py'
            }
        }
    }
}
