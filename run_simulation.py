#!/usr/bin/env python3
"""
Wrapper script to run the Reddit simulation with proper environment setup.
This ensures the OpenAI API key is properly configured before running the simulation.
"""

import os
import sys
import getpass
from reddit_simulation import main
import asyncio

def check_and_setup_api_key():
    """Check if OpenAI API key is set, and prompt for it if not"""
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("🔑 OpenAI API Key Required")
        print("=" * 50)
        print("OASIS requires an OpenAI API key to function.")
        print("You can get one from: https://platform.openai.com/api-keys")
        print()
        
        while True:
            api_key = getpass.getpass("Enter your OpenAI API key: ").strip()
            if api_key:
                os.environ['OPENAI_API_KEY'] = api_key
                break
            print("❌ API key cannot be empty. Please try again.")
        
        print("✅ API key set successfully!")
        print()
    
    # Check for optional base URL
    base_url = os.getenv('OPENAI_API_BASE_URL')
    if not base_url:
        use_custom = input("Use custom OpenAI base URL? (y/N): ").lower().strip()
        if use_custom == 'y':
            base_url = input("Enter OpenAI base URL: ").strip()
            if base_url:
                os.environ['OPENAI_API_BASE_URL'] = base_url
                print(f"✅ Custom base URL set: {base_url}")
    
    return True

def main_wrapper():
    """Main wrapper function"""
    print("🏝️  OASIS Reddit Simulation")
    print("=" * 60)
    print()
    
    # Setup environment
    if not check_and_setup_api_key():
        print("❌ Failed to set up API key. Exiting.")
        return False
    
    print("🚀 Starting Reddit simulation...")
    print("=" * 60)
    print()
    
    try:
        # Run the main simulation
        asyncio.run(main())
        return True
    except Exception as e:
        print(f"❌ Simulation failed: {e}")
        print()
        print("💡 Troubleshooting tips:")
        print("1. Check your OpenAI API key is valid")
        print("2. Ensure you have sufficient API credits")
        print("3. Check your internet connection")
        print("4. Try using GPT-4O-MINI if you hit rate limits")
        return False

if __name__ == "__main__":
    success = main_wrapper()
    if success:
        print("🎉 Simulation completed successfully!")
        print()
        print("📊 Check the results:")
        print("   - Database: ./data/reddit_simulation.db")
        print("   - Agent interactions logged in the terminal above")
    else:
        sys.exit(1)
