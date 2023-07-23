# Exercise 1 : Call History
# Instructions
# Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.

# Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.

# Add a method called show_call_history. This method should print the call_history.

# Add another attribute called messages to your __init__() method which value is an empty list.

# Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
# to : the number of another Phone object
# from : your phone number (also a Phone object)
# content

# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)

# Test your code !!!

class Phone:
    def __init__(self,phone_number,messages):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
    
    def call (self, other_phone):
        call_data = f"the phone number {self.phone_number} to the number {self.other_phone.phone_number}"
        self.call_history.append(call_data)
        print(call_data)
    
    def show_call_history(self):
        print("Call History:")
        for call in self.call_history:
            print(call)
        
    def send_messages(self, other_phone, content):
        message ={
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        print(f"Message sent to {other_phone.phone_number}: {content}")

    def show_outgoing_messages(self):
        print("Outgoing Messages:")
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(f"To:{message['to']}, Content: {message['content']}")

    def show_incoming_messages(self):
        print("Incoming Messages:")
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(f"From:{message['from']}, Content: {message['content']}")

    def show_messages_from(self, other_phone):
        print(f"Messages from {other_phone.phone_number}:")
        for message in self.messages:
            if message["from"] == other_phone.phone_number:
                print(f"To: {message['to']}, Content: {message['content']}")


#  Test your code
phone1 = Phone("123-456-7890")
phone2 = Phone("987-654-3210")

phone1.call(phone2)
phone2.call(phone1)

phone1.send_message(phone2, "Hello!")
phone2.send_message(phone1, "Hi there!")

phone1.show_call_history()
phone2.show_call_history()

phone1.show_outgoing_messages()
phone2.show_incoming_messages()

phone2.show_messages_from(phone1)

