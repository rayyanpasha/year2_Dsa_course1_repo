import time

# Node class to represent each tweet
class TweetNode:
    def __init__(self, content):
        self.content = content
        self.timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.next = None

# LinkedList class to represent the Twitter feed
class TwitterFeed:
    def __init__(self):
        self.head = None

    # Add a new tweet at the beginning of the list
    def add_tweet(self, content):
        new_tweet = TweetNode(content)
        new_tweet.next = self.head  # Point the new tweet to the current head
        self.head = new_tweet  # The new tweet becomes the new head of the list
        print(f"Tweet added: '{content}' at {new_tweet.timestamp}")

    # Display all tweets from most recent to oldest
    def display_feed(self):
        if self.head is None:
            print("The feed is empty.")
            return
        current = self.head
        print("Twitter Feed (Most Recent First):")
        while current:
            print(f"[{current.timestamp}] {current.content}")
            current = current.next  # Move to the next node (tweet)

    # Delete a tweet by content (delete first matching tweet)
    def delete_tweet(self, content):
        current = self.head
        previous = None

        # Check if the head node itself holds the content to be deleted
        if current and current.content == content:
            self.head = current.next  # Move head to the next tweet
            print(f"Deleted tweet: '{content}'")
            return

        # Traverse the list to find the tweet to delete
        while current and current.content != content:
            previous = current
            current = current.next

        # If tweet not found in the list
        if current is None:
            print(f"Tweet '{content}' not found.")
            return

        # Unlink the node from the linked list
        previous.next = current.next
        print(f"Deleted tweet: '{content}'")


# Example usage:
feed = TwitterFeed()

# Adding tweets
feed.add_tweet("Hello, world!")
feed.add_tweet("Learning Linked Lists!")
feed.add_tweet("This is my third tweet.")

# Displaying the feed
feed.display_feed()

# Deleting a tweet
feed.delete_tweet("Learning Linked Lists!")

# Displaying the feed again after deletion
feed.display_feed()
