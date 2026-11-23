pipeline {
    agent {
        docker {
            image 'python:3.12'
            args '-u root:root'
        }
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo 'Code checked out successfully'
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
                sh 'pip install Flask==3.1.2'
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

        always {
            echo 'Pipeline execution completed'
        }
    }
}