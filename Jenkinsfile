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
                    sh "docker compose -f docker-compose.ci.yml down"
                }
                
            }
        
            stage('Deliver/Push Docker Image') {
                steps {
                    script {
                        sh "docker image ls"
                        
                        withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker') {
                            sh "docker push paulsjn/mlops-immo:frontend"
                            sh "docker push paulsjn/mlops-immo:backend"
                        }
                    }
                }
            }

            stage('Removing image') {
                steps {
                    sh "docker image rm -f 5ca a7d"
                    sh "docker image ls"
                }
            }

        
            stage('Deploy') {
                steps{

                    sshagent(credentials : ['ssh-cred']) {
                        sh '''
                        ssh -o StrictHostKeyChecking=no mlops@192.168.1.14 uptime
                        scp ./docker-compose.prod.yml mlops@first-webserver:/home/mlops/immo-price-prediction-website/
                        '''
                        script {
                            withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker') {
                                sh "ssh -v mlops@192.168.1.14 docker pull paulsjn/mlops-immo:frontend"
                                sh "ssh -v mlops@192.168.1.14 docker pull paulsjn/mlops-immo:backend"
                            }

                        }

                        sh '''
                        ssh -v mlops@192.168.1.14 cd /home/mlops/immo-price-prediction-website/
                        ssh -v mlops@192.168.1.14 docker compose -f docker-compose.prod.yml up -d
                        '''
                        echo "App has been deployed in production with success !"
                    }

                }
            }
    }



}

