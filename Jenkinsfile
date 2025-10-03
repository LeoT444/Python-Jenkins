pipeline {
    agent any
   
    stages {
        stage('Build') {
            steps {
                echo 'Iniciando Build...'
                sh 'docker build -t imagemdaora:latest ./app/'
            }
        }
       
        stage('Test') {
            steps {
                echo 'Executando Testes...'
                sh '''
                    docker run --rm imagemdaora:latest python test_app.py
                '''
            }
        }
       
        stage('Deploy') {
            steps {
                echo 'Realizando Deploy...'
                sh '''
                    docker stop imagemdaora || true
                    docker rm imagemdaora || true
                    docker run -d --name imagemdaora -p 80:80 imagemdaora:latest
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