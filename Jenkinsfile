import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

// 获取当前日期和时间
LocalDateTime now = LocalDateTime.now()
print(now)
// 格式化日期和时间
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")
String formattedDateTime = now.format(formatter)
print(formattedDateTime)
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
