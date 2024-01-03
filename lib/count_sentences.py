#!/usr/bin/env python3

class MyString:
  
    def __init__(self, value):
        self._value = value  

    
    def value(self):
        return self._value

    
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        
        modified_value = self._value.replace('!', '.').replace('?', '.')
        
        sentences = [sentence.strip() for sentence in modified_value.split('.') if sentence]
        return len(sentences)


my_string = MyString("Hello World.")
print(my_string.is_sentence())  
print(my_string.is_question())  
print(my_string.is_exclamation())  
print(my_string.count_sentences())  


my_question = MyString("Is anybody there?")
print(my_question.is_sentence())  
print(my_question.is_question())  
print(my_question.is_exclamation())  
print(my_question.count_sentences())  


my_exclamation = MyString("It's me!")
print(my_exclamation.is_sentence())  
print(my_exclamation.is_question()) 
print(my_exclamation.is_exclamation())  
print(my_exclamation.count_sentences())  # Output: 1

# Example with multiple sentences
my_multi_sentence = MyString("Hello! How are you? I hope you're doing well.")
print(my_multi_sentence.count_sentences())  # Output: 3

  
