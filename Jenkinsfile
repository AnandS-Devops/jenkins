pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code checkout from GitHub'
            }
        }

        stage('Verify Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test Application') {
            steps {
                sh 'python3 -c "import app; print(\'Application import successful\')"'
            }
        }

        stage('Build') {
            steps {
                echo 'Application build completed'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}