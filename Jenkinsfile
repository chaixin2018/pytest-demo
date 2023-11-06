def currentTimeMillis = env.BUILD_TIMESTAMP
def formattedDateTime = new Date(currentTimeMillis).format("yyyy-MM-dd_HH:mm:ss")

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
                 report_info = formattedDateTime
                print("report_info"+report_info)
                sh 'python3 easyDemo.py'
            }
        }
    }
}
