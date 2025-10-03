pipeline {
    agent any
   
    stages {
        stage('Build') {
            steps {
                echo 'Iniciando Build...'
                sh 'docker build -t jenkins:latest ./app'
            }
        }
       
        stage('Test') {
            steps {
                echo 'Executando Testes...'
                sh '''
                    docker run --rm jenkins:latest python test_app.py
                '''
            }
        }
       
        stage('Deploy') {
            steps {
                echo 'Realizando Deploy...'
                sh '''
                    docker stop jenkins || true
                    docker rm jenkins || true
                    docker run -d --name jenkins -p 80:80 jenkins:latest
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