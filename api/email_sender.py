from config import Config
import boto3

access_key = "SPARC_PORTAL_USER_ID"
secret_key = "SPARC_PORTAL_ACESS_KEY"
aws_region = "us-east-1"
ses_arn = "SES_ARN"

subject = "Message from SPARC Portal"

ses_client = boto3.client(
    "ses",
    aws_access_key_id=Config.SPARC_PORTAL_AWS_KEY,
    aws_secret_access_key=Config.SPARC_PORTAL_AWS_SECRET,
    region_name=aws_region
)

class EmailSender:
    default_recipient = "jon@blackfynn.com"
    default_subject = "Message from SPARC Portal"
    charset = "UTF-8"
    ses_sender = Config.SES_SENDER
    ses_arn = Config.SES_ARN

    def send_email(self, name, email_address, message):
        ses_client.send_email(
            Source=self.ses_sender,
            Destination={
                "ToAddresses": [
                    self.default_recipient
                ]
            },
            Message={
                "Subject": {
                    "Charset": self.charset,
                    "Data": subject
                },
                "Body": {
                    "Text": {
                        "Charset": self.charset,
                        "Data": message
                    }
                }
            },
            SourceArn=self.ses_arn,
        )