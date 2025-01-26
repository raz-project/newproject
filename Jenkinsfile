pipeline {
    agent any

    stages {
               stage('Install Python') {
            steps {
                script {
                    // For Windows, you can use PowerShell to install Python
                    powershell '''
                        # Check if Python is already installed
                        if (-Not (Get-Command python -ErrorAction SilentlyContinue)) {
                            Write-Host "Installing Python..."
                            Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.6/python-3.9.6.exe -OutFile python-installer.exe
                            Start-Process -FilePath python-installer.exe -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -NoNewWindow -Wait
                        } else {
                            Write-Host "Python is already installed."
                        }
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
                // Make sure Python is installed and available on the agent
                script {
                    // Assuming the Python script is in the repository
                    bat 'employeeDict.py'
                }
            }
        }
    
    }
}
