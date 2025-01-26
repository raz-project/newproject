pipeline {
    agent any

    stages {
    stage('Install Python') {
            steps {
                script {
                    // PowerShell script to check and install Python on Windows
                    powershell '''
                        # Check if Python is already installed
                        $pythonInstalled = Get-Command python -ErrorAction SilentlyContinue

                        if (-Not $pythonInstalled) {
                            Write-Host "Python is not installed. Installing..."
                            
                            # Download the Python installer
                            Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.6/python-3.9.6.exe -OutFile python-installer.exe

                            # Install Python silently with PATH added
                            Start-Process -FilePath python-installer.exe -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -NoNewWindow -Wait
                            
                            # Clean up the installer
                            Remove-Item python-installer.exe
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
                script {
                    // Execute the Python script
                    bat 'employeeDict.py'  // Replace 'your-script.py' with your script filename
                }
            }
        }
    
    }
}
