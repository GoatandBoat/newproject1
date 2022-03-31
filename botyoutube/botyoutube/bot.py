

		
from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the outlook email.
        self.browse("http://www.outlook.com")
        
        #Create a new message
        if not self.find( "newmessage", matching=0.97, waiting_time=40000):
            self.not_found("newmessage")
        self.click("newmessage")

        #sending a message
        if not self.find( "sendmessage", matching=0.97, waiting_time=40000):
            self.not_found("sendmessage")
        self.click("sendmessage")
        
        #writing the email
        self.paste ("brunobezerra66@gmail.com")
        self.enter()
        if not self.find( "writeyourmessage", matching=0.97, waiting_time=10000):
            self.not_found("writeyourmessage")
        self.click("writeyourmessage")
        

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()









