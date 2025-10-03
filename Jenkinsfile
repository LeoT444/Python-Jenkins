pipeline {
    agent any
   
    stages {
        stage('Build') {
            steps {
                echo 'Iniciando Build...'
                sh 'docker build -t pipeline-python:latest ./app'
            }
        }
       
        stage('Test') {
            steps {
                echo 'Executando Testes...'
                sh '''
                    docker run --rm pipeline-python:latest python test_app.py
                '''
            }
        }
       
        stage('Deploy') {
            steps {
                echo 'Realizando Deploy...'
                sh '''
                    docker stop pipeline-python || true
                    docker rm pipeline-python || true
                    docker run -d --name pipeline-python -p 80:80 pipeline-python:latest
                '''
            }
        }
    }
   
    post {
        success {
            echo '✅ Pipeline executado com sucesso!'
        }
        failure {
            echo '❌ Pipeline falhou!'
        }
    }
}