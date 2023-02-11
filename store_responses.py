## Class to store everything and manage everything
## Need to update so it is a map instead where users are the key and lists of messages are the values

class MessageDataBase:
    def __init__(self) -> None:
        ## Make list a dictionary to easily get
        self.users = {}

    ## Push message to a user if it already exists else make the user and add message
    ## LILO way of storing to kick out oldest
    def addmsg(self, message, user):

        ## If the user is already in the dict
        if user in self.users:
            ## Only store up to 5 messages
            if( len(self.users[user]) > 5 ):
                self.users[user].pop()

            self.users[user].append(message)
        
        ## Make a new entry with the value of a list with just the 1st message
        self.users[user] = [message]

    def getmsgofuser(self, user):
        return self.users[user]