print("Welcome to the quiz game")
name=input("Enter your name: ")
print("Rule 1 : You cannot change the answer once entered.")
print("Rule 2 : Play Fairly")

print(f"{name}, you will be answering 10 questions in total.")
que=input("Are you ready?: ")
class Question:
    def __init__(self,question,option,answer):
        self.question=question
        self.option=option
        self.answer=answer
    def display(self):
        print(self.question)
        for i, option in enumerate(self.option,start=1):
          print(f"{i}.{option}")
        choice=int(input("Enter your choice(1-4): "))
        if self.option[choice-1]==self.answer:
            print("correct!")
            return 1
        else:
            print(f"Wrong, the correct answer is {self.answer}")
            return 0

q1=Question("Who was the first female doctor of India?",
                ["Marie Curie", "Anandi Bai Joshi", "Diana","Bandita Sinha"],
                "Anandi Bai Joshi")

q2=Question("Who wrote the indian national anthem?", ["Swami Vivekanand", "Rabindranath Tagore", "Lokmanya Tilak", "Mahatma Gandhi"], "Rabindranath Tagore")

q3=Question("Who was the first prime minister of India?",["Indira Gandhi", "Abdul Kalam", "Narendra Modi", "Jawaharlal Nehru"], "Jawaharlal Nehru")
 
q4=Question("Which is the highest mountain peak in India?", ["Kanchenjunga", "Mt. Everest", "Aravali Hills", "Himalayas"], "Kanchenjunga")

q5=Question("Which City is called as the pink city of India?", ["Jaipur", "Mumbai", "Delhi", "Bangalore"], "Jaipur")

q6=Question("Which Indian cricketer won the ‘Padma Bhushan’ in 2018?", ["Virat Kohli", "Gautam Gambhir", "MS Dhoni", "Rohit Sharma"], "MS Dhoni")

q7=Question("Where is the headquarters of ISRO located?", ["Mumbai", "Pune", "Bangalore", "Delhi"], "Bangalore")

q8=Question(" Which is the longest river in India?",["Ganga", "Yamuna", "Indus", "Brahmaputra"], "Ganga")

q9=Question("Which is the national sport of India?", ["Tennis", "Cricket", "Hockey","Badminton"], "Hockey")

q10=Question("When did India get independence?", ["1947", "1990", "1765", "1948"], "1947")

score=0
score+=q1.display()
score+=q2.display()
score+=q3.display()
score+=q4.display()
score+=q5.display()
score+=q6.display()
score+=q7.display()
score+=q8.display()
score+=q9.display()
score+=q10.display()

print(f"\nYour total score is : {score} points")



                
        

