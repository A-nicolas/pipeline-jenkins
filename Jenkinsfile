pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'url_de_votre_depot_git'
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build('nom_de_votre_image:tag')
                }
            }
        }
        stage('Test') {
            steps {
                // Étapes de test de votre application
            }
        }
        stage('Publish') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'credentials_id_docker_hub') {
                        docker.image('nom_de_votre_image:tag').push()
                    }
                }
            }
        }
    }
}
