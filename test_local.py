#!/usr/bin/env python3
"""
Local testing script for the Make-a-Wish email scheduler
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

def test_openai_connection():
    """Test OpenAI API connection and quote generation"""
    print("🧪 Testing OpenAI API connection...")
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ OPENAI_API_KEY not found in .env file")
        return False
    
    try:
        client = OpenAI(api_key=api_key)
        print("✅ OpenAI client initialized successfully")
        
        # Test if we can generate a quote
        print("🔄 Generating test quote...")
        response = client.responses.create(
            model="gpt-4o",
            input="You are a wise and inspiring writer. Generate a beautiful, inspiring 6-12 line quote about being hopeful, staying positive, and believing in better days ahead. Make it uplifting and meaningful."
        )
        
        quote = response.output_text.strip()
        print("✅ Quote generated successfully:")
        print(f"📝 {quote}")
        return True
        
    except Exception as e:
        print(f"❌ OpenAI API error: {e}")
        return False

def test_email_config():
    """Test email configuration"""
    print("\n🧪 Testing email configuration...")
    
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    
    if not sender_email:
        print("❌ SENDER_EMAIL not found in .env file")
        return False
    
    if not sender_password:
        print("❌ SENDER_PASSWORD not found in .env file")
        return False
    
    print(f"✅ Sender email configured: {sender_email}")
    print("✅ Sender password configured: [HIDDEN]")
    return True

def test_full_email_send():
    """Test sending actual email"""
    print("\n🧪 Testing email sending functionality...")
    
    # Import the main functions
    try:
        from main import generate_hopeful_quote, send_email
        
        print("✅ Main functions imported successfully")
        
        # Test quote generation
        print("🔄 Testing quote generation...")
        quote = generate_hopeful_quote()
        print(f"✅ Quote: {quote[:50]}...")
        
        # Ask user if they want to send test email
        response = input("\n📧 Do you want to send a test email? (y/n): ").lower().strip()
        
        if response == 'y':
            print("📤 Sending test email...")
            send_email()
            print("✅ Test email sent! Check your inbox.")
        else:
            print("⏭️ Skipping email send test")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing email functionality: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Make-a-Wish Email Scheduler - Local Testing")
    print("=" * 50)
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("📝 Please create a .env file with:")
        print("   SENDER_EMAIL=suryagg925@gmail.com")
        print("   SENDER_PASSWORD=your_gmail_app_password")
        print("   OPENAI_API_KEY=your_openai_api_key")
        return
    
    tests_passed = 0
    total_tests = 3
    
    # Test 1: OpenAI API
    if test_openai_connection():
        tests_passed += 1
    
    # Test 2: Email config
    if test_email_config():
        tests_passed += 1
    
    # Test 3: Full functionality
    if test_full_email_send():
        tests_passed += 1
    
    print("\n" + "=" * 50)
    print(f"🏁 Tests completed: {tests_passed}/{total_tests} passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! Ready for deployment!")
    else:
        print("⚠️ Some tests failed. Please fix the issues before deploying.")

if __name__ == "__main__":
    main()