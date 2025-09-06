pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Princccee/Smart-Doc-AI.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t smart_doc_ai:latest .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop and remove existing container if running
                    sh '''
                    docker ps -q --filter "name=smart_doc_ai" | grep -q . && docker stop smart_doc_ai && docker rm smart_doc_ai || true
                    docker run -d --name smart_doc_ai -p 8001:8001 smart_doc_ai:latest
                    '''
                }
            }
        }
    }
}
