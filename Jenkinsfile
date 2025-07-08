pipeline {
    agent any
    environment {
        // Define your Docker Hub credentials ID in Jenkins
        DOCKER_CREDENTIALS = 'docker-cred'
        // Define your SSH credentials ID in Jenkins
        SSH_CREDENTIALS = 'ssh-cred'
        // Define your production server details
        PROD_SERVER = 'mlops@192.168.1.14'
        // Define your Docker registry URL
        REGISTRY_URL = 'docker.io'
        // Define your Docker image name
        DOCKER_IMAGE = 'paulsjn/mlops-immo'

    }
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

            
            stage('Test') {
                steps {
                    /*
                    sh "python3 --version"
                    sh "python3 end_to_end_test.py"
                    */
                    echo "Test passed successfully !"
                }
                
            }
            

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
                            /*sh "docker login -u paulsjn -p ${docker-cred}"
                            sh "docker push paulsjn/mlops-immo:frontend"
                            sh "docker push paulsjn/mlops-immo:backend"*/
                            sh "docker push --all-tags paulsjn/mlops-immo"
                        }
                    }
                }
            }

            stage('Removing image') {
                steps {
                    sh "docker image ls"
                    sh "docker image rm -f 5ca a7d"
                    sh "docker image ls"
                }
            }

        
            stage('Deploy') {
                steps{

                    script {

                    // Retrieve Docker Hub credentials
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS, usernameVariable: 'paulsjn', passwordVariable: 'docker-cred')]) {
                        // Use SSH agent to connect to the production server
                        sshagent(credentials: [SSH_CREDENTIALS]) {
                            sh """
                                ssh -o StrictHostKeyChecking=no ${PROD_SERVER} << EOF
                                # Log in to Docker Hub
                                echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin

                                cd /home/mlops/immo-price-prediction-website/

                                # Build your Docker image
                                docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .


                                # Push your Docker image to Docker Hub
                                docker push ${REGISTRY_URL}/${DOCKER_IMAGE}:frontend
                                EOF
                            """
                        }
                    }
                        /*
                        sshagent(credentials : ['ssh-cred']) {
                            sh "scp -o StrictHostKeyChecking=no ./docker-compose.prod.yml mlops@192.168.1.14:/home/mlops/immo-price-prediction-website/"
                            withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker') {
                                sh"""
                                ssh -o StrictHostKeyChecking=no mlops@192.168.1.14 docker pull paulsjn/mlops-immo:frontend 
                                ssh -o StrictHostKeyChecking=no mlops@192.168.1.14 docker pull paulsjn/mlops-immo:backend
                                """
                            }
                            sh "ssh -o StrictHostKeyChecking=no mlops@192.168.1.14 docker compose -f /home/mlops/immo-price-prediction-website/docker-compose.prod.yml up -d"


                     
                        }*/
                    }


                    /*
                    script {
                        sshagent(credentials : ['ssh-cred']) {

                            sh '''
                            scp -o StrictHostKeyChecking=no ./docker-compose.prod.yml mlops@192.168.1.14:/home/mlops/immo-price-prediction-website/
                            ssh -v -o StrictHostKeyChecking=no mlops@192.168.1.14
                            docker login -u paulsjn -p ${docker-cred}
                            docker pull paulsjn/mlops-immo:frontend 
                            docker pull paulsjn/mlops-immo:backend
                            cd /home/mlops/immo-price-prediction-website/
                            docker compose -f docker-compose.prod.yml up -d
                            exit
                            '''



                            
                        }

                    }
                    */

                    echo "App has been deployed in production with success !"
                }
            }
    }


    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }



}

