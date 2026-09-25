pipeline {

    agent any

    tools {
        maven 'M3'
        jdk 'JDK21'
    }

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
                    sh 'mvn --version'
                    sh 'mvn clean test'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker --version'
                sh 'docker build -t pink-tag-system .'
            }
        }

    }
}
