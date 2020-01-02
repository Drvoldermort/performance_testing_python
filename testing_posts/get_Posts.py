from locust import TaskSet,task,HttpLocust
class UserBehaviour(TaskSet):
    @task
    def getAllPosts(self):
        self.client.get("/")

class UserBehaviourTwo(TaskSet):
    @task
    def getSinglePost(self):
        self.client.get("/")

class User(HttpLocust):
    task_set = UserBehaviour
    min_wait = 1000
    max_wait = 2000
    host = "https://gorest.co.in/public-api/posts?_format=json&access-token=sBnUCg0pyD75DqsaboRe0BYFH5vHniLyM3AK"

class UserTwo(HttpLocust):
    task_set = UserBehaviourTwo
    min_wait = 1000
    max_wait = 2000
    host = "https://gorest.co.in/public-api/posts/1?_format=json&access-token=sBnUCg0pyD75DqsaboRe0BYFH5vHniLyM3AK"