#!/usr/bin/env python3
"""
Simple local test - just sends one email to verify everything works
"""
from main import send_email

if __name__ == "__main__":
    print("🚀 Testing Make-a-Wish Email Scheduler")
    print("📤 Sending test email...")
    
    try:
        send_email()
        print("✅ Test email sent successfully!")
        print("📧 Check your inbox at parchandafalguni@gmail.com and suryaganesan925@gmail.com")
    except Exception as e:
        print(f"❌ Error: {e}")