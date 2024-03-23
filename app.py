class SocialMediaPlatform:
    def __init__(self, name, users):
        self.name = name
        self.users = users

    def authenticate(self, username, password):
        # Authentication logic for each platform
        if username in self.users and self.users[username]['password'] == password:
            print(f"Authenticated with {self.name} as {username}")
            return True
        else:
            print(f"Authentication failed for {username} on {self.name}")
            return False

    def get_user_data(self, username):
        if username in self.users:
            return self.users[username]['data']
        else:
            return None

# Static demo data for users
facebook_users = {
    'user1': {'password': 'pass123', 'data': {'name': 'User One', 'age': 25, 'email': 'user1@example.com'}},
    'user2': {'password': 'pass456', 'data': {'name': 'User Two', 'age': 30, 'email': 'user2@example.com'}}
}

twitter_users = {
    'user3': {'password': 'pass789', 'data': {'name': 'User Three', 'age': 35, 'email': 'user3@example.com'}},
    'user4': {'password': 'pass000', 'data': {'name': 'User Four', 'age': 40, 'email': 'user4@example.com'}}
}

instagram_users = {
    'user5': {'password': 'pass111', 'data': {'name': 'User Five', 'age': 45, 'email': 'user5@example.com'}},
    'user6': {'password': 'pass222', 'data': {'name': 'User Six', 'age': 50, 'email': 'user6@example.com'}}
}

linkedin_users = {
    'user7': {'password': 'pass333', 'data': {'name': 'User Seven', 'age': 55, 'email': 'user7@example.com'}},
    'user8': {'password': 'pass444', 'data': {'name': 'User Eight', 'age': 60, 'email': 'user8@example.com'}}
}

# Create instances for each social media platform
facebook = SocialMediaPlatform("Facebook", facebook_users)
twitter = SocialMediaPlatform("Twitter", twitter_users)
instagram = SocialMediaPlatform("Instagram", instagram_users)
linkedin = SocialMediaPlatform("LinkedIn", linkedin_users)

# Function to select social media platform
def select_social_media():
    print("Select a social media platform:")
    print("1. Facebook")
    print("2. Twitter")
    print("3. Instagram")
    print("4. LinkedIn")
    choice = input("Enter your choice (1-4): ")
    return choice

# Main function
def main():
    choice = select_social_media()
    if choice == '1':
        platform = facebook
    elif choice == '2':
        platform = twitter
    elif choice == '3':
        platform = instagram
    elif choice == '4':
        platform = linkedin
    else:
        print("Invalid choice")
        return

    username = input("Enter username: ")
    password = input("Enter password: ")

    if platform.authenticate(username, password):
        user_data = platform.get_user_data(username)
        if user_data:
            print("User data:", user_data)
        else:
            print("User data not found")

if __name__ == "__main__":
    main()