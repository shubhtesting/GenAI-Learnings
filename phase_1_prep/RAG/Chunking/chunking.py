text = """
Our data analyst course lasts for six months. 
Students get access to all recorded classes. 
Live classes happen from Monday to Friday. 
Refund requests are accepted within 7 days of purchase. 
Students must complete all assignments before placement.
Eligible students receive minimum 3 interview opportunities.
"""

chunks = text.strip().split("\n")

for chunk in chunks:
    print("CHUNK:")
    print(chunk)
    print()