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
                        sh "docker --version"
                        sh "docker compose -f docker-compose.ci.yml up -d"
                        

                }
            }

            /*
            stage('Test') {
                steps {
                    sh "python3 --version"
                    sh "python3 end_to_end_test.py"
                }
                
            }
            */

            stage('Switch off app') {
                steps {
                    sh "docker compose down"
                }
                
            }
        
            stage('Deliver/Push Docker Image') {
                steps {
                    script {
                        withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker', url: 'hub.docker.com/repository/docker/paulsjn/mlops-immo') {
                            sh "docker push paulsjn/mlops-immo:frontend"
                            sh "docker push paulsjn/mlops-immo:backend"
                        }
                    }
                }
            }

        
            stage('Deploy') {
                steps{

                    sshagent(credentials : ['ssh-cred']) {
                        sh '''
                        ssh -o StrictHostKeyChecking=no mlops@first-webserver uptime
                        scp ./docker-compose.prod.yml mlops@first-webserver:/home/mlops/immo-price-prediction-website/
                        '''
                        script {
                            withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker', url: 'hub.docker.com/repository/docker/paulsjn/mlops-immo') {
                                sh "ssh -v mlops@first-webserver docker pull paulsjn/mlops-immo:frontend"
                                sh "ssh -v mlops@first-webserver docker pull paulsjn/mlops-immo:backend"
                            }

                        }

                        sh '''
                        cd /home/mlops/immo-price-prediction-website/
                        ssh -v mlops@first-webserver docker compose -f docker-compose.prod.yml up -d
                        '''
                        echo "App has been deployed in production with success !"
                    }

                }
            }
    }



}

