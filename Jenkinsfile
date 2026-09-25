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
                sh '''
                    mkdir -p "$WORKSPACE/.docker"
                    printf '%s\n' '{\"auths\":{}}' > "$WORKSPACE/.docker/config.json"
                    export DOCKER_CONFIG="$WORKSPACE/.docker"

                    /usr/local/bin/docker --version
                    /usr/local/bin/docker --context desktop-linux build -t pink-tax-system .
                '''
            }
        }

    }
}
