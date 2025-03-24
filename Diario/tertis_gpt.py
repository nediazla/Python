class persona:
    def __init__(self, nombre, apellido, edad, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.skills = []

    def info_personal(self):
        return f'{self.nombre} {self.apellido} tiene {self.edad} anos y es {self.nacionalidad}'

    def add_skill(self, skill):
        self.skills.append(skill)

class estudiante(persona):
    pass

p = persona('nelson', 'diaz', 40, 'panameno')
s1 = estudiante('edwin', 'frias', 30, 'panameno')

print(s1.info_personal())

s1.add_skill('Python')

print(s1.skills)
print(p.info_personal())

s1.add_skill('Javascript')

print(s1.skills)