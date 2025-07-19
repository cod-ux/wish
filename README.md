# Make-a-Wish Email Scheduler

Automatically sends hopeful quotes via email at 11:09 AM and 11:09 PM London time.

## Setup

1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create `.env` file with your credentials:**
   ```
   SENDER_EMAIL=suryagg925@gmail.com
   SENDER_PASSWORD=your_gmail_app_password
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Gmail App Password Setup:**
   - Enable 2FA on your Gmail account
   - Generate an App Password at https://myaccount.google.com/apppasswords
   - Use this App Password, not your regular password

5. **OpenAI API Key:**
   - Get your API key from https://platform.openai.com/api-keys

## Local Testing

Run the script to test email sending:
```bash
python main.py
```

## GitHub Actions Setup

1. **Add these secrets to your GitHub repository:**
   - `SENDER_EMAIL`: Your Gmail address
   - `SENDER_PASSWORD`: Your Gmail App Password  
   - `OPENAI_API_KEY`: Your OpenAI API key

2. **The workflow runs automatically at:**
   - 11:09 AM London time
   - 11:09 PM London time

## Recipients

Emails are sent to:
- parchandafalguni@gmail.com
- suryaganesan925@gmail.com

## Email Format

```
[AI-generated hopeful quote of 6-12 lines]

Make-a-wish
```