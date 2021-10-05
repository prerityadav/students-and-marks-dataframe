import pandas as pd
 
student_data = pd.DataFrame(
    {
        "students": ["bob","preyansh","prerit", "rob"],
        "marks": ["4/10"," 10/10","9/10", "10/10"]

    }
)


print(student_data)
print("preyansh and rob got full marks")
print("preyansh got full marks in english")
print("rob got full marks in maths")