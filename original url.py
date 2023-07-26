import hashlib

class URLShortener:
    def _init_(self):
        self.urls = {}
    
    def shorten_url(self, long_url):
        # Generate a hash of the long URL using hashlib
        hash_object = hashlib.md5(long_url.encode())
        short_code = hash_object.hexdigest()[:6]  # Using the first 6 characters as the short code
        
        # Store the short code and the original URL in a dictionary
        self.urls[short_code] = long_url
        
        # Return the shortened URL
        return f"http://your-short-domain/{short_code}"

    def get_original_url(self, short_code):
        # Retrieve the original URL from the stored dictionary
        return self.urls.get(short_code, None)

# Example usage:
if "_name_" == "_main_":
    shortener = URLShortener()
    original_url = "www.twitter.com"
    
    short_url = shortener.shorten_url(original_url)
    print(f"Shortened URL: {short_url}")
    
    retrieved_url = shortener.get_original_url(short_url.split('/')[-1])
    print(f"Original URL: {retrieved_url}")