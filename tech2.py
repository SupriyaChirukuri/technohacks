import re
import email
from email.parser import Parser

class EmailAnalyzer:
    def __init__(self, email_content):
        self.email_content = email_content
        self.parser = Parser()
        self.email = self.parser.parsestr(email_content)

    def check_from_field(self):
        from_field = self.email.get('From')
        if not from_field:
            return "No 'From' field found."
        if not re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", from_field):
            return "Invalid 'From' field. It should be in the format 'user@domain.com'."
        return None

    def check_to_field(self):
        to_field = self.email.get('To')
        if not to_field:
            return "No 'To' field found."
        if not re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", to_field):
            return "Invalid 'To' field. It should be in the format 'user@domain.com'."
        return None

    def check_subject(self):
        subject = self.email.get('Subject')
        if not subject:
            return "No 'Subject' field found."
        if len(subject) > 50:
            return "Subject is too long. It should be less than 50 characters."
        return None

    def check_attachments(self):
        attachments = self.email.get_payload()
        if attachments:
            return "Attachments detected. This could be a phishing attempt."
        return None

    def check_links(self):
        links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.email_content)
        if links:
            return "Suspicious links detected. Be cautious."
        return None

    def check_return_path(self):
        return_path = self.email.get('Return-Path')
        if not return_path:
            return "No 'Return-Path' field found."
        if not re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", return_path):
            return "Invalid 'Return-Path' field. It should be in the format 'user@domain.com'."
        return None

    def check_message_id(self):
        message_id = self.email.get('Message-ID')
        if not message_id:
            return "No 'Message-ID' field found."
        if not re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", message_id):
            return "Invalid 'Message-ID' field. It should be in the format 'user@domain.com'."
        return None

    def check_domain_key(self):
        domain_key = self.email.get('Domain-Key')
        if not domain_key:
            return "Domain key is missing. This could be a phishing attempt."
        return None

    def analyze_email(self):
        report = []
        report.append(self.check_from_field())
        report.append(self.check_to_field())
        report.append(self.check_subject())
        report.append(self.check_attachments())
        report.append(self.check_links())
        report.append(self.check_return_path())
        report.append(self.check_message_id())
        report.append(self.check_domain_key())
        return report

    def generate_report(self):
        report = self.analyze_email()
        if any(report):
            print("Red Flags Detected:")
            for item in report:
                if item:
                    print(f"  - {item}")
            print("\nHow to Avoid Such Attacks:")
            print("  - Verify the sender's email address.")
            print("  - Check the subject line for suspicious content.")
            print("  - Be cautious of attachments and links.")
            print("  - Verify the domain key.")
        else:
            print("No Red Flags Detected.")

def main():
    email_content = input("Enter the email content: ")
    analyzer = EmailAnalyzer(email_content)
    analyzer.generate_report()

if __name__ == "__main__":
    main()
