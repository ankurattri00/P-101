import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f= open(file_from,'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BJqsKGw2uqgAmMoelC5JjcpOVicAhrDOg8g7U4AiKO422eYtslLqZGy7dB_86LQQpjclL4Ai7x9bIwRgrRYCP44iwDrwp3dxZgsheUIekw7lJwNB4pS5Vk9TsUi-pq9Bc0IbIA4'
    transferData = TransferData(access_token)

   # file_from = input("Enter The File You Want To Upload: ")
    file_from = 'example.txt'
    file_to = '/ankur' + '/' + file_from # The full path to upload the file to, including the file name
 #   file_to=input("enter the full path to upload to dropbox ")
    # API v2
   # try:
    transferData.upload_file(file_from, file_to)
    print("file uploaded")
    #except:
     #   print("something went wrong")


main()
