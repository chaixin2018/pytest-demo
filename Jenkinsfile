def createVersion() {
    // 定义一个版本号作为当次构建的版本，输出结果 20191210175842_69
    return new Date().format('yyyyMMddHHmmss') + "_${env.BUILD_ID}"
}

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
                print("report_info"+createVersion)
                sh 'python3 easyDemo.py'
            }
        }
    }
}
