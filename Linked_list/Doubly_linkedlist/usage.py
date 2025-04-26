"""
Example usage of the DoublyLinkedList data structure.

This module demonstrates practical applications and usage patterns
for the DoublyLinkedList implementation.
"""

from typing import Any, Dict, Optional, TypeVar, Generic
from Dlinkedlist import DoublyLinkedList, Node


def basic_operations_example() -> None:
    """Demonstrate basic DoublyLinkedList operations."""
    print("\n=== BASIC OPERATIONS ===")
    
    # Create a new doubly linked list of integers
    dll = DoublyLinkedList[int]()
    print(f"Created empty list: {dll}")
    
    # Append operations
    dll.append(10)
    dll.append(20)
    dll.append(30)
    print(f"After appending 10, 20, 30: {dll}")
    
    # Prepend operations
    dll.prepend(5)
    dll.prepend(0)
    print(f"After prepending 5, 0: {dll}")
    
    # Access elements by index
    print(f"First element: {dll[0]}")
    print(f"Last element: {dll[-1]}")
    print(f"Middle element: {dll[2]}")
    
    # Modify elements
    dll[1] = 7
    print(f"After changing second element to 7: {dll}")
    
    # Insert at position
    dll.insert_at(3, 15)
    print(f"After inserting 15 at position 3: {dll}")
    
    # Remove operations
    dll.remove_first()
    print(f"After removing first element: {dll}")
    
    dll.remove_last()
    print(f"After removing last element: {dll}")
    
    dll.remove_at(2)
    print(f"After removing element at position 2: {dll}")
    
    # Find and remove a specific value
    node = dll.find(15)
    if node:
        dll.remove(node)
    print(f"After finding and removing 15: {dll}")
    
    # Iterate through the list
    print("Iterating through list:")
    for item in dll:
        print(f"  {item}")
    
    # Check membership
    print(f"Is 7 in the list? {7 in dll}")
    print(f"Is 30 in the list? {30 in dll}")
    
    # Clear the list
    dll.clear()
    print(f"After clearing: {dll}")


def bidirectional_iteration_example() -> None:
    """Demonstrate bidirectional iteration with DoublyLinkedList."""
    print("\n=== BIDIRECTIONAL ITERATION ===")
    
    # Create and populate a list
    dll = DoublyLinkedList[str]()
    words = ["first", "second", "third", "fourth", "fifth"]
    for word in words:
        dll.append(word)
    
    print(f"Original list: {dll}")
    
    # Forward iteration
    print("Forward iteration:")
    current = dll.head
    while current:
        print(f"  {current.data}")
        current = current.next
    
    # Backward iteration
    print("Backward iteration:")
    current = dll.tail
    while current:
        print(f"  {current.data}")
        current = current.prev


def browser_history_example() -> None:
    """Implement a simple browser history using DoublyLinkedList."""
    print("\n=== BROWSER HISTORY EXAMPLE ===")
    
    class BrowserHistory:
        """A simple browser history implementation using DoublyLinkedList."""
        
        def __init__(self, homepage: str):
            """Initialize with a homepage."""
            self.history = DoublyLinkedList[str]()
            self.history.append(homepage)
            self.current = self.history.tail
            print(f"Opened browser at {homepage}")
        
        def visit(self, url: str) -> None:
            """Visit a new URL."""
            # If we're not at the end of history, truncate forward history
            if self.current != self.history.tail:
                # Remove all pages after current
                while self.history.tail != self.current:
                    self.history.remove_last()
            
            # Add the new URL
            self.history.append(url)
            self.current = self.history.tail
            print(f"Visited {url}")
        
        def back(self) -> str:
            """Navigate back in history."""
            if self.current and self.current.prev:
                self.current = self.current.prev
                print(f"Navigated back to {self.current.data}")
                return self.current.data
            else:
                print("Can't go back any further")
                return self.current.data if self.current else ""
        
        def forward(self) -> str:
            """Navigate forward in history."""
            if self.current and self.current.next:
                self.current = self.current.next
                print(f"Navigated forward to {self.current.data}")
                return self.current.data
            else:
                print("Can't go forward any further")
                return self.current.data if self.current else ""
        
        def display_history(self) -> None:
            """Display the full history with current position."""
            print("History:")
            current_page = self.history.head
            index = 0
            current_index = -1
            
            # Find the index of the current page
            temp = self.history.head
            while temp:
                if temp == self.current:
                    current_index = index
                    break
                temp = temp.next
                index += 1
            
            # Reset for actual display
            index = 0
            while current_page:
                marker = " (current)" if index == current_index else ""
                print(f"  {index}: {current_page.data}{marker}")
                current_page = current_page.next
                index += 1
    
    # Usage example
    browser = BrowserHistory("https://www.homepage.com")
    
    browser.visit("https://www.example.com")
    browser.visit("https://www.search.com")
    browser.visit("https://www.results.com")
    
    browser.display_history()
    
    browser.back()
    browser.back()
    
    browser.display_history()
    
    browser.visit("https://www.newpath.com")
    
    browser.display_history()
    
    browser.forward()  # Should say can't go forward


def lru_cache_example() -> None:
    """Implement an LRU (Least Recently Used) Cache using DoublyLinkedList."""
    print("\n=== LRU CACHE EXAMPLE ===")
    
    class LRUCache:
        """
        LRU Cache implementation using a DoublyLinkedList and a dict.
        
        The list maintains the order of items by recency,
        while the dict provides O(1) access to nodes by key.
        """
        
        def __init__(self, capacity: int):
            """Initialize with a fixed capacity."""
            self.capacity = capacity
            self.cache: Dict[Any, Node[tuple[Any, Any]]] = {}  # Maps keys to nodes
            self.list = DoublyLinkedList[tuple[Any, Any]]()  # Stores (key, value) pairs
            print(f"Created LRU cache with capacity {capacity}")
        
        def get(self, key: Any) -> Any:
            """
            Get value from cache by key.
            Also marks the item as recently used.
            """
            if key not in self.cache:
                print(f"Cache miss for key {key}")
                return -1
            
            # Move accessed item to the end (most recently used)
            node = self.cache[key]
            value = node.data[1]
            self.list.remove(node)
            new_node = self.list.append((key, value))
            self.cache[key] = new_node
            
            print(f"Cache hit for key {key}: {value}")
            return value
        
        def put(self, key: Any, value: Any) -> None:
            """
            Put value in cache with given key.
            If key exists, update the value and mark as recently used.
            If cache is full, remove the least recently used item.
            """
            if key in self.cache:
                # Remove existing item
                self.list.remove(self.cache[key])
                print(f"Updated existing key {key} to {value}")
            elif len(self.list) >= self.capacity:
                # Remove least recently used item (front of the list)
                lru_key = self.list.head.data[0] if self.list.head else None
                self.list.remove_first()
                if lru_key is not None:
                    del self.cache[lru_key]
                    print(f"Evicted LRU key {lru_key}")
            else:
                print(f"Added new key {key} with value {value}")
            
            # Add new item to the end (most recently used)
            new_node = self.list.append((key, value))
            self.cache[key] = new_node
        
        def display(self) -> None:
            """Display the current state of the cache."""
            print("Cache contents (LRU -> MRU):")
            current = self.list.head
            while current:
                print(f"  {current.data[0]}: {current.data[1]}")
                current = current.next
    
    # Usage example
    cache = LRUCache(3)
    
    cache.put(1, "One")
    cache.put(2, "Two")
    cache.put(3, "Three")
    
    cache.display()
    
    cache.get(1)  # This moves 1 to the MRU position
    
    cache.display()
    
    cache.put(4, "Four")  # This should evict key 2
    
    cache.display()
    
    cache.get(2)  # Should be a cache miss
    
    cache.get(3)  # Should be a cache hit
    
    cache.display()


def music_playlist_example() -> None:
    """Implement a simple music playlist using DoublyLinkedList."""
    print("\n=== MUSIC PLAYLIST EXAMPLE ===")
    
    class Song:
        """A simple song representation."""
        
        def __init__(self, title: str, artist: str, duration: int):
            """Initialize a song with title, artist, and duration in seconds."""
            self.title = title
            self.artist = artist
            self.duration = duration
        
        def __repr__(self) -> str:
            """Return a string representation of the song."""
            minutes, seconds = divmod(self.duration, 60)
            return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"
    
    class MusicPlayer:
        """A simple music player with playlist functionality."""
        
        def __init__(self):
            """Initialize an empty playlist."""
            self.playlist = DoublyLinkedList[Song]()
            self.current: Optional[Node[Song]] = None
            print("Created new music player")
        
        def add_song(self, song: Song) -> None:
            """Add a song to the end of the playlist."""
            node = self.playlist.append(song)
            
            # If this is the first song, set it as current
            if self.current is None:
                self.current = node
            
            print(f"Added song: {song}")
        
        def play(self) -> None:
            """Play the current song."""
            if self.current:
                print(f"Now playing: {self.current.data}")
            else:
                print("Playlist is empty")
        
        def next_song(self) -> None:
            """Move to the next song in the playlist."""
            if not self.current:
                print("Playlist is empty")
                return
            
            if self.current.next:
                self.current = self.current.next
                print(f"Skipped to next song: {self.current.data}")
            else:
                print("Already at the last song")
        
        def previous_song(self) -> None:
            """Move to the previous song in the playlist."""
            if not self.current:
                print("Playlist is empty")
                return
            
            if self.current.prev:
                self.current = self.current.prev
                print(f"Returned to previous song: {self.current.data}")
            else:
                print("Already at the first song")
        
        def display_playlist(self) -> None:
            """Display all songs in the playlist."""
            print("Current playlist:")
            
            current = self.playlist.head
            index = 1
            while current:
                playing = " (currently playing)" if current == self.current else ""
                print(f"  {index}. {current.data}{playing}")
                current = current.next
                index += 1
            
            if index == 1:
                print("  (Playlist is empty)")
    
    # Usage example
    player = MusicPlayer()
    
    player.add_song(Song("Bohemian Rhapsody", "Queen", 354))
    player.add_song(Song("Stairway to Heaven", "Led Zeppelin", 482))
    player.add_song(Song("Hotel California", "Eagles", 390))
    player.add_song(Song("Sweet Child O' Mine", "Guns N' Roses", 356))
    
    player.display_playlist()
    
    player.play()
    player.next_song()
    player.next_song()
    
    player.display_playlist()
    
    player.previous_song()
    
    player.display_playlist()


def text_editor_example() -> None:
    """Implement a simple text editor using DoublyLinkedList."""
    print("\n=== TEXT EDITOR EXAMPLE ===")
    
    class TextEditor:
        """A simple text editor that stores each line in a doubly linked list."""
        
        def __init__(self):
            """Initialize an empty document."""
            self.lines = DoublyLinkedList[str]()
            self.cursor_line = 0
            print("Created new text editor")
        
        def insert_line(self, line_number: int, text: str) -> None:
            """Insert a line at the specified position."""
            # If inserting past the end, fill with blank lines
            while len(self.lines) < line_number:
                self.lines.append("")
            
            if line_number == len(self.lines):
                self.lines.append(text)
            else:
                self.lines.insert_at(line_number, text)
            
            self.cursor_line = line_number
            print(f"Inserted at line {line_number + 1}: '{text}'")
        
        def delete_line(self, line_number: int) -> None:
            """Delete the line at the specified position."""
            if line_number < 0 or line_number >= len(self.lines):
                print(f"Error: Line {line_number + 1} does not exist")
                return
            
            deleted = self.lines[line_number]
            self.lines.remove_at(line_number)
            
            # Adjust cursor if needed
            if self.cursor_line >= len(self.lines):
                self.cursor_line = max(0, len(self.lines) - 1)
            
            print(f"Deleted line {line_number + 1}: '{deleted}'")
        
        def edit_line(self, line_number: int, text: str) -> None:
            """Replace the content of a line."""
            if line_number < 0 or line_number >= len(self.lines):
                print(f"Error: Line {line_number + 1} does not exist")
                return
            
            old_text = self.lines[line_number]
            self.lines[line_number] = text
            self.cursor_line = line_number
            
            print(f"Edited line {line_number + 1}")
            print(f"  Old: '{old_text}'")
            print(f"  New: '{text}'")
        
        def move_cursor(self, line_number: int) -> None:
            """Move the cursor to the specified line."""
            if line_number < 0 or line_number >= len(self.lines) and len(self.lines) > 0:
                print(f"Error: Line {line_number + 1} does not exist")
                return
            
            self.cursor_line = min(line_number, len(self.lines) - 1) if len(self.lines) > 0 else 0
            
            if len(self.lines) > 0:
                print(f"Moved cursor to line {line_number + 1}: '{self.lines[self.cursor_line]}'")
            else:
                print("Document is empty")
        
        def display_document(self) -> None:
            """Display the entire document with line numbers."""
            print("Document contents:")
            
            for i in range(len(self.lines)):
                cursor = " ← cursor" if i == self.cursor_line else ""
                print(f"  {i + 1}: {self.lines[i]}{cursor}")
            
            if len(self.lines) == 0:
                print("  (Document is empty)")
    
    # Usage example
    editor = TextEditor()
    
    editor.insert_line(0, "# My Document")
    editor.insert_line(1, "")
    editor.insert_line(2, "This is a simple text editor example using a doubly linked list.")
    editor.insert_line(3, "Each line is stored as a node in the list.")
    
    editor.display_document()
    
    editor.edit_line(2, "This is a sophisticated text editor example using a doubly linked list.")
    
    editor.display_document()
    
    editor.delete_line(1)  # Delete the blank line
    
    editor.display_document()
    
    editor.move_cursor(0)
    
    editor.display_document()


def main() -> None:
    """Run all example use cases."""
    print("DOUBLY LINKED LIST EXAMPLE USAGE")
    print("================================")
    
    basic_operations_example()
    bidirectional_iteration_example()
    browser_history_example()
    lru_cache_example()
    music_playlist_example()
    text_editor_example()


if __name__ == "__main__":
    main()