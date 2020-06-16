import facebook

class FbAgent:
    def __init__(self):

        self.__access_token = 'EAANErE4UGlUBAJo9Da3HExGRSKteOaWFPobyKDnwb50mKyYHAv9EkVkkfClLQzPI4bSPZBZByKvDzScm797WJpR0rYAhw9qBMXm5HHt7Kn8ZAAk3isxsfaE9jmb4IFv0POVdknDSn9oZCEQN9F0aV0b3B61tuXs8dzw4jbIPMO8AWb2UL0gDzTE33NsFGCSWkTIRau62iDeSgSA0yDmleRj3HjRBaLsvvu2Axk4MFAZDZD'
        self.graph = facebook.GraphAPI(access_token=self.__access_token, version="7.0")

fb_agent = FbAgent()

fb_agent.graph.put_object(
   parent_object="me",
   connection_name="feed",
   message="This is a great website. Everyone should visit it.",
   link="https://www.facebook.com")
