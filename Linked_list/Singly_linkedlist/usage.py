"""
Example usage of the SinglyLinkedList data structure.

This script demonstrates typical operations and practical applications
of the SinglyLinkedList implementation.
"""

from Slinkedlist import SinglyLinkedList


def main():
    """
    Demonstrate various operations and use cases for the SinglyLinkedList.
    """
    print("Singly Linked List Example Usage")
    print("--------------------------------")
    
    # Create an empty list
    print("\n1. Creating an empty list")
    llist = SinglyLinkedList()
    print(f"List: {llist}")
    print(f"Is empty: {llist.is_empty()}")
    
    # Add elements
    print("\n2. Adding elements")
    llist.append(10)
    llist.append(20)
    llist.append(30)
    print(f"After appending 10, 20, 30: {llist}")
    
    llist.prepend(5)
    print(f"After prepending 5: {llist}")
    
    llist.insert_at(2, 15)
    print(f"After inserting 15 at position 2: {llist}")
    
    # Access elements
    print("\n3. Accessing elements")
    print(f"Head value: {llist.head_value}")
    print(f"Value at position 2: {llist.get(2)}")
    
    # Search operations
    print("\n4. Search operations")
    print(f"Position of 20: {llist.search(20)}")
    print(f"Contains 25: {llist.contains(25)}")
    
    # Remove elements
    print("\n5. Removing elements")
    removed = llist.remove_head()
    print(f"Removed head: {removed}, List: {llist}")
    
    removed = llist.remove(2)
    print(f"Removed at position 2: {removed}, List: {llist}")
    
    # Iteration
    print("\n6. Iterating over the list")
    print("Elements:", end=" ")
    for value in llist:
        print(value, end=" ")
    print()
    
    # Convert to list
    print("\n7. Converting to Python list")
    py_list = llist.to_list()
    print(f"As Python list: {py_list}")
    
    # Reversing the list
    print("\n8. Reversing the list")
    llist.reverse()
    print(f"Reversed list: {llist}")
    
    # Creating a copy
    print("\n9. Creating a copy")
    llist_copy = llist.copy()
    print(f"Original: {llist}")
    print(f"Copy: {llist_copy}")
    
    # Clear the list
    print("\n10. Clearing the list")
    llist.clear()
    print(f"After clearing: {llist}")
    print(f"Is empty: {llist.is_empty()}")
    
    # Example with different data types
    print("\n11. Using with different data types")
    str_list = SinglyLinkedList(["apple", "banana", "cherry"])
    print(f"String list: {str_list}")
    
    mixed_list = SinglyLinkedList([1, "two", 3.0, [4, 5]])
    print(f"Mixed type list: {mixed_list}")
    
    # Example: Using the linked list as a stack
    print("\n12. Using as a stack")
    demonstrate_stack()
    
    # Example: Using the linked list for undo functionality
    print("\n13. Implementing undo functionality")
    demonstrate_undo()
    
    # Example: Creating a simple playlist
    print("\n14. Music playlist implementation")
    demonstrate_playlist()


def demonstrate_stack():
    """
    Demonstrate using the SinglyLinkedList as a stack.
    """
    stack = SinglyLinkedList()
    
    # Push operations
    stack.prepend("A")
    stack.prepend("B")
    stack.prepend("C")
    print(f"Stack after pushes: {stack}")
    
    # Pop operations
    top = stack.remove_head()
    print(f"Popped: {top}, Stack: {stack}")
    
    top = stack.remove_head()
    print(f"Popped: {top}, Stack: {stack}")


def demonstrate_undo():
    """
    Demonstrate using the SinglyLinkedList for undo functionality.
    """
    class TextEditor:
        """Simple text editor with undo functionality."""
        
        def __init__(self, initial_text=""):
            self.text = initial_text
            self.history = SinglyLinkedList([initial_text])
        
        def add_text(self, new_text):
            """Add text and save to history."""
            self.text += new_text
            self.history.prepend(self.text)
        
        def undo(self):
            """Undo the last change."""
            if len(self.history) > 1:
                self.history.remove_head()  # Remove current state
                self.text = self.history.head_value
            return self.text
    
    # Create text editor
    editor = TextEditor()
    
    # Make some changes
    editor.add_text("Hello ")
    editor.add_text("world!")
    print(f"Current text: {editor.text}")
    
    # Undo changes
    editor.undo()
    print(f"After first undo: {editor.text}")
    
    editor.undo()
    print(f"After second undo: {editor.text}")


def demonstrate_playlist():
    """
    Demonstrate using the SinglyLinkedList as a music playlist.
    """
    class Song:
        """Simple song class for the playlist."""
        
        def __init__(self, title, artist):
            self.title = title
            self.artist = artist
        
        def __str__(self):
            return f"{self.title} by {self.artist}"
    
    class MusicPlayer:
        """Simple music player with playlist functionality."""
        
        def __init__(self):
            self.playlist = SinglyLinkedList()
            self.current_index = 0
        
        def add_song(self, title, artist):
            """Add a song to the playlist."""
            self.playlist.append(Song(title, artist))
        
        def play(self):
            """Play the current song."""
            if self.playlist.is_empty():
                return "Playlist is empty"
            
            songs = self.playlist.to_list()
            if self.current_index >= len(songs):
                self.current_index = 0
            
            current_song = songs[self.current_index]
            return f"Now playing: {current_song}"
        
        def next_song(self):
            """Move to the next song."""
            self.current_index += 1
            if self.current_index >= len(self.playlist):
                self.current_index = 0
            return self.play()
        
        def show_playlist(self):
            """Show all songs in the playlist."""
            if self.playlist.is_empty():
                return "Playlist is empty"
            
            result = "Playlist:\n"
            for i, song in enumerate(self.playlist):
                prefix = "▶️ " if i == self.current_index else "  "
                result += f"{prefix}{i+1}. {song}\n"
            return result
    
    # Create music player
    player = MusicPlayer()
    
    # Add songs
    player.add_song("Bohemian Rhapsody", "Queen")
    player.add_song("Imagine", "John Lennon")
    player.add_song("Yesterday", "The Beatles")
    
    # Show playlist
    print(player.show_playlist())
    
    # Play songs
    print(player.play())
    print(player.next_song())
    print(player.next_song())
    
    # Show updated playlist
    print(player.show_playlist())


if __name__ == "__main__":
    main()