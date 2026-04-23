from pyscript import display, document

# Define a class to represent a classmate
class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

# Method to introduce the classmate
    def introduce(self):
        return (    
            f"Hi! I am {self.name} from {self.section}. "
            f"My favorite subject is {self.favorite_subject}."
        )

# Initial classmates list with at least 5 different classmates
classmates = [
    Classmate("Jake, Andes", "Topaz", "Math"),
    Classmate("Fil, Ayala", "Topaz", "Science"),
    Classmate("Martina, Cabrillos", "Topaz", "English"),
    Classmate("Mary, Daed", "Topaz", "Filipino"),
    Classmate("Gabrielle, Damondamon", "Topaz", "Social Studies"),
]

# Display all classmates and their introductions
def displayClassmates(e):
    output = document.getElementById("playerOutput")
    output.innerHTML = "<strong>Classmate List:</strong><br><br>"

    for i, classmate in enumerate(classmates, start=1):
        output.innerHTML += f"{i}. {classmate.introduce()}<br>"

# Add a new classmate from the input fields
def addClassmate(e):
    name_input = document.getElementById("playerName")
    section_input = document.getElementById("section")
    subject_input = document.getElementById("favoriteSubject")
    output = document.getElementById("playerOutput")

    name = name_input.value.strip()
    section = section_input.value.strip()
    favorite_subject = subject_input.value.strip()

    if not name or not section or not favorite_subject:
        output.innerHTML = "<span style='color: red;'>Please fill in all fields before adding a classmate.</span>"
        return

    # Create a new classmate object and add it to the classmates list
    classmates.append(Classmate(name, section, favorite_subject))
    output.innerHTML = f"<span style='color: green;'>Added {name} successfully.</span><br><br>"

    name_input.value = ""
    section_input.value = ""
    subject_input.value = ""