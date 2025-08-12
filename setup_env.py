#!/usr/bin/env python3
"""
Setup script to configure environment variables for OASIS.
This script helps set up your OpenAI API key and other environment variables.
"""

import os
import getpass
from dotenv import load_dotenv, set_key
import shutil

def setup_openai_key():
    """Setup OpenAI API key"""
    print("🔑 Setting up OpenAI API Key")
    print("=" * 50)
    
    # Check if key already exists
    existing_key = os.getenv('OPENAI_API_KEY')
    if existing_key:
        print(f"✅ OpenAI API key is already set (starts with: {existing_key[:10]}...)")
        update = input("Do you want to update it? (y/N): ").lower().strip()
        if update != 'y':
            return existing_key
    
    # Get new API key
    while True:
        api_key = getpass.getpass("Enter your OpenAI API key: ").strip()
        if api_key:
            break
        print("❌ API key cannot be empty. Please try again.")
    
    # Set the environment variable for current session
    os.environ['OPENAI_API_KEY'] = api_key
    
    print("✅ OpenAI API key has been set for this session.")
    print()
    print("📋 To make this permanent, add the following to your shell profile:")
    print("   For zsh (default on macOS): ~/.zshrc")
    print("   For bash: ~/.bashrc or ~/.bash_profile")
    print()
    print(f"   export OPENAI_API_KEY='{api_key}'")
    print()
    
    return api_key

def setup_optional_base_url():
    """Setup optional OpenAI base URL for proxy services"""
    print("🌐 Setting up OpenAI Base URL (Optional)")
    print("=" * 50)
    
    existing_url = os.getenv('OPENAI_API_BASE_URL')
    if existing_url:
        print(f"✅ OpenAI base URL is already set: {existing_url}")
        update = input("Do you want to update it? (y/N): ").lower().strip()
        if update != 'y':
            return existing_url
    
    base_url = input("Enter OpenAI API base URL (press Enter to skip): ").strip()
    
    if base_url:
        os.environ['OPENAI_API_BASE_URL'] = base_url
        print(f"✅ OpenAI base URL has been set: {base_url}")
        print()
        print("📋 To make this permanent, add to your shell profile:")
        print(f"   export OPENAI_API_BASE_URL='{base_url}'")
        print()
        return base_url
    else:
        print("⏭️  Skipping base URL setup.")
        return None

def check_installation():
    """Check if OASIS is properly installed"""
    print("🔍 Checking OASIS Installation")
    print("=" * 50)
    
    try:
        import oasis
        import camel
        print("✅ OASIS is properly installed")
        print(f"   OASIS version: {getattr(oasis, '__version__', 'unknown')}")
        print(f"   CAMEL version: {getattr(camel, '__version__', 'unknown')}")
        return True
    except ImportError as e:
        print(f"❌ OASIS installation issue: {e}")
        print("   Try running: uv add camel-oasis")
        return False

def check_data_files():
    """Check if required data files exist"""
    print("📁 Checking Data Files")
    print("=" * 50)
    
    data_file = "./data/reddit/user_data_36.json"
    if os.path.exists(data_file):
        print(f"✅ User data file found: {data_file}")
        return True
    else:
        print(f"❌ User data file not found: {data_file}")
        print("   This file should have been downloaded during setup.")
        return False

def main():
    """Main setup function"""
    print("🏝️  OASIS Environment Setup")
    print("=" * 60)
    print()
    
    # Check installation
    if not check_installation():
        return False
    print()
    
    # Check data files
    if not check_data_files():
        return False
    print()
    
    # Setup API key
    api_key = setup_openai_key()
    if not api_key:
        return False
    print()
    
    # Setup optional base URL
    setup_optional_base_url()
    print()
    
    print("🎉 Setup completed successfully!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Run the Reddit simulation: uv run reddit_simulation.py")
    print("2. Check the generated database: ./data/reddit_simulation.db")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        exit(1)
