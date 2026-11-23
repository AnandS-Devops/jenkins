pipeline {
    agent {
        label 'python-agent'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                sh 'python --version'
                sh 'pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test Application') {
            steps {
                sh 'python -c "import app; print(\'Application import successful\')"'
            }
        }

        stage('Build') {
            steps {
                sh 'python -m compileall .'
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