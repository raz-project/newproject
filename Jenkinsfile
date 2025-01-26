pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
             stage('Hello World') {
                 steps{
        echo 'Hello World'
    }
             }
             stage('Clone Git Repository') {
            steps {
                // Replace with your Git repository URL
                git 'https://github.com/raz-project/newproject.git'
            }
        }
              stage('Execute Python Script') {
            steps {
                // Make sure Python is installed and available on the agent
                script {
                    // Assuming the Python script is in the repository
                    sh 'python3 https://github.com/raz-project/newproject/blob/master/employeeDict.py'
                }
            }
        }
    
    }
}
