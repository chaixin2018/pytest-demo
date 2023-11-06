def currentTimeMillis = env.BUILD_TIMESTAMP

pipeline {
    agent any
    
    stages {
        stage('Install Dependencies') {
            steps {
                        echo 'pip install selenium begin'
                        //sh 'pip3 install selenium'
                        echo 'pip install selenium finish'
                }
            }
        
        stage('Build') {
            steps {
                echo '111 Hello, Jenkins!'
                print("report_info"+currentTimeMillis)
                sh 'python3 easyDemo.py'
            }
        }
    }
}
