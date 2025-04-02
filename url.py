import hashlib
import random
import string

def generate_short_url(long_url, url_map):
    """Generates a short URL for a given long URL."""
    hash_object = hashlib.md5(long_url.encode())
    hex_digest = hash_object.hexdigest()
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6)) #Generate a random short code.
    if short_code in url_map.values():
      short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6)) #Ensure uniqueness.

    url_map[short_code] = long_url
    return short_code

def redirect_url(short_code, url_map):
    """Redirects a short URL to its original long URL."""
    if short_code in url_map:
        return url_map[short_code]
    else:
        return None

def main():
    """Main function to run the URL shortener."""
    url_map = {}

    while True:
        print("\nSimple URL Shortener")
        print("1. Shorten URL")
        print("2. Redirect URL")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            long_url = input("Enter long URL: ")
            short_code = generate_short_url(long_url, url_map)
            print(f"Short URL: {short_code}")
        elif choice == "2":
            short_code = input("Enter short URL: ")
            long_url = redirect_url(short_code, url_map)
            if long_url:
                print(f"Redirecting to: {long_url}")
            else:
                print("Short URL not found.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()