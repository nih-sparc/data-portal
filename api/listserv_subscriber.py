from config import Config
import boto3

ses_client = boto3.client(
    "ses",
    aws_access_key_id=Config.SPARC_PORTAL_AWS_KEY,
    aws_secret_access_key=Config.SPARC_PORTAL_AWS_SECRET,
    region_name=Config.AWS_REGION
)

class ListservSubscriber(object):

    def __init__(self):
        self.default_subject = "LISTSERV from SPARC Portal"
        self.charset = "UTF-8"
        self.ses_sender = Config.SES_SENDER
        self.ses_arn = Config.SES_ARN

    def send_email(self, name, email_address):
        body = "SUBscribe NIH-SPARC-INFO " + name
        ses_client.send_email(
            Source=email_address,
            Destination={
                "ToAddresses": [
                    "listserv@list.nih.gov"
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
