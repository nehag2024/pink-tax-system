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

        stage('Maven Build and Test') {
            steps {
                dir('maven-app') {
                    sh 'mvn clean test'
                }
            }
        }

        stage('Check Docker') {
            steps {
                sh '/usr/local/bin/docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '/usr/local/bin/docker build -t pink-tag-system .'
            }
        }

    }

}
