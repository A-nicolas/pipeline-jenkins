pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build('nicolasdata/pipeline-jenkins')
                }
            }
        }
        stage('Test') {
            steps {
                script{
                    sh 'pip install -r requirements.txt'
                    sh 'pytest'
                }
            }
        }
        stage('Publish') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'credentials_id_docker_hub') {
                        docker.image('nicolasdata/pipeline-jenkins').push()
                    }
                }
            }
        }
    }
}
