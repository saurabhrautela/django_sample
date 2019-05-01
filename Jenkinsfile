// Dockerhost for build
def dockerhost=''
/ Docker registry where push should be performed
def targetRegistry=''
// Docker image version
def imageVersion='19.0.1'

pipeline{
    agent{
        node{
            label 'sample_node'
            customWorkspace '/home/django_sample/'
        }
    }
    stages{
        stage('Checkout'){
            parallel{
                stage('Clone-repositries from git'){ 
                    steps{
                         checkout scm: [$class: 'GitSCM', branches: [[name: '*/master']],userRemoteConfigs: [[url: 'https://github.com/saurabhrautela/django_boilerplate.git']]]

                        }
                    }
               }
            }
        stage("Building Image"){
            steps {
                script {
                    sh 'rm -f requirements.txt'
                    sh 'pipenv lock -r >> requirements.txt'
                    def img=docker.build("${targetRegistry}/sample:${imageVersion}")
                    docker.withRegistry("https://${targetRegistry}",'docker-registry') {
                        img.push()
                    }
                }
            }
        }
        // Use the following block in case dockerhost is on a seperate machine
        // stage("Building Image"){
        //     steps {
        //         script {
        //             sh 'rm -f requirements.txt'
        //             sh 'pipenv lock -r >> requirements.txt'
        //             docker.withServer("tcp://${dockerhost}:2376",'dockerhost') {
        //                 def img=docker.build("${targetRegistry}/sample:${imageVersion}")
        //                 docker.withRegistry("https://${targetRegistry}",'docker-registry') {
        //                     img.push()
        //                 }
        //             }
        //         }
        //     }
        // }
    }
}
