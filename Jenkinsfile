pipeline {
    agent {
        label 'python-agent'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo 'GitHub checkout successful'
            }
        }

        stage('Verify Python') {
            steps {
                container('python') {
                    sh 'python --version'
                    sh 'pip --version'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                container('python') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test Application') {
            steps {
                container('python') {
                    sh '''
                        python -c "import app; print('Application import successful')"
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                container('python') {
                    sh 'python -m compileall .'
                }
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