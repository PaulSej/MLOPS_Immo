pipeline {
    agent any

    stages {

        stage('Git Checkout') {
            steps {
                git branch: 'release_1.0', credentialsId: 'git-cred', url: 'https://github.com/PaulSej/Les_400_coups_d_Emilien.git'
            }
        }


        stage('Build & Tag Docker Image') {
            steps {
                script {
                     withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker', url: 'hub.docker.com/repository/docker/paulsjn/mlops-immo') {
                         sh "docker compose up -d"
                         
                    }
                }
            }


        stage('Test') {
            steps {
                sh "python end_to_end_test.py"
            }
            
        }

        stage('Switch off app') {
            steps {
                sh "docker compose down"
            }
            
        }
        
        stage('Deliver/Push Docker Image') {
            steps {
                script {
                     withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker', url: 'hub.docker.com/repository/docker/paulsjn/mlops-immo') {
                         sh "docker push paulsjn/frontend:latest"
                         sh "docker push paulsjn/backend:latest"
                    }
                }
            }
        }

        
        stage('Deploy') {
            steps{

                sshagent(credentials : ['ssh-cred']) {
                    sh 'ssh -o StrictHostKeyChecking=no mlops@first-webserver uptime'
                    sh 'ssh -v mlops@first-webserver'
                    sh 'scp ./source/filename user@hostname.com:/remotehost/target'
                }

                sh ssh mlops@192.168.1.14
                sh docker pull paulsjn/docker_project_images
                sh ftp docker-compose.yml
                sh docker compose up -d
            }
        }
    }
}







pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'release_1.0', credentialsId: 'git-cred', url: 'https://github.com/PaulSej/Les_400_coups_d_Emilien.git'
            }
        }
        
        stage('Build & Tag Docker Image') {
            steps {
                script {
                     withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker', url: 'hub.docker.com/repository/docker/paulsjn/mlops-immo') {
                         sh "docker build -t paulsjn/frontend:latest ./frontend"
                         sh "docker build -t paulsjn/backend:latest ./backend"
                    }
                }
            }
            
            
        stage('Push Docker Image') {
            steps {
                script {
                     withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker', url: 'hub.docker.com/repository/docker/paulsjn/mlops-immo') {
                         sh "docker push paulsjn/frontend:latest"
                         sh "docker push paulsjn/backend:latest"
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Hello World'
            }
        }
        
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
}