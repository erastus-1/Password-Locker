class Credentials:
    '''
    Class that generates new instances of credentials.
    '''
     
    credential_list =[] #empty credential list

    def __init__(self,first_name,second_name,account,username,password):

       self.first_name = first_name
       self.second_name = second_name
       self.account = account
       self.username = username
       self.password = password

