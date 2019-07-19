from config import Config
import boto3

subject = "Message from SPARC Portal"

ses_client = boto3.client(
    "ses",
    aws_access_key_id=Config.SPARC_PORTAL_AWS_KEY,
    aws_secret_access_key=Config.SPARC_PORTAL_AWS_SECRET,
    region_name=Config.AWS_REGION
)

class EmailSender(object):

    def __init__(self):
        self.default_subject = "Message from SPARC Portal"
        self.charset = "UTF-8"

    def send_email(self, name, email_address, message):
        body = name + "\n" + message
        ses_client.send_email(
            Source=self.ses_sender,
            Destination={
                "ToAddresses": [
                    email_address
                ]
            },
            Message={
                "Subject": {
                    "Charset": self.charset,
                    "Data": self.default_subject
                },
                "Body": {
                    "Text": {
                        "Charset": self.charset,
                        "Data": body
                    }
                }
            },
            SourceArn=self.ses_arn,
        )