nombre=("Luis vejarano")
dias="7"

diaslaborados=int(input("ingrese los dias laborados:"))
salario=float(input("ingrese el salario :"))

prima=(salario*diaslaborados)/360
cesantias=(salario*diaslaborados)/360
interesescesantias=(cesantias*0.12)/diaslaborados
vacaciones =(salario*diaslaborados)/720
liquidacion=prima+cesantias+vacaciones+interesescesantias
print (f"señor,{nombre} para los {dias} laborados y salario {salario} su liquidacion se compone asi: prima {prima} cesantias {cesantias} intereses cesantias {interesescesantias} vacaiones {vacaciones}y su liquidacion es {liquidacion}")

