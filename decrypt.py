import base64
import pyperclip
import sys

def clipboard(text):
	pyperclip.copy(text)
	pyperclip.paste()

# x Parameter MUST be a byte
def decode(x):
	decoded = str(base64.b64decode(bytes(x, "utf-8")))

	try:
		first_part = decoded.split("b\"")
		second_part = first_part[1].split("\"")
	except:
		first_part = decoded.split("b\'")
		second_part = first_part[1].split("\'")

	return str(second_part[0])

if __name__ == "__main__":
	a = str(sys.argv[1])

	print("\nHow to use: Put a \"\" between your base64.\n\nOutput: " + decode(a))

	copy_choice = input("\nCopy to clipboard?\n(y/n): ")

	if copy_choice.lower() == "y" or copy_choice.lower() == "yes":
		clipboard(decode(a))
