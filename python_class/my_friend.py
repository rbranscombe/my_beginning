user_feeling = input("how are you? ")
good_emotions = ["good", "great", "happy", "awesome"]
bad_emotions = ["sad", "angry", "tired", "upset"]


if user_feeling in good_emotions:
	print(f"I'm glad you're feeling {user_feeling}")

else:
	if user_feeling in bad_emotions:
		print(f"I'm sorry you're feeling {user_feeling}")

	else:
		print("I truly don't know what that is like.")
