pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test Python Application') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t pink-tag-system .'
            }
        }

        stage('Docker Build Successful') {
            steps {
                echo 'Pink Tag System Docker image built successfully!'
            }
        }
    }
}
