
# ASSignment 3: WhatsApp Chat Data Analysis

n = int(input("Enter the no of messages: "))
chat = {}

# Input messages
for i in range(n):
    name, msg = input().split(':')  # Split only at first ':'
    if name in chat:
        chat[name].append((i, msg.strip()))
    else:
        chat[name] = [(i, msg.strip())]

# Menu loop
while True:
    print("\n--- WhatsApp Chat Analysis Menu ---")
    print("1. Count the number of messages")
    print("2. Identify unique users in the chat")
    print("3. Count total words in chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Most frequent word used by a specific user")
    print("9. Retrieve first & last message by a user")
    print("10. Check if a user is present in chat")
    print("11. Find commonly repeated words")
    print("12. Identify user with longest average message length")
    print("13. Count messages mentioning a specific user")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Extract all questions in chat")
    print("17. Calculate reply ratio between two users")
    print("18. Check for deleted messages")
    print("0. Exit\n")
    
    ch = int(input("Enter your choice: "))

    if ch == 0:
        break

    elif ch == 1:  # Count messages
        total_msg = 0
        for user in chat:
            total_msg += len(chat[user])
        print(f"Total number of messages: {total_msg}")

    elif ch == 2:  # Unique users
        print("Unique users in chat:")
        for i, key in enumerate(chat):
            print(f"{i+1}. {key}")

    elif ch == 3:  # Count total words
        total_words = 0
        for msgs in chat.values():
            for _, msg in msgs:
                total_words += len(msg.split())
        print(f"Total words in the chat: {total_words}")

    elif ch == 4:  # Average words per message
        total_msgs = 0
        total_words = 0
        for msgs in chat.values():
            total_msgs += len(msgs)
            for _, msg in msgs:
                total_words += len(msg.split())
        print(f"Average words per message: {round(total_words / total_msgs, 2)}")

    elif ch == 5:  # Longest message
        longest = ("", "")
        for user, msgs in chat.items():
            for _, msg in msgs:
                if len(msg) > len(longest[1]):
                    longest = (user, msg)
        print(f"Longest message: \"{longest[0]}: {longest[1]}\"")

    elif ch == 6:  # Most active user
        max_user = ("", 0)
        for user, msgs in chat.items():
            if len(msgs) > max_user[1]:
                max_user = (user, len(msgs))
        print(f"Most active user: {max_user[0]} ({max_user[1]} messages)")

    elif ch == 7:  # Message count for a specific user
        name = input("Enter user name: ")
        if name in chat:
            print(f"Messages sent by {name}: {len(chat[name])}")
        else:
            print(f"User '{name}' not found in the chat.")

    elif ch == 8:  # Most frequent word by user
        name = input("Enter user name: ")
        if name in chat:
            words = {}
            for _, msg in chat[name]:
                for w in msg.lower().split():
                    words[w] = words.get(w, 0) + 1
            if words:
                freq_word = max(words, key=words.get)
                print(f"Most frequent word used by {name}: \"{freq_word}\"")
        else:
            print(f"User '{name}' not found in the chat.")

    elif ch == 9:  # First and last message by user
        name = input("Enter user name: ")
        if name in chat:
            print(f"First message by {name}: \"{name}: {chat[name][0][1]}\"")
            print(f"Last message by {name}: \"{name}: {chat[name][-1][1]}\"")
        else:
            print(f"User '{name}' not found in the chat.")

    elif ch == 10:  # Check user presence
        name = input("Enter user name: ")
        if name in chat:
            print(f"User '{name}' is present in the chat.")
        else:
            print(f"User '{name}' not found in the chat.")

    elif ch == 11:  # Commonly repeated words
        word_count = {}
        for msgs in chat.values():
            for _, msg in msgs:
                for w in msg.lower().split():
                    word_count[w] = word_count.get(w, 0) + 1
        common = {w for w, count in word_count.items() if count > 1}
        print(f"Common repeated words: {common}")

    elif ch == 12:  # User with longest average message length
        avg_lengths = {}
        for user, msgs in chat.items():
            total_words = sum(len(msg.split()) for _, msg in msgs)
            avg_lengths[user] = total_words / len(msgs)
        max_user = max(avg_lengths, key=avg_lengths.get)
        print(f"User with longest average message: {max_user} (avg {round(avg_lengths[max_user], 1)} words)")

    elif ch == 13:  # Count messages mentioning a user
        name = input("Enter name to check mentions: ").lower()
        count = 0
        for msgs in chat.values():
            for _, msg in msgs:
                if name in msg.lower():
                    count += 1
        print(f"Messages mentioning '{name.capitalize()}': {count}")

    elif ch == 14:  # Remove duplicate messages
        seen = set()
        unique_msgs = []
        for user, msgs in chat.items():
            for _, msg in msgs:
                if msg not in seen:
                    seen.add(msg)
                    unique_msgs.append(f"{user}: {msg}")
        print(f"Unique messages count: {len(unique_msgs)}")
        for m in unique_msgs:
            print(m)

    elif ch == 15:  # Sort messages alphabetically
        all_msgs = []
        for user, msgs in chat.items():
            for _, msg in msgs:
                all_msgs.append(f"{user}: {msg}")
        for m in sorted(all_msgs):
            print(m)

    elif ch == 16:  # Extract questions
        questions = []
        for user, msgs in chat.items():
            for _, msg in msgs:
                if "?" in msg:
                    questions.append(f"{user}: {msg}")
        if questions:
            print("Questions in chat:")
            for q in questions:
                print(q)
        else:
            print("No questions found in chat.")

    elif ch == 17:  # Reply ratio
        u1, u2 = input("Enter two users (e.g., Alice Bob): ").split()
        if u1 in chat and u2 in chat:
            replies = 0
            for _, msg in chat[u2]:
                if u1.lower() in msg.lower():
                    replies += 1
            print(f"Reply ratio from {u2} to {u1}: {replies} replies")
        else:
            print("One or both users not found.")

    elif ch == 18:  # Deleted messages
        deleted = 0
        for msgs in chat.values():
            for _, msg in msgs:
                if msg.strip().lower() == "this message was deleted":
                    deleted += 1
        print(f"Deleted messages found: {deleted}")

    else:
        print("Invalid choice")
