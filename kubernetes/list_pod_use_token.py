from kubernetes import client

def list_pod():
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6InVjeWJsSDBPRTFpMUM1V2sta1YzOE5xc1M4cHJmVzByblRjMkQ3ck1sa1UifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkYXNoYm9hcmQtYWRtaW4tdG9rZW4tODZuOG4iLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGFzaGJvYXJkLWFkbWluIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiN2E5NjYwMjktOGFiZC00YjFkLTkwNTItMmQyYmU3YWY5N2Y0Iiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmVybmV0ZXMtZGFzaGJvYXJkOmRhc2hib2FyZC1hZG1pbiJ9.bnjv5h86T6-GhiFP4tHZB4JCvfMU6uQIUnBJ5uNiPk5ZY0m7eWq7wHcvG7qJBcQVGg8y1I7WceKxU3XyliOb80BcLEWC_RAgfabZ-JcR3j16vvhyO0ju45Amg2AV2zqD75o8q8B4oVull6CjhajAFL7eV8BPmcw-dqPPW6NiiMjtt2UhoOs8ZIyBA9-e_d4eSurdK_qQ0vEnebr6AUv5SB0GJordkuFrqC_bdLCgSfgrYPK6VxwEy3adlK7OQ_Ke2tNxfgHW9MJFFYKy6CBu3k_hLtsghellu211nLV3uaaFuYjAv-gIsNbXIWy8vRy3rYsZWrFRn088C0bZli5yzg"
    conf = client.Configuration()
    conf.host = "https://192.168.1.135:6443"
    conf.verify_ssl = False
    conf.api_key = {'authorization': 'Bearer ' + token}
    client.Configuration.set_default(conf)
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == "__main__":
    list_pod()