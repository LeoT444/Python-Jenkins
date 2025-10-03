pipeline {
    agent any
   
    stages {
        stage('Build') {
            steps {
                echo 'Iniciando Build...'
                sh 'docker build -t myapp:latest ./app'
            }
        }
       
        stage('Test') {
            steps {
                echo 'Executando Testes...'
                sh '''
                    docker run --rm myapp:latest python test_app.py
                '''
            }
        }
       
        stage('Deploy') {
            steps {
                echo 'Realizando Deploy...'
                sh '''
                    docker stop myapp || true
                    docker rm myapp || true
                    docker run -d --name myapp -p 80:80 myapp:latest
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