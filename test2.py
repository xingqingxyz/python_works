#!/usr/bin/python
import emoji

result1 = emoji.emojize("Python is :red_heart:", language="alias",
                        variant="text_type")
result2 = emoji.emojize("Python is a_thumbs_up_a", delimiters=("a_", "_a"))
print(result1)
print(result2)
print("hello world")

