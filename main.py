import smtplib
import schedule
import time
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from openai import OpenAI
import pytz

# Load environment variables
load_dotenv()

# Email configuration
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
RECIPIENTS = ['parchandafalguni@gmail.com', 'suryaganesan925@gmail.com']

# OpenAI client - using the new Responses API
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_hopeful_quote():
    """Generate a hopeful quote using OpenAI API"""
    try:
        # Try Responses API first (if available)
        if hasattr(client, 'responses'):
            response = client.responses.create(
                model="gpt-4o",
                input="You are a wise and inspiring writer. Generate a beautiful, inspiring 6-12 line quote about being hopeful, staying positive, and believing in better days ahead. Make it uplifting and meaningful."
            )
            return response.output_text.strip()
        else:
            # Fallback to Chat Completions API
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a wise and inspiring writer."},
                    {"role": "user", "content": "Generate a beautiful, inspiring 6-12 line quote about being hopeful, staying positive, and believing in better days ahead. Make it uplifting and meaningful."}
                ],
                max_tokens=200,
                temperature=0.8
            )
            return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating quote: {e}")
        # Fallback quote
        return """Hope is the thing with feathers
That perches in the soul,
And sings the tune without the words,
And never stops at all.
Even in the darkest moments,
Remember that dawn always follows the night."""

def send_email():
    """Send hopeful quote email"""
    try:
        # Generate the quote
        quote = generate_hopeful_quote()
        
        # Create email content
        email_body = f"""{quote}

Make-a-wish"""
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['Subject'] = "Daily Hope 🕐"
        
        # Add body to email
        msg.attach(MIMEText(email_body, 'plain'))
        
        # Gmail SMTP configuration
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        # Send to all recipients
        for recipient in RECIPIENTS:
            msg['To'] = recipient
            text = msg.as_string()
            server.sendmail(SENDER_EMAIL, recipient, text)
            print(f"Email sent to {recipient} at {datetime.now()}")
            del msg['To']  # Remove To header for next recipient
        
        server.quit()
        
    except Exception as e:
        print(f"Error sending email: {e}")

def run_scheduler():
    """Run the email scheduler"""
    # London timezone
    london_tz = pytz.timezone('Europe/London')
    
    print("Starting email scheduler...")
    print("Emails will be sent at 11:09 AM and 11:09 PM London time")
    
    # Schedule emails at 11:09 AM and 11:09 PM London time
    schedule.every().day.at("11:09").do(send_email)
    schedule.every().day.at("23:09").do(send_email)
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    print("Make-a-Wish Email Scheduler")
    print("=" * 30)
    
    # Test email sending (optional - comment out for production)
    print("Sending test email...")
    send_email()
    
    # Start scheduler
    # run_scheduler()  # Uncomment to start scheduler