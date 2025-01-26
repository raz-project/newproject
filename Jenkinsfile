pipeline {
    agent any

    stages {
        stage('Install Python and Virtual Environment') {
            steps {
                script {
                    // Install dependencies and Python if necessary
                    sh '''
                        # Update package list and install Python if not already installed
                        sudo apt-get update
                        sudo apt-get install -y python3 python3-pip python3-venv

                        # Create and activate virtual environment
                        python3 -m venv venv
                        source venv/bin/activate
                    '''
                }
            }
        }
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
                script {
                    // Activate the virtual environment and run Python script
                    sh '''
                        source venv/bin/activate
                        python https://github.com/raz-project/newproject/blob/master/employeeDict.py
                    '''
                }
            }
        }
    
    }
}
