pipeline {
    agent any
        parameters {
        string(name: 'CUSTOM_MESSAGE', defaultValue: 'Hello from Jenkins!', description: 'Message to be echoed')
        string(name: 'GIT_REPO_URL', defaultValue: 'https://github.com/yourusername/your-repository.git', description: 'Git repository URL to clone')

        choice(name: 'ENVIRONMENT', choices: ['dev', 'stage', 'production'], description: 'Select the environment where the pipeline will run')    
    }

    stages {
          stage('Echo Custom Message') {
            steps {
                echo "${params.CUSTOM_MESSAGE}"  // Echo the custom message provided by the user
            }
        }
        
        stage('Clone Git Repositorys') {
            steps {
                git "${params.GIT_REPO_URL}"  // Clone the Git repository URL provided by the user
            }
        }
       stage('Select Environment') {
            steps {
                script {
                    // Print the selected environment
                    echo "Selected environment: ${params.ENVIRONMENT}"
                }
            }
        }
    
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
